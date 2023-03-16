# Local Data Point
#
# This firmare is run on each Pico that has water sensors attached.   It assumes status is via
# both a locally attached 16x2 LCD and serially

# libs
from machine import Pin, ADC, PWM
from time import sleep_ms

from gpio_lcd import GpioLcd

from common import scale_value
from vds001 import VDS001
from pico_temp import PicoTemp

# lcd custom characters (limit 8)
SYMBOL_CELSIUS = 0
SYMBOL_EMPTY = 1
SYMBOL_FULL = 2

# lcd data
d4Pin = 18
d5Pin = 19
d6Pin = 20
d7Pin = 21

# lcd control
ePin = 17
rsPin = 16
ledPin = 25
contrastPin = 26

# inputs
pinContrast = ADC(Pin(contrastPin))

# max of 9 supported by display
waterSensors = [
    
    VDS001(6),
    VDS001(7),
    VDS001(8),
    VDS001(9),
    
    VDS001(10),
    VDS001(11),
    VDS001(12),
    VDS001(13),
    
    VDS001(14),
]

temp = PicoTemp()

# outputs
lcd = GpioLcd(rs_pin=Pin(rsPin),
              enable_pin=Pin(ePin),
              d4_pin=Pin(d4Pin),
              d5_pin=Pin(d5Pin),
              d6_pin=Pin(d6Pin),
              d7_pin=Pin(d7Pin),
              num_lines=2, num_columns=16)
led = Pin(ledPin, Pin.OUT)

def digitalToRepresentation(value):
    if value == True:
        return SYMBOL_FULL
    return SYMBOL_EMPTY

def digitalToDebugRepresentation(value):
    if value == True:
        return "*"
    return "."

# init
def init_lcd():
    global lcd
    lcd.clear()
    lcd.putstr(" Temp: ")
    lcd.move_to(0,1)
    lcd.putstr("Water: ")

lcd.custom_char(SYMBOL_CELSIUS, bytearray([0x06,0x09,0x06,0x0,0x0,0x0,0x0,0x0]))
lcd.custom_char(SYMBOL_EMPTY, bytearray([0x1F,0x11,0x11,0x11,0x11,0x11,0x11,0x1F]))
lcd.custom_char(SYMBOL_FULL, bytearray([0x1F,0x1F,0x1F,0x1F,0x1F,0x1F,0x1F,0x1F]))

init_lcd()

while True:
    contrast = pinContrast.read_u16() # 16-bit integer result
    sleep_ms(100)

    temperature = temp.update()
    sleep_ms(100)

    for waterSensor in waterSensors:
        waterSensorsDebug = waterSensor.update()    

    waterSensorsDebug = ""
    for waterSensor in waterSensors:
        waterSensorsDebug = waterSensorsDebug + digitalToDebugRepresentation(waterSensor.read()[RDJ001.DIGITAL])

    display = "Contrast: {} Temp: {} Water: {}".format(scale_value(contrast, 0, 65535, 0, 100), temperature, waterSensorsDebug)
    print(display)

    lcd.move_to(7,0)
    lcd.putstr("         ")
    lcd.move_to(7,0)
    lcd.putstr("{} ".format(temperature))
    lcd.putchar(chr(SYMBOL_CELSIUS))
    lcd.putstr("C")

    lcd.move_to(7,1)
    lcd.putstr("         ")
    lcd.move_to(7,1)
    for idx, waterSensor in enumerate(waterSensors):
        lcd.putchar(chr(digitalToRepresentation(waterSensor.read()[waterSensor.DIGITAL])))

    led.toggle()
