import network
import socket
from time import sleep
from machine import Pin

import machine
import ssd1306
import time
from machine import ADC
import _thread
import neopixel

def oled():
    while True:
        percent = charging_Status_pin.read_u16()
        percent = ((percent-min_percent)/(max_percent-min_percent))*100
        if percent > 0:
            bufferY = "     "+str(int(percent))+"%"
        draw(bufferY)
        time.sleep(0.1)
    
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    pico_led.on()
    sleep(5)
    pico_led.off()
    sleep(5)
    
    return ip

def open_socket(ip):
    # Open a UDP socket
    address = (ip, 8000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(address)
    return sock

def set_led_color(index, red, green, blue):
    """
    Set the color of the specified LED on the neopixel strip.

    Parameters:
    index (int): The index of the LED to set the color for (starting from 0)
    red (int): The intensity of the red color (0-255)
    green (int): The intensity of the green color (0-255)
    blue (int): The intensity of the blue color (0-255)
    """
    pixels[index] = (red, green, blue)
    pixels.write()
    
def clear_led():
    # Turn off all LEDs
    pixels.fill((0, 0, 0))
    pixels.write()

def draw(bufferY):
    display.fill(0)  # Clear the display
    display.text(bufferX, 0, 20)
    display.text(bufferY, 0, 40)
    display.show()
    
def serve(sock):
    #Start a web server
    state = 'OFF'
    pico_led.off()
    temperature = 0
    while True:
        data, addr = sock.recvfrom(2048)
        print("Connected by", addr)
        data = data.decode().strip()
        data = float(data)
        step_number = (data % 10) * 256
        count = 0
        print("data = " + str(data))
        print("step_number = " + str(step_number/512))
        if data < 20:
            pico_led.on()
            sleep(0.5)
            pico_led.off()
            sleep(0.5)
            #sock.sendto("Mini robot is going straight\r\n".encode(), addr)
            while count <= step_number:
                count += 1
                for step in full_step_sequence:
                    for i in range(len(pins)):
                        pins[i].value(step[i])
                        pins2[i].value(step[i])
                        sleep(0.0015)
                    
        elif data < 30:
            #sock.sendto("Mini robot is going straight\r\n".encode(), addr)
            while count <= step_number:
                count += 1
                for step in full_step_sequence_b:
                    for i in range(len(pins)):
                        pins[i].value(step[i])
                        pins2[i].value(step[i])
                        sleep(0.0015)
                    
        elif data < 40:
            #sock.sendto("Mini robot is going straight\r\n".encode(), addr)
            while count <= step_number:
                count += 1
                for step in full_step_sequence:
                    for i in range(len(pins)):
                        pins[i].value(step[i])
                        pins2[i].value([0,0,0,0])
                        sleep(0.0015)
                    
        elif data < 50:
            #sock.sendto("Mini robot is going straight\r\n".encode(), addr)
            while count <= step_number:
                count += 1
                for step in full_step_sequence:
                    for i in range(len(pins)):
                        pins[i].value([0,0,0,0])
                        pins2[i].value(step[i])
                        sleep(0.0015)
                    
        else:
            #sock.sendto("YOU TYPED A MEANINGLESS BUTTON\r\n".encode(), addr)
            continue

if __name__ == "__main__":
    ssid = 'mechalab_intra'
    password = 'mechastudent'
    
    # Define I2C pins
    i2c = machine.I2C(0, scl=machine.Pin(5), sda=machine.Pin(4))

    percent = 0
    max_percent = 55200
    min_percent = 20000 # 48500
    pin_number = 28
    charging_Status_pin = ADC(pin_number)


    # Initialize SSD1306 OLED display
    display = ssd1306.SSD1306_I2C(128, 64, i2c)

    bufferX = "     TOGG"
    bufferY = "     0%"
    
    pins = [
        Pin(26, Pin.OUT),
        Pin(22, Pin.OUT),
        Pin(21, Pin.OUT),
        Pin(20, Pin.OUT),
        ]
    pins2 = [
        Pin(19, Pin.OUT),
        Pin(18, Pin.OUT),
        Pin(17, Pin.OUT),
        Pin(16, Pin.OUT),
        ]
    full_step_sequence = [
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1],
        ]
    full_step_sequence_b = [
        [0,0,0,1],
        [0,0,1,0],
        [0,1,0,0],
        [1,0,0,0],
        ]
    
    # Set up neopixel on GPIO 15 with 12 LEDs
    pixels = neopixel.NeoPixel(Pin(0), 12)
    pico_led = Pin("LED", Pin.OUT)

    try:
        _thread.start_new_thread(oled, ())
        ip = connect()
        sock = open_socket(ip)
        serve(sock)
    except KeyboardInterrupt:
        machine.reset()