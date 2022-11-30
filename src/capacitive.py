# Capacitive Water Sensor
#
from machine import Pin, ADC
from common import scale_value

class Capacitive:

    DIGITAL = 0
    ANALOG = 1
    SENSOR_MAX = 2 ** 16                  # ADC high with no moisture
    DIGITAL_THRESHOLD = 30
    
    sensorBaseline = SENSOR_MAX        # min observed when in water (dynamically updated)

    digitalValue = None

    analogPin = None
    analogValue = None
    analogSensor = None
    
    def __init__(self, analogPin):
        self.analogPin = analogPin        
        self.setup()

    def setup(self):                    
        if self.analogPin is not None:
            self.analogSensor = ADC(Pin(self.analogPin))                    

    def update(self):
        if self.analogPin is not None:
            reading = self.analogSensor.read_u16()
            self.sensorBaseline = min(self.sensorBaseline, reading)    # ensure if we drop further have new ref
            scaled = scale_value(reading, self.sensorBaseline, self.SENSOR_MAX, 0, 100)
            self.analogValue = round(100 - scaled)
            self.digitalValue = self.analogValue > self.DIGITAL_THRESHOLD
            
        return self.read()
    
    def read(self):
            return (self.digitalValue, self.analogValue)        

if __name__ == "__main__":
    print("No local diagnostics for this sensor have been implemented.")
