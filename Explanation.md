# Explanation of the Components on the Circuits

## Main Circuit

| Component Name on PCB | Type of the Component | What It Does  |
|-----------------------|-----------------------|---------------|
| BMS     | 2 Pin JST XH2.54 Male Connector | Connects BMS device to PCB |
| On-Off      | 2 Pin Dip Switch      | Manually Controls Main Power |
| Power | 2 Pin JST XH2.54 Male Connector      |    Connects Main Power Supply to PCB |
| DC Motor | 2 Pin JST XH2.54 Male Connector       | Connects a DC Motor to PCB |
| Step Motor | 5 Pin JST XH2.54 Male Connector       | Connects a Stepper Motor to PCB|
| Reset | 2 Pin Tact Switch      | Resets Pico  |
| R1 | Resistor      | Divides BMS Voltage for Battery Level Measurement |
| R2 | Resistor      | Divides BMS Voltage for Battery Level Measurement |
| R3 | Resistor      | Divides Power Voltage for Power Level Measurement |
| R4 | Resistor      | Divides Power Voltage for Power Level Measurement |
| LM2596 | Step-Down Voltage Regulator      | Regulates Power to 5V for Pico and other Components which needs 5V |
| ULN2003A | DIP-16 Stepper Motor Driver      | Controls 1 stepper motor connected to the circuit with the signals coming from Pico  |
| L293D | DIP-16 DC Motor Driver      | Controls 2 DC motor connected to the circuit with the signals coming from Pico |
| C1 | Electrolytic Capacitor      | Smoothens Power Input for safer use |
| C2 | Electrolytic Capacitor      | Smoothens Power Input for safer use |
| Raspberry Pi Pico W | Microcontroller Board | Microcontroller Board which controls the whole circuit |
| NeoPixel | 3 Pin JST XH2.54 Male Connector     | Connects LED Strip to the circuit |

For the schematic of the Main Circuit, [Main Circuit Schematic](/Schematic_MiniMiniRobots.pdf)

## Transfer Circuit

| Component Name on PCB | Type of the Component | What It Does  |
|-----------------------|-----------------------|---------------|
| PICO | 1x20 2.54mm Male Header  | Connects the Main Circuit to the Transfer Circuit |
| OTHER      | 1x20 2.54mm Male Header | Connects the Transfer Circuit to other circuits or a breadboard |
| 220R | 220Ω Resistor  | Decreases the Current for the LED to function |
| LED | 5mm LED  | Shows the Connected Signal |

For the schematic of the Main Circuit, [Transfer Circuit Schematic](/Schematic_ME220-461-PCB.pdf)
