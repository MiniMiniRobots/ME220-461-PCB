# PCB Design for ME220 and ME461 Courses

The repository is created for the PCB circuits used in ME220 and ME461 lectures which are offered in Middle East Technical University in Turkey in Fall 2023 term. The main circuit is firstly made for the MiniMiniRobots project, which this repository is forked from.

The main circuit board is made so that this PCB can be used for controlling both Stepper and/or DC motors. The board also have connectorys required to connect OLED screen, Neopixel LED's etc.

The main board is designed for using 5V as main supply but it has Step-down Voltage Regulator so that it can be powered with higher voltages between 5-35V. The board can also be supplied with batteries, which was a requirement for the MiniMiniRobots project, thus it has BMS socket on it.

PCB designs are created on EasyEDA. The complete schematic and layout files for both Altium Designer and EasyEDA are located on their subsequent folders. You can also find PDF file for the schematics.

If you want to direct order the PCB without making any changes, you can use the Gerber files.

## Components on the PCB

### The Main Circuit
The main circuit requires these components to be soldered on their locations on the PCB in order to be function.
- 2 x 20kΩ Resistors
- 2 x 10kΩ Resistors
- 2 x 16V 10µF Capacitors 
- LM2596 Step-down Voltage Regulator (should be adjusted so that output should be 5V)
- 2-pin Dip Switch
- 4 x 2-pin JST XH2.54 female connectors
- 1 x 3-pin JST XH2.54 female connectors
- 2 x 5-pin JST XH2.54 female connectors
- 1 x L239D Motor Driver Integrated Circuit
- 2 x ULN2003A Stepper Motor Driver Integrated Circuit
- 1 x 2 pin Push Button
- 3 x 1x20 Female Header (2.54mm)
- 1 x Raspberry Pi Pico W

### The Tranfer Circuit
The transfer circuit only requires these components to be soldered on their locations on it in order to be function.
- 2 x 1x20 Female Header (2.54mm)
- 1 x 5mm LED
- 1 x 220Ω Resistor

## Designed Board Pictures

### The Main Circuit
![Top of the Main Board](/Images/Top_Side.png "Top Side")
![Bottom of the Main Board](/Images/Bottom_Side.png "Bottom Side")
![3D View of the Main PCB](/Images/3D.png "3D View")

## The Transfer Circuit
![Bottom of the Transfer Board](/Images/Bottom_Side_Transfer.png "Bottom Side")
![3D View of the Transfer PCB](/Images/3D_Transfer.png "3D View")

