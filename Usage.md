# Usage of the Circuits

## Usage of The Main Circuit

The Main circuit can operate with Raspberry Pi Pico (or Pico W) and all of the elements except the motors (both DC and Stepper Motors) with USB Power coming from the Pico when connected to a computer or a power adapter. But one needs to be careful while using the circuit with Pico's power input since too much current can be drained from it and the computer USB ports can be damaged (or even the computer motherboard can be damaged). 

For connecting Raspberry Pi Pico and the motor drivers, 2.54mm 6 / 20 pin female headers should be soldered on the circuit first. 

Power port, On/Off Dip Switch and the voltage regulator are needed when the circuit needs to be powered on with an external voltage higher than 5V. Noting that external power source is needed for driving both the DC and stepper motors.

BMS port and R1-R2 resistors are optional and can be used for voltage measurement with Pico when needed. 

R3 and R4 resistors are optional and can be used for voltage measurement coming from Power port.

For driving DC motors, one needs to connect an external power source, L293D motor driver and motors to the circuit.

For driving stepper motors, one needs to connect an external power source, 1 (or 2 for 2 stepper motor driving) ULN2003A stepper motor driver/s and motors to the circuit.

For using strip LEDs, one needs to connect LEDs via NeoPixel port. Here, one needs to be careful about the power need of the LEDs since without an external power source and only power coming from a computers USB port, computer motherboard or the USB port connected can be damaged. 

For connecting the Transfer Circuit, one needs to solder a 1x20 2.54mm female header to the port next to the Pico.

## Usage of The Transfer Circuit

For using the transfer circuit, one needs to solder 2 1x20 2.54mm male headers to their adjacent ports. Advising soldering the headers such that the `Middle East Technical University` text stays on the top such that one can read the name of the pins while using the circuits.

LED and 220R resistor can be soldered for seeing the power connection to the transfer circuit. 

Noting that due to the small design error of the transfer circuit, the transfer circuit is connected with 180degrees rotated to the main circuit.
