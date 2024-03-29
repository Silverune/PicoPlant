<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/diagrams/PicoPlantLogo.png" />
</p>

# Pico Plant
## Introduction
This project develops a low cost microcontroller controlled moisture monitoring solution that can be applied to a variety of moisture detection requirements.  The entire project should cost similar to the price of a commercial single moisture probe with plenty of scope for future enhancement.  Some knowledge of interfacing to a microcontroller and the ability to solder is required.

### Final Product
The following is a photo which shows the completed project along with it being used to monitor 9 hanging plants.   The control unit is on the bottom left of the picture (blue display) with the probes connecting to an interface box and then feeding to the individual plants via the metal support at the top.

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/photos/PicoPlantInstallation.jpg" />
</p>

The top-level components of the project.

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/diagrams/top_level.png" />
</p>

Which is controlled via the following circuit using a Raspberry Pi Pico W and the status of the plants is displayed on an LCD1602

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/diagrams/circuit.png" />
</p>

The finished display looks as follows:

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/photos/3M_LCD.jpg" />
</p>

The entire build is connected to an interface module:

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/photos/3M.jpg" />
</p>

Installed in some hanging plants:

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/photos/3M_plant.jpg" />
</p>

**NOTE** - I have added affiliate links to most of the items listed in this blog.  As such, any purchases made through those links results in a small commision which assists in developing the project further.

## Key Elements
The following are the primary elements required:

- **Microcontroller** - the device connecting everything together.  This controls the display and receives input from the sensors
- **Firmware** - control software for the microcontroller which is able to process the inputs and output to the display
- **Display** - visual interface to show the current status of the sensors
- **Sensors** - input sensors providing the moisture information

Each of these elements can be interchanged as required.  For this specific implementation I have used:

### Microcontroller - [Raspberry Pi Pico W](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html) (RPIPW)
## <sub><sup>https://amzn.to/3ZNeLJn (with soldered headers)</sup></sub>
This low-cost microcontroller is able to completely suit the requirements for the project with enough general purpose input / output (GPIO) pins to satisfy all the current requirements (pun intended).  It can also provide 5V and 3.3V for external peripherals (display) and if desired can be network connected (hence the “W” in the product name).  Networking of the display results is not covered in this documentation as that is outside the scope of the project and is common to all Raspberry Pi Pico W projects

### Firmware - [MicroPython](https://micropython.org/) / [PicoPlant Repo](https://github.com/Silverune/PicoPlant)

This can be broken into two main areas:
1. **Operating system** - using MicroPython.  This has a number of advantages and the processing requirements of the project are minimal.  Rapid development and ability to run a serial monitor for debugging makes this a suitable choice.
2. **Application software** - this is custom built for the project (supplied in this repository).  It consists of the following main elements:

   * device driver for the temperature sensor on the RPIPW
   * device driver for the chosen 16x2 display (LCD1602)
   * device driver for the custom sensors
   * custom fonts for use with the display
   * device initialisation
   * main processing / monitoring loop (“main”)

All the MicroPython code required is provided in this repository.  If using an alternative sensor than the one I've specified (e.g., an off-the-shelf capacitive or resistive sensor) I have also provided a couple of device drivers I created for those as well but I did not end up using either of those as they are expensive and offer no advantage in my use-case.

