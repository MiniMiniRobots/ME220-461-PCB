import network, socket, time, machine, ssd1306, _thread, neopixel
from time import sleep
from machine import Pin, ADC

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    tryCount = 0
    while wlan.isconnected() == False and tryCount < 10:
        print('Waiting for connection...')
        sleep(1)
        tryCount += 1
    if wlan.isconnected() == False:
        print('Connection failed')
        return None
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

def oled():
    while True:
        robotIdStr = f'0{robot_id}' if robot_id < 10 else str(robot_id)
        # Get the battery voltage
        percent = battery_voltage_pin.read_u16()
        # Charging status
        status = charging_status_pin.value()
        percent = ((percent-min_percent)/(max_percent-min_percent)) * 100  # Calculate the percentage
        percent = round(percent)  # Round the percentage to 2 decimal places
        # Convert the percentage to an integer
        percent = int(percent) if percent < 100 else 100 if percent > 0 else 0
        percentStr = f'00{str(percent)}' if percent < 10 else f'0{str(percent)}' if percent < 100 else '100'
        infoMessage = f'{robotIdStr}.{str(status)}{str(percentStr)}'
        # Send the percentage to the server
        client_socket.sendto(str(infoMessage).encode(), (transmitter_ip, 8000))
        if percent > 0:
            bufferY = f'     {str(percent)}%'
        else:
            bufferY = f'     0%'
        draw(bufferY)  # Draw the buffer
        time.sleep(0.1)  # Sleep for 0.1 seconds

def draw(bufferY):
    display.fill(0)  # Clear the display
    display.text(bufferX, 0, 20)
    display.text(bufferY, 0, 40)
    display.show()

def set_neopixel_color(index, red, green, blue):
    """
    Set the color of the specified LED on the neopixel strip.

    Parameters:
    index (int): The index of the LED to set the color for (starting from 0)
    red (int): The intensity of the red color (0-255)
    green (int): The intensity of the green color (0-255)
    blue (int): The intensity of the blue color (0-255)
    """
    try:
        if index == "all":
            for i in range(4):
                pixels[i] = (red, green, blue)
        else:
            pixels[index] = (red, green, blue)
        pixels.write()
    except:
        print("Error: No neopixel strip is connected.")

def serve(sock):
    #Start a web server
    state = 'OFF'
    pico_led.off()
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
            while count <= step_number:
                count += 1
                for step in full_step_sequence:
                    for i in range(len(pins)):
                        pins[i].value(step[i])
                        pins2[i].value(step[i])
                        sleep(0.0015)

        elif data < 30:
            while count <= step_number:
                count += 1
                for step in full_step_sequence_b:
                    for i in range(len(pins)):
                        pins[i].value(step[i])
                        pins2[i].value(step[i])
                        sleep(0.0015)

        elif data < 40:
            while count <= step_number:
                count += 1
                for step in full_step_sequence:
                    for i in range(len(pins)):
                        pins[i].value(step[i])
                        pins2[i].value([0, 0, 0, 0])
                        sleep(0.0015)

        elif data < 50:
            while count <= step_number:
                count += 1
                for step in full_step_sequence:
                    for i in range(len(pins)):
                        pins[i].value([0, 0, 0, 0])
                        pins2[i].value(step[i])
                        sleep(0.0015)

        else:
            continue

if __name__ == "__main__":
    robot_id = 11
    ssid = 'Abdulkadir'  # 'mechalab_intra'
    password = 'ujbj3761'  # 'mechastudent'

    # Define I2C pins
    i2c = machine.I2C(0, scl=machine.Pin(5), sda=machine.Pin(4))

    # Define pins
    # Set up LED on GPIO 25
    pico_led = Pin("LED", Pin.OUT)
    # Set up neopixel on GPIO 15 with 4 LEDs
    pixels = neopixel.NeoPixel(Pin(0), 4)

    percent = 0
    max_percent = 55200
    min_percent = 20000  # 48500
    charging_status_pin = Pin(27, Pin.IN)
    battery_voltage_pin = ADC(28)

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
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]
    full_step_sequence_b = [
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0],
    ]

    try:
        set_neopixel_color("all", 255, 0, 0) # Red
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        transmitter_ip = '192.168.227.91'
        ip = connect()
        if ip == None:
            set_neopixel_color("all", 255, 0, 0) # Red
            print("Could not connect to WiFi")
            sleep(1)
            set_neopixel_color("all", 0, 0, 0) # Off
            machine.reset()
        set_neopixel_color("all", 0, 0, 255) # Blue
        sock = open_socket(ip)
        _thread.start_new_thread(oled, ())
        set_neopixel_color("all", 0, 255, 0) # Green
        serve(sock)
    except KeyboardInterrupt:
        set_neopixel_color("all", 0, 0, 0) # Off
        sock.close()
        machine.reset()
