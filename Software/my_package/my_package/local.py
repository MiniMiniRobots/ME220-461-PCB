import socket
from time import sleep


if __name__ == "__main__":
    # set the IP address and port number of the Raspberry Pi Pico
    ip_address = '192.168.48.92'
    port = 8000

    # create a TCP/IP socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the Raspberry Pi Pico
    sock.connect((ip_address, port))

    count = 1
    while True:
        if count:
            command = "s"
            sock.sendall(command.encode())
            response = sock.recv(1024).decode().strip()
            print('Response:', response)
            
    # close the socket
    sock.close()
