# MiniMiniRobots

MiniMiniRobots is a small robot project with custom made mechanical parts and a PCB. It is made in Spring Semester of 2023 as a part of ME462 - Mechatronics Design course in Middle East Technical University, Turkey. The collaborators for this Project are Emir Bahadir Unsal, Mert Kerem Ulku, Yusuf Onat Yilmaz, Musa Doruk Ucar, Abdulkadir Saritepe and Burak Arslan. The project is under MIT License. 

The whole project can be considered under several sub-parts.

## Electronics

The project is built on a custom-made PCB circuit and several small circuit boards. A Breadboard is attached on the robot so that additional electronics can be added. 

### PCB Design

PCB design files and their details can be found under "PCB" folder. The left part of the PCB has 1x20 female headers that is not used by default. With these extra headers, additional circuitry can be connected to it.

### Powering

The system can be powered using 2S battery. For charging the batteries with balance, a Battery Management System circuit is suggested. The BMS can be connected to the PCB board and this connection can be used to detect charging. 

## Mechanical Design

Mechanical parts and the assembly file can be found under "Mechanical Design" folder. All of the parts can be manufactured using a 3D Printer. Top part of the design can be used for putting Breadboard or any other circuit boards. Back part can be used for charging with the Charging Station.

## Charging Station

The "Charging Station" part is used for Wireless Charging Station stage. It can be used coated with aluminum foil with attached on a ground coated with aluminum foil. 
For the station to be powered, 8.4V voltage is required for robots with 2S battery. To achieve this voltage, an adjustable power supply or a fixed ac-dc power supply with a voltage regulator can be used. 
