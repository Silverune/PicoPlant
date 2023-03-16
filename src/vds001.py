# VDS001 Water Sensor
#

from machine import Pin, ADC
from common import scale_value

class VDS001:

    DIGITAL = 0

    digitalPin = None
    digitalValue = None
    digitalSensor = None
    
    def __init__(self, digitalPin):
        self.digitalPin = digitalPin
        self.setup()

    def setup(self):
        
        if self.digitalPin is not None:
            self.digitalSensor = Pin(self.digitalPin, Pin.IN)
                    
    def update(self):
        if self.digitalPin is not None:            
            self.digitalValue = not(self.digitalSensor.value())
            
        return self.read()
    
    def read(self):
            return (not self.digitalValue, 0)        

if __name__ == "__main__":
    print("No local diagnostics for this sensor have been implemented.")
