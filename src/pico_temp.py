# Raspberry Pi Pico In-Built Temperature Sensor
#

from machine import Pin, ADC
from common import scale_value, CONVERT_TO_VOLTS

class PicoTemp:

    VOLTAGE_REDUCTION_PER_DEGREE = 0.001721 # datasheet: 1.721 mV
    REFERENCE_TEMPERATURE = 27              # datasheet
    REFERENCE_VOLTAGE = 0.706               # datasheet

    analogPin = 4                           # internal pin so not mapped via a GPIO
    analogValue = None
    analogSensor = None
    
    def __init__(self):
        self.setup()

    def setup(self):                            
        self.analogSensor = ADC(self.analogPin)

    def update(self):            
        reading = self.analogSensor.read_u16() * CONVERT_TO_VOLTS
        temperature = self.REFERENCE_TEMPERATURE - (reading - self.REFERENCE_VOLTAGE) / self.VOLTAGE_REDUCTION_PER_DEGREE
        self.analogValue = round(temperature,1)            
        return self.read()
    
    def read(self):
            return self.analogValue

if __name__ == "__main__":
    print("No local diagnostics for this temperature sensor have been implemented.")
