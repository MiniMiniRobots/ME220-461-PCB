## Python File on Pico - web_server.py

The program consists of several functions and a main function. In `main` function, Pico configures itself for battery voltage reading, defines steps for stepper motors and calls required functions for socket connections in a try-catch phrase. 

`oled()` function is used for displaying the charging status and/or battery percent on the OLED screen. OLED pins should be declared on the main function for properly functioning. 

`connect()` function is used for making Wi-Fi connection. `ssid` and `password` variables should be changed in main function in order to connect to the wanted network.

`open_socket()`  function is used for connecting to the socket server on the PC, which should be on the same network with Pico.

`set_led_color()` function can be used for adjusting the colors for the neopixel led strip connected to the PCB. 

`clear_led()` function can be used for turning off the neopixel.

`draw()` function can be used for drawing shapes on the OLED screen connected to the PCB.

`serve(sock)` function does the required communication with PC to be able to move with respect to the commands came from PC.
