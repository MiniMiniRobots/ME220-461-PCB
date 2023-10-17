# PCB Design for ME220 and ME461 Courses

The repository is created for the PCB circuits used in ME220 and ME461 lectures which are offered in Middle East Technical University in Turkey in Fall 2023 term. The main circuit is firstly made for the MiniMiniRobots project, which this repository is forked from.

The main circuit board is made so that this PCB can be used for controlling both Stepper and/or DC motors. The board also have connectorys required to connect OLED screen, Neopixel LED's etc.

The main board is designed for using 5V as main supply but it has Step-down Voltage Regulator so that it can be powered with higher voltages between 5-35V. The board can also be supplied with batteries, which was a requirement for the MiniMiniRobots project, thus it has BMS socket on it.

PCB designs are created on EasyEDA. The complete schematic and layout files for both Altium Designer and EasyEDA are located on their subsequent folders. You can also find PDF file for the schematics.

If you want to direct order the PCB without making any changes, you can use the Gerber files.

## Components on the PCB

### The Main Circuit
The main circuit requires these components to be soldered on their locations on the PCB in order to be function.

| Type of the Component | Details | Notes  |
|-----------------------|-----------------------|---------------|
| Resistors     | Depends on the Connected Devices | Read [Usage](/Usage.md) file for finding the required resistances |
| Capacitors      | 2 x 16V 10µF  | Needs to be Electrolytic (cylindrical) to fit their locations on the PCB  |
| Voltage Regulator | LM2596 Step-Down  | There is 2 regulator with different dimensions, its dimensions should be 43x21x14 $mm^3$ to fit to PCB  |
| JST XH2.54 Male Connectors | 4 x 2-Pin, 1 x 3-Pin, 2 x 5-Pin  | Male Connectors should be soldered to PCB |
| DC Motor Driver | L293D DIP-16 Driver | Do not forget to solder 2 x 6-Pin female 2.54mm headers first|
| Stepper Motor Driver | ULN2003A DIP-16 Driver | The driver which comes with the  28BYJ-48 Stepper Motor Set can be used on the circuit |
| Push Button | 2-pin Tact Button  | Can be used to reset the Pico without disconnecting the power source |
| Dip Switch | 2 Pin Dip Switch | Both of the should be on to pass the power |
| Female Headers | 3 x 1x20, 6 x 1x6 2.54mm | 1x20 female headers can be broken to obtain 1x6 headers |
| Microcontroller Circuit | Rasppberry Pi Pico W | Raspberry Pi Pico can also be used with this circuit but in ME220 and ME461, Pico W is used |


### The Transfer Circuit
The transfer circuit only requires these components to be soldered on their locations on it in order to be function.

| Type of the Component | Details | Notes  |
|-----------------------|-----------------------|---------------|
| Female Header     | 2 x 1x20 2.54mm | Advising soldering the headers such that the `Middle East Technical University` text stays on the top such that one can read the name of the pins while using the circuits. |
| LED      | 1 x 5mm  | Shows if the transfer circuit is powered or not  |
| Resistor | 1 x 220Ω  | Needed for lowering the current passing on the power LED 

While preparing the circuits for usage, please refer [Usage of the Circuits](/Usage.md).

For more detailed explanation for each component on the circuits, one can refer to [Explanation of the Components](/Explanation.md).

## Designed Board Pictures

### The Main Circuit
![Top of the Main Board](/Images/Top_Side.png "Top Side")
![Bottom of the Main Board](/Images/Bottom_Side.png "Bottom Side")
![3D View of the Main PCB](/Images/3D.png "3D View")

## The Transfer Circuit
![Bottom of the Transfer Board](/Images/Bottom_Side_Transfer.png "Bottom Side")
![3D View of the Transfer PCB](/Images/3D_Transfer.png "3D View")

