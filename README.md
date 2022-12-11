# WaterMonitor
MicroPython code for a microcontroller (Raspberry Pi Pico) based water monitoring solution using simple moisture detection via analog circuitry which interfaces as a digital inputs to the microcontroller (3.3V / 5V)

# Aim
Come up with a monitoring solution for low moisture levels to aid in knowing when to water in different seasons without the need to manually inspect each plant.

# Target
Sensors will be attached to 9 hanging plants in the garage which are exposed to a wide range of environmental conditions.  These include:
- Wide range of humidity due to “outdoor” nature of location and a continually running dehumidifier
- Potentially lots of evaporation as each pot uses a coconut hanger which provides a lot of surface area with which to lose moisture.
- Varying pot sizes so each plant should be monitored independently
- Covers a fairly significant expanse (9m) 

# Design
| Schematics |
| ---------- |
| ![alt text](https://github.com/Silverune/WaterMonitor/blob/main/diagrams/RDJ001.png "RDJ Water Sensor x2") |
| ![alt text](https://github.com/Silverune/WaterMonitor/blob/main/diagrams/DSEFP3.png "DSFEP3 Water Sensor") |

# Status Quo

## Existing Approach
Using a cheap water sensor (analog) that is able to show moisture on a scale of 1-10 (broadly) but is effectively uses as a binary (“Needs Water” / “Fine”) with these values being the same for all current plants (<3 “red” needs water, otherwise fine).

### Downside of Existing Approach
- Requires manually inspecting each plant
- Information is transient and not recorded for later pattern analysis
- Can be destructive to the plant as can cause root damage
- Non-scalable
- Time consuming
- Pull technology - probs only noticed when inspected rather than Push
- Only provides moisture only - no scope for temperature (tho this is currently not a requirement)

### Solutions

## Gold Plated
TODO

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
Based on the DSFE Volume 1 Project 3 (DS1-3) 

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

