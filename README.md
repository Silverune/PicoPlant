# WaterMonitor
MicroPython code for a microcontroller (Raspberry Pi Pico) based water monitoring solution using simple moisture detection via analog circuitry which interfaces as digital inputs to the microcontroller (3.3V / 5V)

# Aim
Come up with a monitoring solution for low moisture levels to aid in knowing when to water in different seasons without the need to manually inspect each plant.

# Status Quo
Latest update is development nearing completion on the Beta prototype.

## Completed
- Firmware completed
- Power supplied
- Probe connector plate create / installed
- Mounting plate created for controller
- 1x Completed probe
- 9x NPN resistors, capacitors soldiered

## TODO
- Soldering: signal probes, Vcc, GND.
- Create other probes
- Attach dual core wire to each probe
- Cut dual core wire to appropriate length
- Run each dual core wire from plant to probe plate
- Move 5V power to give additional space for mounting offset
- Reconnect power supply
- Connect mounting plate
- Connect mounting plate to wall
- Connect the probe and controller plates together
- Run each probe into the probe plate
- Run each signal from the probe plate into the controller

# Primary Target
The initial installation will be to the 9 hanging plants in the garage area.  These are exposed to a wide range of environmental conditions, including:
- Wide range in humidity due to “outdoor” nature of location and a continually running dehumidifier
- Wide range in temperature due to limited insulation in garage and lack of air-conditioning.  Plants are also located physically in an elevated location near the apex of the structure.
- Potentially lots of evaporation loss as each pot uses a coconut hanger which provides a lot of surface area with which to lose moisture.
- Varying pot sizes so each plant should be monitored independently.
- Varying planting so each plant may have its own moisture consumption profile.
- Covers a fairly significant expanse (9m) 

# Software Design
Firmmware is written in MicroPython 3 running on a Raspberry Pi Pico.  Minor pin changes would likely be required to shift to other RPI (or compatible) hardware with minimal software changes required.  Broadly this code falls into the following main categories:
- Controller - "main" which sets up the hardware and runs the main control loop
- Device Drivers - custom drivers created for the water sensor probe (bespoke) as well as the 16x2 LCD display and temperature sensor
- Misc - minor utility routines including custom fonts for visual representation of the water level.

# Hardware Design
The hardware consists of the following main areas:
- Microcontroller - Raspberry Pi Pico
- 16x2 backlit LCD - 4 input display (8 available but only 4 required [D4-D7])
- Potentiometer - provides contrast for the LCD to deal with varying light conditions
- 63 row protoboard (solderable breadboard) - houses the water sensor analog logic
- Dual core wire: 40m approx - connects sensor probes (in plant) to the probe board
- 2x 20pin female connectors for connecting the controller board to the probe board
- 5V DC 2A fixed 2.1mm tip plugpack
- DC barrel power jack / connector
- 9x Each of the following:
  - NPN transitions (2N2222 / S8050 effectively identical for this application) - NW / FN switch
  - 330 Ohm resistors - controls the NW threshold
  - Metal probe set (2x)
  - Lever nut splicing connectors (2x)
  - Probe to controller connecting wire (2x)

# Design
| Schematics |
| ---------- |
| ![alt text](https://github.com/Silverune/WaterMonitor/blob/main/diagrams/RDJ001.png "RDJ Water Sensor x2") |
| ![alt text](https://github.com/Silverune/WaterMonitor/blob/main/diagrams/DSEFP3.png "DSFEP3 Water Sensor") |


## Existing Approach
Using a cheap water sensor (analog) that is able to show moisture on a scale of 1-10 (broadly) but is effectively uses as a binary (“Needs Water” [NW]/ “Fine” [FN]) with these values being the same for all current plants (<3 “red” needs water, otherwise fine).

### Downside of Existing Approach
- Requires manually inspecting each plant
- Information is transient and not recorded for later pattern analysis
- Can be destructive to the plant as can cause root damage
- Non-scalable
- Time consuming
- Pull technology - probs only noticed when inspected rather than "pushed"
- Provides moisture only - no scope for temperature (tho this is currently not a requirement)

# Prototypes

## Prototype 1 - Use a microcontroller with OTS Sensor
First test was to use a uC to test the ability of monitoring the sensor.  Tested on Raspberry Pi Pico but used an Arduino compatible sensor (Elegoo).   Prototype expanded to test other TTL style sensors.

### Advantages
- Single unit
- Many digital inputs 
- ight be cheaper
- Complete control over all aspects
- Should be easy to deal with corrosion on the leads as they are independent of the design

### Disadvantages
- Only 3 usable ADC pins
- Expensive / sensor.  Ranging from: $2 (non-capacitive) up to $8 (capacitive in bulk)
- Sensors appear to all have a corrosion problem, even when left unpowered.
- Not all the sensors provide a digital input.
- Requires up to 3 wires to be run / sensor to the location
- Sensors are small and may not penetrate very far 

## Prototype 2 - Implement Purely in Analog
Based on the DSFE Volume 1 Project 3 (DS1-3) then modified to bring the logical / power levels into the acceptable range for both NW and FN.

### Advantages
- Simple to debug
- Might be cheaper
- Complete control over all aspects
- Should be easy to deal with corrosion on the leads as they are independent of the design

### Disadvantages
- Might be more expensive
- Calibration might be quite complicated especially if not using potentiometers for the resistence.  Eventually the signal will need to be treated as a digital input so the resistor values need to be picked so that NW triggers either a low / high and FN triggers the opposite.   Mainly due to the limited number of analog inputs on the microcontrollers.

# Alpha
After testing decision has been made to construct a simple breadboard implementation using my simple analog circuit feeding the output as a digital signal into a Raspberry Pi Pico.  

## Components
- Micropython control code
 - LCD GUI to show results / inputs from sensors
 - Driver for new analog input
 
- Physical Construction
 - Probes consist of:
   * Two conductive sensors that are able to be placed (long term) into the soil.   Should not corrode or if they corrode easily cleanable / replaceable.
   * Each sensor is able to be run directly to the control board with one sensor connecting to GND while the other is the input.
 - Mounting of microcontroller to location which is physically close enough to the sensors
 - Power supplied by 5V not 3.3V.   While the pico runs at 3.3V the LCD screen requires 5V for correct operation.   Also as using an external power supply on the VSYS line cannot use the VBUS power previously (no USB power attached).

### Probe construction
The probes are made from a simple tent peg that has been bent into a straight shape making a long spike with a robust physical point able to push into hard soil.   Attached at one end is an Male Slide Connector which is slightly crimped and then soldered.   Though the hole is then soldered some AWG 22 single core wire which is then run to the required distance and inserted into the breadboard.

### TODO
- Investigate cost of components
- How much does the length of the wire (sensor) affect the resistance

# Miscellaneous
- The non-powered working sensor has the following characteristics:
    - 1k ohm resistance
    - Water as reference: 0.33V passes through
    - 2.5 with 1M ohm scale 3

# Terminology
The following terminology is being used:

- NW - Needs Water - moisture level considered below some threshold,   This will be different for analog to digital but in either case means the same thing.
- FN - Fine - moisture level considered above some threshold,   This will be different for analog to digital but in either case means the same thing.

# Links
- 16x2 LCD uP driver https://github.com/dhylands/python_lcd/blob/master/lcd/pyb_gpio_lcd_test.py
- Raspberry Pi Pico specs https://dronebotworkshop.com/pi-pico/
- EveryCircuit https://everycircuit.com/circuit/4978760010694656

