# MiniMiniRobots PCB Design

The Circuit Board used in the project is made so that the built robot can be actuated with both Stepper and/or DC motors. The Board also have connectors required to connect OLED screen, Neopixel LED's etc. 

The Project is designed so that the system can be powered using 2S Li-ion batteries. To charge these batteries with balance, external 2S Battery Management System (BMS) circuit can be used and can be connected to designed board using "BMS" socket on it.

PCB design is created on EasyEDA. The complete schematic and layout files for both Altium Designer and EasyEDA are located on their subsequent folders. You can also find PDF file for the schematics.

If you want to direct order the PCB without making any changes, you can use the Gerber files.

## Components on the PCB

The circuit requires these components to be soldered on their locations on the PCB in order to be function.
- 2 x 20kΩ Resistors
- 2 x 10kΩ Resistors
- 2 x Capacitors
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

## Designed Board Pictures

![Top of the Board](/PCB/Images/Top_Side.png "Top Side")
![Bottom of the Board](/PCB/Images/Bottom_Side.png "Bottom Side")
![3D View of the PCB](/PCB/Images/3D.png "3D View")