### Display - LCD1602 
## <sub><sup>https://amzn.to/409E4oM</sup></sub>
Note: this item is almost always shipped in any Arduino compatible starter kit (e.g., [Elegoo kits](https://amzn.to/3LpCuem)) so it is recommended to get it as part of a kit if you have even a general interest in electronics. These kits provide excellent value and is a common display with a variety of methods of driving the display.  I have opted to not complicate the project with requiring the I2C driver and have instead used it in 4-bit mode to handle the display.  Using it with only 4-bits has no functional downside as the update rate of the screen is only a number of hertz and it reduces the need for additional data lines / soldering.

### Sensors - Voltage Dividers
## <sub><sup>https://amzn.to/3mUGQzN</sup></sub>
20K ohm resistor (one per input sensor) .  The solution used for this project involved building 9 custom voltage divider circuits which are fed into the GPIO (digital) pins on the RPIPW using a voltage divider inputting the 3.3V RPIPW back into the GPIO pins as an input.   The actual sensors themselves consisted of wires connected to more robust hardware that can be inserted deep into soil. 

### Other - Necessary Evils
While not key elements, the following are also required for the project:

1. **5V DC Power Supply** (the RPIPW requires 3.3V but the display is a 5V device so needs this extra voltage.  Total current draw is only in the order of 40mA) https://amzn.to/3lhiHTq  Alternatively, I could have used a boost converter such as the TPS61200, LTC3525, MAX1724/MAX756 or MCP1640. All of these ICs are specifically designed to provide voltage boosting capabilities within the scope of the project.  However, as I already had a 5V source this was not required.  If only powering the RPIPW from the 3.3V USB source this may be of interest (while adding slightly to the complexity).
2. **2.1mm Female Power Jack** for connecting the power to the board https://amzn.to/3YWlJdS
3. **Protoboard** for soldering everything together https://amzn.to/3JfQLax / https://core-electronics.com.au/protoboard-63-row.html
4. **Hookup Wire** (I used solid core) to hook everything up https://amzn.to/3yDnwJN
5. **10K Potentiometer** for brightness control of the LCD display. https://amzn.to/3Tl3z43
6. **10uF Capacitor** across the power rails https://amzn.to/3mJhnJq  Avoid spikes due to dodgy power supplies and takes out some noise.

### Other - Non-necessary Evils
These are items I ended up using but depending on your installation requirements may not be required:

1. **Wooden Mounting Board** - any offcut will do that's large enough to hold the mounting board
2. **Metal Brackets / Screws** - assumed you have this staple
3. **Electrical Wire** (dual core) to run out to each sensor as I had a long run which made using regular wire cost-prohibitive and messy. https://amzn.to/3JhbVFd
4. **A Female Header 20-pin Mount** for connecting the sensors to https://amzn.to/3lhkbNu
5. **Electrical Connecting Adapters** to separate the tent peg wires from connecting directly into the protoboard https://amzn.to/3ZObedI
6. **Tent Pegs** (2x per sensor) these were connected via wires to the resistors which then form the voltage dividers as inputs to the microcontroller. https://amzn.to/3FphK2s
7. **Heat Shrink Solder Connectors** - these made connecting the wires to the tent pegs relatively straight forward as the tent pegs are not easy to simply solder to without using a lot of solder/flux and a substantial soldering iron due to the mass of the pegs.   This provided an easy shortcut. https://amzn.to/3YJnQRT

The female header 20-pin mounts being used to separate the interface cables:

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/photos/3M_female.jpg" />
</p>

Electrical Connecting Adapters:

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/photos/3M_interface.jpg" />
</p>

When both are connected together form the following unit which I have zip-tied to vertical support:

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/photos/3M.jpg" />
</p>

### Equipment
Most of these items are workshop staples.  For completeness I have listed what I used:

1. **Soldering Iron / Station** (Composite Tip) https://amzn.to/406pVZd
2. **Solder 63/37 Rosin Core** (thin - 0.5mm) https://amzn.to/3likx6H
3. **Digital Multimeter (DMM)** https://amzn.to/3ZOJaGW
4. **Bench Power-Supply** https://amzn.to/3yEkOUt
5. **Computer** - Mac / PC etc.  I used a Raspberry Pi 4 https://amzn.to/4060Ei2
6. **Heat Gun** https://amzn.to/3JhXyR9
7. **Bench Vice** https://amzn.to/3JFZg00
8. **Wire Strippers** https://amzn.to/3laT0Ei
9. **Wire Cutters** https://amzn.to/3TkRwnA
10. **Digital Microscope** https://amzn.to/3Tl6cCX (optional for double-checking soldering / debugging)

## Philosophy 
The general idea behind this project was to base it on a real-life requirement I had which was to monitor the moisture levels of 9 different types of plants in a location out of easy reach (required a ladder each time to check moisture levels with a traditional metre).   Additionally, each of these plants was planted in different hanging baskets sizes with different soils types so a sensor on a random plant would not be indicative of all the plants.  Continuous monitoring was not required as no automated watering was connected so there was no need to run power to it until actually interested in the results.  Due to the distances between the plants and where the control unit would be a large amount of wire would be required.  In my case something like 40m of wire was required in total.

Delving into each of the key elements

### Microcontroller
A minimum cost microcontroller is all that is required for the project.   As long as there are enough input / output ports to hook everything up then pretty much any microcontroller should do.  I chose the RPIPW as it was low-cost, could later be Wifi connected (if I decided I also wanted remote monitoring) and had great community support.   An Arduino (Uno etc.) would also be a completely suitable solution with only minor modification to the sensors due to the level change from 3.3V to 5V. 

One consideration that may be not initially obvious is the fact that most microcontrollers have only a limited number of analog inputs while having an abundance of digital inputs.   Most commercial moisture meters like to give analog output, while some will also provide a digital output as well (controlled by a potentiometer on the control board).  For my purpose this was overkill, I simply wanted to know when the plant required watering because the soil moisture had dropped to a level I considered was “time to water” (more on this in the sensor discussion below).   As such, analog inputs are only used in two instances in the entire project: temperature sensing (internal as part of the RPIPW) and for debug as part of the LCD brightness control (optional). 

The firmware using MicroPython was purely a choice based on simplicity.   There were more steps involved in getting a C compiler development setup all working with no significant advantage based around speed.  As such, easy to go with MicroPython where there were already a number of external support modules already built I could use.  (e.g., LCD display driver).

### Display
As there are only a boolean display required for each of the input sensors (water / non-water) and a single temperature display there was no requirement for a high resolution screen and a simple 16x2 display would suffice.  In fact, even though the display supports I2C it was also considered overkill to bother using in this manner as the screen was simply showing the sensor status on a single “page”.  I did create a few custom character fonts to make the display look slightly more professional than simply using the default 8-bit ASCII selection.  These were a celsius symbol as well as full and empty water indicators.   Also - there is an (optional) battery display available which scales a custom character font to show the state of the batteries if using.

### Sensors
This is the most subjective and varied part of this project but also the part most people will be attracted to about this project.   The reasons for this is that there currently doesn’t exist very many reasonably priced robust moisture monitoring components on the market and those that do exist and are reasonable are overkill for a non-continuous monitoring requirement.   I’ll break down in simple terms my views on each and how I came to reaching my decision to simply “reinvent the wheel”.

1. **Water Level Sensor Detection Unit** (e..g, https://amzn.to/3yEdCYt / https://amzn.to/3yEdRCR)   These units function completely fine in a limited use case.   They still cost roughly $4 in bulk so hooking up a whole greenhouse might start to add up and they cannot have power applied continually or they oxidise and become unusable after a few months.  In some cases they provide an analog output which (as mentioned previously) is not required or desirable. 
2. **Capacitive Water Sensor Detection Unit** (e.g., https://amzn.to/3TfFPhE)  These are seen as superior to the regular detection sensors mainly due to their ability to resist corrosion as they do not have exposed copper wiring.  However, they come at a higher cost (generally over 3x the cost) and if there is no requirement to be continually powered then this is not an issue.  Additionally, they appear to be difficult to source the better quality units with an ability not to corrode.
3. **Traditional Analog Design**  There are no off-the-shelf versions of this that are suitable for adding to the project though it is trivial to build one.  Many of the older electronics kits like the [Dick Smith's Fun Way Into Electronics Volume 1 Project 3](https://archive.org/embed/funway_into_electronics) / [Jaycar Short Circuits Volume 2 Project 6](https://www.jaycar.com.au/medias/sys_master/root/hb7/h46/8884452786206/BJ8504-ShortCircuits-2-310316.pdf) home hobbyist solutions involve a simple LN2022 style NPN (PNP in Radio Shack’s case) transistor amplifying a weak signal through the amplifier and lighting up an LED to indicate water level or continuity.  In the Short Circuits case this is a nice flexible solution with a simple toggle between the Wet / Dry detection types but still uses an IC to deal with flashing an LED and sounding an alarm.   This is not required as we can simply toggle the Wet / Dry state in the Python code if need to be and we already have a display connected to deal with communicating the probe results back to the user.   So even though these are simple solutions they are still over-engineered for what we need and to be fair these were never designed with a microcontroller input in mind.  It would mean each sensor requires a transistor and one (or two) resistors as well as an IC.  Not a huge cost but also not required.
6. **Voltage divider coupling**  This is the design I have gone with - rationale:

    * We have a number of knowns that other solutions don’t - using that to our advantage. The main one being that we are trying to turn an analog value into a digital one.   That’s a whole rabbit hole in itself but in our case it boils down to simply matching the resistance in the sensors when there is enough moisture between the probes with the positive signal the microcontroller accepts.   To break down each:  
    
     * **Resistance in the sensor** - there are many ways to look at this problem.  The two off-the-shelf solutions monitor the change in voltage (resistance) or capacitive build-up. In either case the conductivity in the circuit changes the transducer to report a different value.   I took the approach of looking at resistance changes caused by moisture changes.  Simply put, pure water doesn’t even conduct electricity, its the impurities in water that allow current to pass.  However, soil happens to have a lot of impurities so you will often get a surprisingly strong reading in what we would think of as mostly dry .   Therefore the approach is to simply to use an external reference to work out what is considered “dry” or “needs water”.   I used a trational water probe with an analog scale from 1 to 10.   On this scale anything 3 or below is in the red (dry).  So I simply sampled a number of plants I had at that level and used a digital multimeter to measure the resistance in our sensors in the soil and note that as a reference point.   Despite a wide range of soils I found values in the 20k to 50k ohm to be the sweet spot.  Once dry the resistance quickly shoots up into the mega ohm range.   This resistance is important in the next step.  NOTE: Under certain weather conditions (very cold) this method breaks down.  In these conditions the resistance will go up and the plants will appear to be dry while they are actually just extremely cold.  If living in such a climate and monitoring plants under such conditions then this solution might not be suitable.

    * **Analog Input** - most microcontrollers have a very limited number of analog inputs (and we don’t need them anyway).  The goal becomes converting the sensor reading to an on or off (boolean) value for the software.   This is where a data-sheet can come in handy but these are still only a guide.   You can simply test your microcontroller with a potentiometer or variable power supply and work out what is a logical on and off and how this maps to the voltage.  To use a specific example of the RPIPW the data-sheet lists the logical “high” as 1.6V (it’s a 3.3V device so essentially half the voltage) all the way up to 3.3V.  There is an undefined dead zone that any values below 0.8V count as “low.  On the other end of the scale if somehow the sensors were directly connected together ("short-circuit") then it would read the source voltage of 3.3V.  This is important information for the design - we need to match the minimum high to the threshold maximum resistance that we want to trigger on.   e.g., if we find that 20k ohm resistance means the plant needs water then we map this 20k ohm to a voltage that will (at minimum) remain high.  Once the resistance goes beyond this we are dropping into the undefined / low state which is when we need to water the plant.   The solution, a voltage divider.   We simply couple the input sensor to the input resistance that we deem too low and everything falls into place.  If the sensors in the soil are just watered and the conductivity is high at most it can only ever be 3.3V (the supply voltage output from the GPIO pin) but if it resists above our value the voltage on the GPIO pin drops below 1.6V and the sensor will read low (in reality once in the undefined state it flickers around which is actually desired as it shows that this reading is on the threshold - a non-binary reading on a binary sensor!).

  * **Super cheap** - the design consists of two wires and a resistor - it’s almost impossible to make a cheaper unit!  No matter how many sensors you add there is simply no way that will blow your budget.  As far as design real-estate it is also advantageous - on the protoboard it can be simplified to take up as little as 2 rows.
 
      * **Robust** - Electronics often requires lots of wires, power supplies etc. that are not compatible with the dirt, Sun and water requirements of plants.   Additionally, when doing actual watering it can be quite a physical process and move the plant and soil around.   So the design needs to deal with this reality while still feeding the information back for processing by the microcontroller.   I used levels of robustness to achieve this and took specific steps to decouple the sensors to the board via an optional interface.   These levels start with the GPIO pins of the RPIPW:
        * Circuit wire to the resistor where the voltage divider is located.  This is fed by a separate wire that is connected to a female header socket.
        * A single core wire connecting the female connector input (male) to an electrical connector box.
        * A multistrand dual wire line ("Electrician's wire") is connected to the other input of the electrical connector box
        * The electrical wire is run out to where the plant to be measured is located and is connected via electrical heat solder wrap to two large tent pegs which have been inserted into the soil.  The electrical wire is also anchored above the plant to reduce movement during watering.

  * **Debugging** - Diagnosis is fast and simple.  At all points the circuit can be examined to ensure correct functionality.  Other than the microcontroller and display there are no IC’s to deal with and each part can be taken apart without having to uninstall / remove the whole setup from the connected plants.

In summary, the solution involves a simple cheap off-the shelf microcontroller that is well supported both by the organisation / community.  The language used has low barriers to entry and there exists many third-party libraries making this a fairly safe choice if you get yourself into trouble.  The display is nothing to write home about but completely functional for the job and very low cost - especially if you get one in a bundle and for simple usage will be more than enough.   The sensors themselves are the cheapest part of the whole project which is important as this is the part you may have the most of.  The design is simple and dirt cheap - when you can have faith a 50c sensor will do the job of a $12 off-the-shelf unit (while not taking up an analog input) then this is the best part.  Simply add as many units as you like - it’s only the effort of wiring things up that becomes the issue (not in any way the cost).  As long as your microcontroller has spare GPIO pins then you can simply keep adding more.

## Build

### Parts List
For completeness I will list all the parts used for my build.   Understandably, less parts could be used (not including “*Other - Non-necessary Evils*”) but if you are not interested in my particular installation simply ignore these items.   It is better to have a complete reference than to leave these out.

The list will be broken into the software and hardware side of things.

### Software
The following software is required for the project:

  * MicroPython installation.
  * This repository - download all the files from this repo and copy them over to the device.  I would recommend renaming the “```main.py```” file to something else to start with as this will be the file that get automatically booted each time the device is reset so if you have problems you are advised to run this from the interpreter (e.g., Thonny) in case there are problems that hang your microcontroller each time.  
  
    When finally happy with the firmware you will put the “```main.py```” file onto the device for the final installation.  If you don’t require any of the other sensor types (I didn’t) then you can leave off the “```capacitive.py```” (if not using capacitive sensors) and “```hw080.py```” (if not using regular off-the-shelf resistive sensors).  All other files are required.

### Hardware
This can be broken down into a few sections:

### Electronics components
* Raspberry Pi Pico (W optional) https://amzn.to/3ZNeLJn
* 10k Ohm potentiometer https://amzn.to/3Tl3z43
* 9x 20k Ohm resistors (1 / sensor) https://amzn.to/3mUGQzN
* LCD1602 compatible display https://amzn.to/409E4oM
* 2.1mm power adapter (positive inner core) https://amzn.to/3YWlJdS
* 5V DC power supply https://amzn.to/3lhiHTq
* 10 uF capacitor https://amzn.to/3mJhnJq

### Physical Hardware
* Protoboard large enough to solder all the components. I used a MakerVerse which I found worked perfectly
* 20x1 female IC socket
* AWG 22 single core wire
* 40m insulated 2 core wire (this is very installation dependant - my installation required a lot of wire due to the location.  Most implementers are likely to not require this amount).
* 18x tent pegs (2 / sensor)
* 18x solder seal wire connectors (heat shrink solder connectors)
* 9x Electrical contact connectors (2-input)
* Wooden board (larger than your protoboard)
* Screws to bolt protoboard to installation board
* Offsets for each screw (my particular installation used both side of the protoboard so needed to have the board offset in the final installation location
* Cable ties (I required the final installation vertically mounted on a metal strut so these were used.)

## Design
The following is the broad design of the entire project.  Broken down into it’s simplest components:

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/diagrams/top_level.png" />
</p>

The circuit board is powered by the 5V supply which is then connected to an external interface which acts as commications point with sensors going out to each of the plants to be monitored.

The main electronics work is on the protoboard.  This is the design.

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/diagrams/circuit.png" />
</p>

Each sensor consists of the following simple voltage divider circuit.

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/diagrams/voltage_divider_circuit.png" />
</p>

Which is simulated here and can be interacted with: [Pico Plant 3.3V Voltage Divider Circuit](https://everycircuit.com/circuit/4855455733776384)

The linked simulation can be used to prototype differing resistance selections.  The “V” in the simulation maps directly to the GPIO input of the microcontroller.   As can be seen by varying the potentiometer (which simulates the differing dryness levels on a scale of 1 to 10) this brings the voltage into a logical “high” state when above a value of 3 which equates to around 1.8V on the GPIO input.   Short circuit (10) yields 3.3V which is still safe as the GPIO input.   Anything dryer / lower than this is a  logical “low” (< 1.8V) and triggers the false boolean state on the input.  The undefined area between 1.8v and 0.8v will generally trigger an intermittent transient state which shows up on the LCD as a flickering ON/OFF state for that sensor.

If requiring finer precision in the on / off state the resistor can be changed to something lower (e.g., 10k ohm) which will make the sensor more sensitive.   An alternative is to instead install a potentiometer (100k ohm) which can be used to perfectly tweak the dry / non-dry setting for your particular scenario.   This was over-kill for my requirements but would be an easy modification (quite a bit more cost / soldering though).

The voltage divider circuit fundamentally boils down to the following equivalant circuit:

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/diagrams/voltage_divider_b.png" />
</p>

Which in practicality looks like this with the two sensors going into the plants soil to have the moisture measured.

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/diagrams/voltage_divider_a.png" />
</p>

The resistance in the wire used for the sensors can generally be ignored.   Over a typical length and the fact that the voltage divider is using quite a sizeable resistance this does not play a significant role in the design.  Typical wire resistance might be in the 8-10 ohm range while the resistors being used are 20k ohm so this constitutes 0.05% difference.

Traditional water sensors work by having different materials in the probe and the conductivity in the water create a battery which is passed across a 1k ohm resistor then fed to the analog display.  This solution uses a larger resistance but from two separate probes and then measures the voltage drop when the 3.3v input source is applied.   The voltage divider resistor on the board regulates what the voltage drop is in relation to the GPIO input.

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/diagrams/probes.png" />
</p>

To construct the sensors the following process was used.

1. Bend the tent peg into a straight shape.   The tent peg is a suitable choice due to its robust nature and ability to push deep into the soil with no issues.  However, the hook that most tent pegs have is not required unless the probe is used in a hanging basket and even then I found I still wanted to run the wires up to the top of the structure for easier channeling to the controller unit.  To bend the tent peg use either a pair of pliers (easy) or a bench vice (cleaner / better result).
2. Cut some wire that is easily able to span the distance from the plant to the controller.   This is where I used electrician’s wire as a single cable was able to hold two inner wires isolated and came in long roles (mine was a 100m in length!).
3. Strip the wires and put each into a solder seal wire connector.  Use a heat gun to seal the tent peg to the wire (x2) 
Congratulations - you have your first sensor.   Now do this again for however many you require - 9 in my case.

## Firmware

### Operating System
Before you will be able to use any of the files in this repository, the first thing you will need to do is install the MicroPython bootloader onto the RSPPIW.  Follow these instructions to get started: https://www.raspberrypi.com/documentation/microcontrollers/micropython.html

### Application Code
The code in this repository will need to then by copied across to control the system.  This is not designed to be an exhaustive line by line talk-through of the MicroPython code.  It is meant to give an oversight of what is being done, how it is being done and any non-obvious sections of the code that might be helped by additional explanation.

Files:

- ```main.py``` - this is the "main" where the MicroPython starts executing the code.  All other files are referenced from this one.
- ```vds001.py``` - device interface for the voltage divider circuit.  Essentially, this is a simple wrapper around assigning one of the GPIO pins to act as a digital input.
- ```pico_temp.py``` - the Raspberry Pi Pico has a built in temperature sensor.  This file has routines for reading this value and processing the results
- ```lcd_api.py``` - API class for sending information for display to the LCD.  Original is from https://github.com/dhylands/python_lcd
- ```gpio_lcd.py``` - top-level class for interfacing to the LCD.  This is the class used by main.py.  It uses ```lcd_api.py``` as part of its implementation.  Original is from https://github.com/dhylands/python_lcd
- ```common.py``` - utility routines and constants used by the firmware

Additionally, optional files provided are:

- ```hw080.py``` - device interface if using a traditional off-the-shelf water sensor
- ```capacitive.py``` - device interface if using one of the newer capacitive off-the-shelf water sensors

As mentioned previously, the provided implementation uses only the voltage divider circuit so the other two device drivers are provided only as an option.

The ```main.py``` is the only file that is worth looking at in any detail.  All the others can be considered "black boxes" which do their job without needing to understand how they are doing it.

Broadly, most microcontroller code is always broken down into the following sections:

* Initialization
* Looping over the input / outputs

### Initialization

This can be broken into the following:

* **Inputs** - data that the microcontroller will process
* **Outputs** - communication to the LCD

Inputs consist of:
* **Temperature sensor** - analog-input on-board
* **Sensor inputs for the moisture probes** - digital GPIO (x9)
* **Contrast potentiometer** - value for debugging (analog-input)
* **Battery Level (Optional)** - to show the health of the battery module

Outputs consist of:
* **Digital nybble lines** - for displaying a character on the LCD (digital GPIO x4)
* **LED Control** - for debugging (digital on-board)
* **LCD Enable** - (digitial GPIO) to facilitate writing of data to the registers
* **LCD Register** - select (digital GPIO) used for controlling where the LCD stores data sent to it
* **Battery Health (Optional)** - visual representation of the state of the batteries

At startup all of these inputs / outputs are configured and the appropriate library classes are passed the desired configuration.   In most cases the GPIO assignments can be switched around to match a different wiring configuration but any of the on-board sensors need to remain untouched as they are not configurable.  These are:

* **Temperature** - sensor on analog pin 4
* **On-board LED** - mapped to GPIO pin 25

Neither of these pins appear on the regular pin-out diagram but the software maps to the analog / digital ports just like any other input.

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/diagrams/raspberry_pi_pico_w_pinout.png" />
</p>

For my particular installation, I wanted to have all the moisture sensors on one side of the microcontroller and leave the other side purely for the LCD.   This was to give a little more space on protoboard to focus on each of these sections in isolation of the other.  So the moisture sensors are mapped to GPIO pins 6-14 while most of the LCD control pins are on the other edge of the micrcontroller GPIO pins 16-21.  There is also an analog input pins configured which shows the output of the LCD contrast potentimometer but this is purely optional and was used during development for display on a serial monitor.

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/photos/3M_circuit.jpg" />
</p>

The only other significant initialization before the main loop is creating a number of custom characters for the LCD display as these are not by default supported with the existing libraries I was using.  The characters are:

* **Celsius symbol** - the LCD has a temperature display and this makes it appear a little more professional
* **Symbol to show for lack of moisture** - "dry"
* **symbol to show for acceptable moisture** - "wet"

These are simply encoded into a sequence of 8 5-bit values (additional bits of byte are ignored) which are then handed to the library for use later.   Additionally, we also initialize the LCD library and show an initial screen.   Due to the way the main loop (moves cursor to the update location and doesn't refresh whole screen) updates the screen the labels for the temperature and water only ever need to be sent to the LCD once at startup.

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/photos/3M_LCD.jpg" />
</p>

Next is the main loop.  Here is where the microcontroller spends all of its time performing the same operations until it is switched off.  These are:

* Read the current state of the contrast potentiometer (optional) before a short wait
* Read the current state of the temperature sensor before a short wait.
* (Optional) Read the current state of the battery before a short wait.

These waits are generally considered best practise when reading from analog inputs, they may not be required but I haven't tested thoroughly without them so have opted to leave them in.

Next comes the reading of all the moisture sensors.  This is simply done in a loop by reading the digital input value currently on each of the configured GPIO pins.   Any reading 3.3V down to rougly 1.8V is read as a "high" while anything below 0.8V is "low".   Anything with the range between these two is undetermined and may appear as either high / low.   In practise this tends to show as flickering between the two states.

Now all values have been read the next job is to act on the data.  This boils down to:

* Output results via the serial debugging interface (optional)
* Updating the temperature value on the LCD
* Converting the high / low values from the moisture monitor sensors to a representation on the LCD (dry/wet).

For the output to the serial interface this is a built-in function for micropython where a simple "print()" outputs the information and can be viewed from within the IDE (Thonny).

The updating of the LCD for temperature moves the logical cursor (though it is not visible) up to the top-line of the display and outputs the most recent temperature value (followed by the custom celsius symbol we defined earlier).

Similarly, each of the moisture sensors is also updated by moving the cursor back to the bottom line and showing either of the custom symbols we defined for each state next to each other.   An example display is as follows:

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/diagrams/LC1602.png" />
</p>

The top row is showing the temperature in celsius while the bottom consists of each cell showing our custom character for either "wet" (full) or "dry" (hollow square).  It is easy to change this to whatever is desired but this served to be quite clear at a distance when performing the actual watering and monitoring the display.

# Battery Power / Indicator (Optional)
One modification to the base design is to add in an option for the unit to be battery powered rather than requiring a wall power-supply.  The current draw is only in the order of 40mA and typically lower with the main draw only being the LCD1602 rather than the Raspberry Pi Pico.

The main requirement is providing a 5V voltage for the ```VSYS``` input on the RPIPW.   If using a simple 1.5V battery pack of 4 this outputs 6V which can then be fed into a voltage regulator to step down to 5V.  Assuming using an alkaline AAA battery which has a capacity of 850-1200mAh (for simplicity we’ll say 1000mAh).  Therefore,
```
  4 x 1000mA = 4000mA total
```
So the power consumption is:
```
Voltage * Current = 5V * 40mA = 0.2 watts
```
To estimate the battery life, divide the total energy capacity of the battery pack by the power consumption of the circuit:
```
Battery Life = Battery Capacity / Power Consumption = 4Ah / 0.2W = 20 hours
```

### Voltage Divider
Circuit design:

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/diagrams/battery_indicator_circuit.png" />
</p>

This design can be interacted via the simulation here: [Battery Indicator](https://everycircuit.com/circuit/4574887641088000)

Therefore, with a 6V battery pack consisting of four alkaline batteries, and a circuit drawing 40mA of current from a 5V voltage regulator, the batteries would last approximately 20 hours. This is a rough estimation, and it may vary depending on factors such as battery discharge characteristics and efficiency of the voltage regulator but certainly gives a ballpark idea that the unit can be run for a long time without needing the batteries replaced as it’s not a unit that should be left on and typically would only be switched on for a few minutes at a time.

The following circuit can be added in place of the existing 5V DC input:

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/diagrams/MR2940CT-5.0_Battery.png" />
</p>

The main elements are the 6V battery pack feeding into a 5V voltage regulator which then feeds into the RPIPW.  The regulator is required to step down the voltage from 6V to 5V while also ensuring smooth operation for varying current draw.

## Low Battery Indicator
One advantage of having the LCD screen as part of this project is also using it as a display for the state of the battery health.  The design takes advantage of the unused ```ADC1``` input and uses a voltage divider circuit out of the battery pack to change the input from 3.3V when the voltage is at 6V down to 2.78V once the voltage reaches 5V.   At 5V input to the voltage regulator the IC is no longer able to output 5V to the ```VSYS``` line so the batteries should be replaced.  This pin can then be read as part of the main loop to check the voltage and scale an indicator on the screen appropriately.

<p align="center">
  <img src="https://github.com/Silverune/PicoPlant/blob/main/photos/Battery_Indicator.jpg" />
</p>

This is done by regenerating a custom display character each time which shows one of the 16x2 cells partially filled depending on scaling between the 3.33V (full) and 2.78V (empty).  The battery functionality can be toggled on / off using the boolean “BATTERY_POWER” at the top of the ```main.py``` MicroPython code.

# Dual Power / On-Off Switch (Optional)

## Dual Power
Another reasonable modification to the standard circuit would be to combine the battery option above with the ability to also have it powered from a wall mount DC supply.   Either supply voltage should be able to be used to power the system and with some simple diode protection even if both battery and the wall power were present the unit would still work.   Essentially, we can keep the exisiting battery circuit (above) but then run the output from the voltage regulator through a low forward voltage drop Schottky diode (I chose the ```1N5819```).  The voltage drop will only be in the order of 0.3V which is within specification of the system (even USB powered RPIPW has only around 4.5V on the ```VSYS``` output).   We could modify the original 5V DC power supply design to ensure it also has its own forward voltage diode (same as the voltage regulator) so there is no chance of backfeeding to deal with if there happens to be power coming from both the battery pack and DC wall supply.  This is optional though as while there is DC power there will be no voltage drop across the battery diode so no current should be flowing.  Only if the DC supply is off would the voltage drop exist which would make the battery power supply current to the ```VSYS```.   It is only recommended to run one or the other as running both will still drain the batteries (albeit a lot more slowly).

A simulation of how it works is here: [Dual Power](https://everycircuit.com/circuit/5978638612430848)

## On-Off Switch
For the power switch there is a slight complication in that we really only want one switch but it needs to turn-off power in two locations.   The obviously main location is just before the ```VSYS``` input to the microcontroller (anywhere after the dual power diodes).   However, in the case where battery is being used this still results in a current draw as the battery level indicator feeds a signal to the analog input of the microcontroller before it goes goes through the voltage regulator which means that it will still be drawing a current regardless of there being no flow in the regulator (very small, in the order of 15.5uA but still undesirable).   So we need to also switch-off the battery input to this battery status circuitry when the switch is toggled (either side of the battery terminals will work).   To achieve this with two separate circuits via a single switch we use a double pole double throw (DPDT) switch that controls both parts of the circuit yet are isolated from each other - many commercial options are available.

# Summary
The above project creates a simple yet versatile water monitoring solution using readily available off-the-shelf components.  It would act as a good introduction to any hobbyist looking to get into electronics or using microcontrollers.   It can act as a starting point to a more involved sensing system that can be used for continuous monitoring and there are plenty of spare pins on the microcontroller so that automated watering could also be implemented if so required.  Also, the Wifi features of the Pico W have not been actively used but I chose this to future-proof later changes without the need to install a different controller.

I hope this has been helpful, feedback always welcome.

# Links
- [Raspberry Pi Pico W Official Circuit Diagram](https://datasheets.raspberrypi.com/picow/PicoW-A4-Pinout.pdf)
- [Raspberry Pi Pico W Official Documentation](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html#pinout-and-design-files17)
- [Raspberry Pi LCD1602 Control](https://www.mbtechworks.com/projects/drive-an-lcd-16x2-display-with-raspberry-pi.html)
- [5V Voltage Regulator LM2940CT-5.0](https://au.mouser.com/ProductDetail/Texas-Instruments/LM2940CT-5.0?qs=X1J7HmVL2ZHPtClZnI0H9A%3D%3D)
- [Thonny IDE](https://thonny.org/)



