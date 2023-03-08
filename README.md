# MICROCONTROLLER MOISTURE MONITOR (MMM)

## Introduction
This project develops a low cost microcontroller controlled moisture monitoring solution that can be applied to a variety of moisture detection requirements.  All components used are listed and are low-cost.  The entire project should cost similar to the price of a commercial single moisture probe with plenty of scope for future enhancement.  Some knowledge of interfacing the microcontroller and ability to solder is required.

## Key Elements
The following are the primary elements required:

Microcontroller - the device connecting everything together.  Controls the display and receives input from the sensors
Firmware - control software for the microcontroller which is able to use the inputs and output to the display
Display - visual interface to show the current status of the sensors
Sensors - input sensors providing the moisture information

Each of these elements can be interchanged and the project itself will still achieve it’s purpose.  For this specific implementation I have used:

### Microcontroller - Raspberry Pi Pico W
https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html ($9.90 AUD-$15.05AUD (with soldered headers) https://core-electronics.com.au/raspberry-pi-pico-w-with-soldered-male-headers.html).   This low-cost microcontroller is able to completely suit the requirements for the project with enough general purpose input output (GPIO) pins to satisfy all the current requirements.  It can also provide 5V and 3.3V for external peripherals (display) and if desired can be network connected (“W”).  Networking of the display results is not covered in this documentation as that is outside the scope of the project and is common to all Raspberry Pi Pico W projects

### Firmware - MicroPython3 / Custom (this repo)
This can be broken into two main areas:
1. Operating system - using MicroPython3.  This has a number of advantages and the processing requirements of the project are minimal.  Rapid development and ability to run a serial monitor for debugging makes this a suitable choice.
2. Application software - this is custom built for the project (supplied in this repository).  It consists of the following main elements: a. device driver for the temperature sensor on the RPIPW b. device driver for the chosen 16x2 display c. device driver for the custom sensor d. custom fonts for use with the display e. device initialisation f. main processing / monitoring loop (“main”)
All the micro python code required is provided on this repository.  If using an alternative sensor than the one in specified (e,g., an off-the-shelf capacitive or resistive sensor I have also provided a couple of device drivers I created for those as well but I did not end up using either of those as they are expensive and offer no advantage in my use-case.

### Display - LCD1602 
https://core-electronics.com.au/iic-lcd1602-gadgeteer-compatible.html ($18.95AUD)  Note: this item is almost always shipped in any Arduino compatible starter kit (e.g., Elegoo kits) so it is recommended to get it as part of a kit if you have even a general interest in electronics. These kits provide excellent value.   This is a common display with a variety of methods of driving the display.  I have opted to not complicate the project with requiring the I2C driver and have instead simply run 4 data lines to it to handle the display.

### Sensors - Voltage Dividers
20K resistor, (per input sensor) .  The solution used for this project involved building 9 custom voltage divider circuits which were fed into the GPIO (digital) pin on the RSPPW analog sensors built around using a voltage divider inputting the 3.3V RPIPW back into the GPIO pins as a digital input.   The actual sensors themselves consisted of wires connected to more robust hardware that could be inserted deep into the soil. 

### Other - Necessary Evils
While not  key elements the following are also required for the project.
1. 5V power supply (the RPIPW requires 3.3V but the display is a 5V device so needs this extra voltage)
2. 2.1mm jack for connecting the power to the board
3. Protoboard for soldering everything together
4. Wire (I used single core) to hook everything up
5. 10K potentiometer for brightness control of the LCD display.
6. 10uF capacitor across the power rails - good practice!   Avoid spikes due to dodgy power supplies and takes out some noise.   Sure you can get away without it by if you have one I definitely think you should clean things up.

### Other - Non-necessary Evils
These are items I ended up using but depending on your installation requirements may not be required.
1. Mounting board
2. Brackets
3. Electrical wire (dual core) to run out to each sensor as I had a long run which made using regular wire cost-prohibitive and messy.
4. A female 20-pin I/C mount for connecting the sensors to
5. Electrical connecting adapters to separate the tent peg wires from connecting directly into the protoboard
6. Tent pegs (2x per sensor) these were connected via wires to the resistors which then form the voltage dividers as inputs to the microcontroller.
7. Heat shrink solder connectors - these made connecting the wires to the tent pegs relatively straight forward as the tent pegs are not easy to simply solder too without using a lot of solder/flux and a substantial soldering iron due to the mass of the pegs.   This provided an easy shortcut.

## Philosophy 
The general idea behind this project was to base it on a real-life requirement I had which was to monitor the moisture levels of 9 different types of plants in a location out of easy reach (required a ladder each time to check moisture levels with a traditional metre).   Additionally, each of these plants was planted in different hanging baskets sizes with different soils types so a sensor on a random plant would not be indicative of all the plants.  Continuous monitoring was not required as no automated watering was connected so there was no need to run power to it until actually interested in the results.  Due to the distances between the plants and where the control unit would be a large amount of wire would be required.  In my case something like 40m of wire was required in total.

The following looks at the design decisions around each of the key elements

### Microcontroller
A minimum cost microcontroller is all that is required for the project.   As long as there are enough input / output ports to hook everything up then pretty much any microcontroller should do.  i chose the RPIPW as it was low-cost, could later be Wifi connected if I decided I also wanted remote monitoring and had great community support.   An Arduino (Uno etc.) would also be a completely suitable solution with only a minor modification to the sensors due to the level change from 3.3V to 5V. 

One consideration that may be not initially obvious is the fact that most microcontrollers have only a limited number of analog inputs while having an abundance of digital inputs.   Most commercial moisture meters like to give analog output, while some will also provide a digital output as well (controlled by a potentiometer on the control board).  For my purpose this was overkill, I simply wanted to know when the plant required watering because the soil moisture had dropped to a level I considered was “time to water” (more on this in the sensor discussion below).   As such, analog inputs are only used in two instances in the entire project: temperature sensing (internal as part of the RPIPW) and for debug as part of the LCD brightness control (optional). 

The firmware using MicroPython3 was purely a choice based on simplicity.   There were more steps involved in getting a C compiler development setup all working with no significant advantage based around speed.   As such, easy to go with MP3 where there were already a number of external support modules already built I could use.  (e..g, LCD display driver).

### Display
As there are only a boolean display required for each of the input sensors (water / non-water) and a single temperature display there was no requirement for a high resolution screen and a simple 16x2 display would suffice.  In fact, even though the display supports I2C it was also considered overkill to bother using it in this manner as the screen was simply showing the sensor status on a single “page”.   I did create a few custom character fonts to make the display look slightly more professional than simply using the default 8-bit ASCII selection.  These were a celsius symbol as well as full and empty water indicators.

### Sensors
This is the most subjective varied part of this project and probably the part most people will be attracted to about this project.   The reasons for this is that there currently doesn’t exist very many reasonably priced robust moisture monitoring components on the market and those that do exist and are reasonable are overkill for a non-continuous monitoring requirement.   I’ll break down in simple terms my views on each and how I came to reaching my decision to simply “reinvent the wheel”.

1. Water Level Sensor Detection Unit (e..g, https://www.amazon.com.au/Sensor-Module-Detection-Surface-Arduino/dp/B01N058HS6)   These units function completely fine in a limited use case.   They still cost roughly $4 in bulk so hooking up a whole greenhouse might start to add up and they cannot have power applied continually or they oxidise and become unusable after a few months.  In most cases they provide an analog output which (as mentioned previously) is not required or desirable. 
2. Capacitive Water Sensor Detection Unit (e.g., https://www.amazon.com.au/Electronic-Capacitive-moisture-Corrosion-Resistant/dp/B08VDD2HRR)  These are seen as superior to the regular detection sensors mainly due to their ability to resist corrosion as they do not have exposed copper wiring.  However, they come at a higher cost (over 3x the cost) and if there is no requirement to be continually powered then this is not an issue.  Additionally, they appear to be difficult to source the better quality units with an ability not to corrode.   They do generally have the advantage that they come with an interface unit allowing you to configure a digital input but this is yet another control board.  For a single sensor probably not an issue but in my use case where I needed 9x this would have unacceptable.
3. Traditional analog design.  There are no off-the-shelf versions of this that are suitable for adding to the project though it is trivial to build one.  Many of the older electronics kits like the Radio Shack / Dick Smith home hobbyist solutions involve a simple LN2022 style NPN (PNP in Radio Shack’s case) transistor amplifying a weak signal through the signal and lighting up an LED to indicate water level or continuity.  Strangely, even though these are simple solutions they are still over-engineered for what we need.   It would mean each sensor requires a transistor and one (or two) resistors.  Not a huge cost but also not required.  Completely suitable as an educational aid but that’s not why we are looking at these designs.
4. Voltage divider coupling!  This is the “design” I have gone with.   To explain why this is the design a little dive into the problem:
    1. We have a number of knowns that other solutions don’t - let’s use that to our advantage. The main one being that we are trying to turn an analog value into a digital one.   That’s a whole rabbit hole in itself but in our case it boils down to simply matching the resistance in the sensors when there is enough moisture between the probes with the positive signal the microcontroller accepts.   To break down each:
    
1. Resistance in the sensor - there are many ways to look at this problem.   The two off-the-shelf solutions look at the change in voltage (resistance) or impedance? (capacitive). In either case the conductivity in the circuit changes the transducer to report a different value.   I took the approach of looking at resistance changes caused by moisture changes.    Simply put, pure water doesn’t even conduct electricity, its the impurities in water that allow current to pass.  However, soil happens to have a lot of impurities so you will often get a surprisingly strong reading in what we would think of as mostly dry compared to dropping a sensor in a cup of water (which again is not as conductive as you would think).     So the approach is simply to use an external reference to work out what is considered “dry” or “needs water” (on my simple scope its anything 3 or below on a scale of 1-10).  When the reading is at that level, use a multimeter to measure the resistance in our sensors in the soil and note that as a reference point.   Despite a wide range of soils I found values in the 20k to 50k ohm to be the sweet spot.  Once dry the resistance quickly shoots up into the mega ohm range.   This resistance is important in the next step.

2. As our microcontroller has a very limited number of analog inputs (and we don’t need them anyway) we need to convert the sensor reading to an on or off value for the software.   This is where a data-sheet can come in handy but these are still a guide.   You can simply test your microcontroller will a potentiometer and work out what it finds is a logical on and off and how that maps to the analog voltage.  To use a specific example of the RPIPIW the data-sheet lists the logical “high” as 1.6V (it’s a 3.3V device so essentially half the voltage) all the way up to 3.3V.  There is an undefined dead zone that any values below 0.8V count as “low” and if you had a short-circuit it would read the source voltage of 3,3V   This is important information for the design - we need to match the minimum high to the threshold maximum resistance that we want to trigger on.   e.g., if we found that 20k ohm resistance led to us deciding that the plant has finally needed water then we map this 20k ohm to a voltage that will at minimum remain high.  Once the resistance goes beyond this we are dropping into the undefined / low state which is when we need to water the plant.   The solution, a voltage divider.   We simply couple the input sensor to the input resistance that we deem too low and everything falls into place.  If the sensors in the soil are just watered and the conductivity is high at most it can only ever be 3.3V (the supply voltage) but if it resists above our value the voltage on the GPIO pin drops below 1.6V and the sensor should read low (in reality once in the undefined state it flickers around which is actually desired as it shows that this reading is on the threshold - a non-binary reading on a binary sensor!).  So if wet enough the GPIO reads high and once beyond what we consider acceptable it reads low - perfect!

3. Super cheap - the design is two wires and a resistor.  It’s almost impossible to make a cheaper unit.   No matter how many sensors you add there is simply no way to compete with this.  On the protoboard it can be simplified to take up as little as 2 rows!
 
 4. Diagnosis is fast and simple.   At all points the circuit can be examined to ensure correct functionality.  There are no IC’s to deal with or interface boards.

In summary, the solution involves a simple cheap off-the shelf microcontroller that is well supported both by the organisation / community.  The language used has low barriers to entry and there exists many third-party libraries making this a fairly safe choice if you get yourself into trouble.   The display is nothing to write home about but completely functional for the job and very low cost - especially if you get one in a bundle.  For simple usage this will be more than enough.   The sensors themselves are the cheapest part of this whole project which is important as this is the part you may have the most of!   The design is simple and dirt cheap.   When you can have faith a 50c sensor will do the job of a $12 off-the-shelf unit (while not taking up an analog input) then this is really where this design comes into it’s own.   Simply add as many units as you like - it’s only the effort of wiring things up that becomes the issue not in any way the cost.  As long as your microcontroller has spare GPIO pins then you can simply keep adding more.

## Build

### Parts List
For completeness I will list all the parts used for my build.   Understandably, less parts could be used (not including “Other - Non-necessary Evils”) but if you are not interested in my particular installation simply ignore these items.   It is better to have a complete reference than to leave these out.

The list will be broken into the software and hardware side of things.

### Software
- MicroPython3 installation.
- Download all the files from this repo and copy them over to the device.  I would recommend renaming the “main.py” file to something else to start with as this will be the file that get automatically booted each time the device is reset so if you have problems you are advised to run this from the interpreter (e..g, Thonny) in case there are problems that hang your microcontroller each time.  When finally happy with the firmware you will put the “main.py” file onto the device for the final installation. If you don’t require any of the other sensor types (I didn’t) then you can leave off the “capacitive.py” (if not using Capacitive sensors) and “hw080.py” (if not using regular off-the-shelf resistive sensors.  All other files are required.

### Hardware
This can be broken down into a few sections:

Electronics components
- Raspberry Pi Pico (W optional)
- 10k Ohm potentiometer
- 9x 20k Ohm resistors (1 / sensor)
- LCD1602 compatible display
- 2.1mm power adapter (positive inner core)
- 5V DC power supply
- 10 uF capacitor

Physical Hardware
- Protoboard large enough to solder all the components. I used a MakerVerse which I found worked perfectly
- 20x1 female IC socket
- AWG 22 single core wire
- 40m insulated 2 core wire (this is very installation dependant - my installation required a lot of wire due to the location.  Most implementers are likely to not require this amount).
- 18x tent pegs (2 / sensor)
- 18x solder seal wire connectors (heat shrink solder connectors)
- 9x Electrical contact connectors
- Wooden board (larger than your protoboard)
- Screws to bolt protoboard to installation board
- Offsets for each screw (my particular installation used both side of the protoboard so needed to have the board offset in the final installation location
- Cable ties (I required the final installation vertically mounted on a metal strut so these were used.)

There will also be a number of assumed tools that you have to work on all this.  Soldering iron, wire stripper, digital multimeter, computer etc.   It is beyond the scope of this blog to deal with these topics.

## Design
The following is the broad design of the entire project.  Broken down into it’s simplest components:

TODO: power -> protoboard -> sensors -> plants

The main electronics work is on the protoboard.  This is the design.

![alt text](https://github.com/Silverune/MMM/blob/main/diagrams/circuit.png "Circuit Design")

Each sensor consists of the following simple voltage divider circuit.

![alt text](https://github.com/Silverune/MMM/blob/main/diagrams/voltage_divider_circuit.png "Voltage Divider Circuit") 

Which is simulated here and can be interacted with:

[Voltage Divider Simulation Circuit](https://everycircuit.com/circuit/4709676088033280](https://everycircuit.com/circuit/4709676088033280) 

This fundamentally boils down to the following equivalant circuit:

![alt text](https://github.com/Silverune/MMM/blob/main/diagrams/voltage_divider_b.png "Voltage Divider Equivalant Circuit") 

Which in practicality looks like this with the two sensors going into the pot to have the moisture measured

![alt text](https://github.com/Silverune/MMM/blob/main/diagrams/voltage_divider_a.png "Voltage Divider Practical")

The linked simulation can be used to prototype differing resistance selections.  The “V” in the simulation maps directly to the GPIO input of the microcontroller.   As can be seen by varying the potentiometer (which simulates the differing dryness levels on a scale of 1 to 10) this brings the voltage into a logical “high” state when above a value of 3 which equates to around 1.8V on the GPIO input.   Short circuit (10) yields 3.3V which is still safe as the GPIO input.   Anything dryer / lower (<3) than this is a  logical “low” (< 1.8V) and triggers the false boolean state on the input.  The undefined area between 1.8v and 0.8v will generally trigger an intermittent transient state which shows up on the LCD as a flickering ON/OFF state for that sensor.

If requiring finer precision in the on / off state the resistor can be changed to something lower (e.g., 10k ohm) which will make the sensor more sensitive.   An alternative is to instead install a potentiometer (100k) which can be used to perfectly tweak the dry/non-dry setting for your particular scenario.   This was over-kill for my requirements but would work without a lot of modification (quite a bit more cost / soldering though).

The resistance in the wire used for the sensors can generally be ignored.   Over a typical length and the fact that the voltage divider is using quite a sizeable resistance this does not play a significant role in the design.  Typical wire resistance might be in the 8-10 ohm range while the resistors being used are 20k ohm so this constitutes 0.05% difference.

Traditional water sensors work by having different materials in the probe and the conductivity in the water create a battery which is passed across a 1k ohm resistor then fed to the analog display.  This solution uses a larger resistance but from two separate probes and then measures the voltage drop when the 3.3v input source is applied.   The voltage divider resistor on the board regulates what the voltage drop is in relation to the GPIO input.

To construct the sensors the following process was used.

1. Bend the tent peg into a straight shape.   The tent peg is a suitable choice due to its robust nature and ability to push deep into the soil with no issues.  However, the hook that most tent pegs have is not required unless the probe is used in a hanging basket and even then I found I still wanted to run the wires up to the top of the structure for easier channeling to the controller unit.  To bend the tent peg use either a pair of pliers (easy) or a bench vice (cleaner / better result).
2. Cut some wire that is easily able to span the distance from the plant to the controller.   This is where I used electrician’s wire as a single cable was able to hold two inner wires isolated and came in long roles (mine was a 100m in length!).
3. Strip the wires and put each into a solder seal wire connector.  Use a heat gun to seal the tent peg to the wire (x2) 
Congratulations - you have your first sensor.   Now do this again for however many you require - 9 in my case!

Firmware

This is not designed to be an exhaustive line by line talk-through of the micro Python code.  It is designed to give an oversight of what is being done, how it is being done and any non-obvious sections of the code that might be helped by additional explanation.

Files:

- main.py - this is the "main" where the micro Python starts executing the code.  All other files are referenced from this one.
- rdj001.py - device interface for the voltage divider circuit.  Essentially, is a simple wrapper around assigning one of the GPIO pins to act as a digital input.
- pico_temp.py - the Raspberry Pi Pico has a built in temperature sensor.  This file has routines for reading this value and processing the results
- lcd_api.py - API class for sending information for display to the LCD
- gpio_lcd.py - top-level class for interfacing to the LCD.  This is the class used by main.py.  It uses lcd_api.py as part of its implementation
- common.py - utility routines and constants used by the firmware

Additionally, optional files provided are:

- hw080.py - device interface if using a traditional off-the-shelf water sensor
- capacitive.py - device interface if using one of the newer capacitive off-the-shelf water sensors

As mentioned previously, the provided implementation uses only the voltage divider circuit so the other two device drivers are provided only as an option.

The main.py is the only file that is worth looking at in any detail.  All the others can be considered "black boxes" which do their job without needing to understand how they are doing it.

Broadly, most microcontroller code is always broken down into the following sections:

1. Initialization
2. Looping over the input / output

Initialization

This can be broken into the following:

Inputs - data that the microcontroller will process
Outputs - communication to the LCD

Inputs consist of:
a. Temperature sensor (analog-input on-board)
b. Sensor inputs for the moisture probes (digital GPIO x9)
c. Contrast potentiometer value for debugging (analog-input)

Outputs consist of:
a. Digital nybble lines for displaying a character on the LCD (digital GPIO x4)
b. LED control for debugging (digital on-board)
c. LCD Enable (digitial GPIO) to facilitate writing of data to the registers
d. LCD Register Select (digital GPIO) used for controlling where the LCD stores data sent to it

At startup all of these inputs / outputs are configured and the appropriate library classes are passed the desired configuration.   In most cases the GPIO assignments can be switched around to match a different wiring configuration but any of the on-board sensors need to remain untouched as they are not configurable.  These are:

1. Temperature sensor on analog pin 4
2. On-board LED mapped to GPIO pin 25

Neither of these pins appear on the regular pin-out diagram but the software maps to the analog / digital ports just like any other input.

For my particular installation, I wanted to have all the moisture sensors on one side of the microcontroller and leave the other side purely for the LCD.   This was to give a little more space on protoboard to focus on each of these sections in isolation of the other.  So the moisture sensors are mapped to GPIO pins 6-14 while most of the LCD control pins are on the other edge of the micrcontroller GPIO pins 16-21.  There is also an analog input pins configured which shows the output of the LCD contrast potentimometer but this is purely optional and was used during development for display on a serial monitor.

The only other significant initialization before the main loop is creating a number of custom characters for the LCD display as these are not by default supported with the existing libraries I was using.  The characters are:

1. A celsius symbol - the LCD has a temperature display and this makes it appear a little more professional
2. A symbol to show for lack of moisture - "dry"
3. A symbol to show for acceptable moisture - "wet"

These are simply encoded into a sequence of 8 4-bit nybbles (we only are using 4 data lines) which are then handed to the library for use later.   Additionally, we also initialize the LCD library and show an initial screen.   Due to the way the main loop updates the screen the labels for the temperature and water only ever need to be sent to the LCD once at startup.

Next is the main loop.  Here is where the microcontroller spends all of its time performing the same operations until it is switched off.  These are:

1. Read the current state of the contrast potentiometer (optional) before a short wait
2. Read the current state of the temperature sensor before a short wait.

These waits are generally considered best practise when reading from analog inputs, they may not be required but I haven't tested thoroughly without them so have opted to leave them in.

Next comes the reading of all the moisture sensors.  This is simply done in a loop by reading the digital input value currently on each of the configured GPIO pins.   Any reading 3.3V down to rougly 1.8V is read as a "high" while anything below 0.8V is "low".   Anything with the range between these two is undetermined and may appear as either high / low.   In practise this tends to show as flickering between the two states.

Now all values have been read the next job is to act on the data.  This boils down to:

1. Output results via the serial debugging interface (optional)
2. Updating the temperature value on the LCD
3. Converting the high / low values from the moisture monitor sensors to a representation on the LCD (dry/wet).

For the output to the serial interface this is a built-in function for micropython where a simple "print()" outputs the information and can be viewed from within the IDE (Thonny).

The updating of the LCD for temperature moves the logical cursor (though it is not visible) up to the top-line of the display and outputs the most recent temperature value (followed by the custom celsius symbol we defined earlier).

Similarly, each of the moisture sensors is also updated by moving the cursor back to the bottom line and showing either of the custom symbols we defined for each state next to each other.   An example display is as follows:


# Design
| Diagrams |
| ---------- |
| ![alt text](https://github.com/Silverune/MMM/blob/main/diagrams/circuit.png "Circuit Design") |
| ![alt text](https://github.com/Silverune/MMM/blob/main/diagrams/LCD1602.png "LCD1602 16x2 LCD") |
| ![alt text](https://github.com/Silverune/MMM/blob/main/diagrams/raspberry_pi_pico_w_pinout.png "Raspberry Pi Pico W Official") |
| ![alt text](https://github.com/Silverune/MMM/blob/main/diagrams/voltage_divider_a.png "Voltage Divider Practical") |
| ![alt text](https://github.com/Silverune/MMM/blob/main/diagrams/voltage_divider_b.png "Voltage Divider Equivalant Circuit") |
| ![alt text](https://github.com/Silverune/MMM/blob/main/diagrams/vvoltage_divider_circuit "Voltage Divider Circuit") |

| Photos |
| ---------- |
| ![alt text](https://github.com/Silverune/MMM/blob/main/photos/3M.jpg "3M Wall Installation") |
| ![alt text](https://github.com/Silverune/MMM/blob/main/photos/3M_circuit.jpg "3M Circuit") |
| ![alt text](https://github.com/Silverune/MMM/blob/main/photos/3M_LCD.jpg "3M Display") |

# Links
- [Raspberry Pi Pico W Official Circuit Diagram](https://datasheets.raspberrypi.com/picow/PicoW-A4-Pinout.pdf)
- [Raspberry Pi Pico W Official Documentation](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html#pinout-and-design-files17)
- [Raspberry Pi LCD1602 Control](https://www.mbtechworks.com/projects/drive-an-lcd-16x2-display-with-raspberry-pi.html)



