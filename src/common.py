# common - common constants across projects

# defines
HIGH = 1
LOW = 0

VOLTAGE = 3.3
_16BIT = pow(2, 16)
CONVERT_TO_VOLTS = VOLTAGE / _16BIT

def scale_value(value, in_min, in_max, out_min, out_max):
  scaled_value = (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
  return scaled_value

def map(value, in_min, in_max, out_min, out_max):  
  return scaled_value(value, in_min, in_max, out_min, out_max)

def print_bytearray(byte_array):
    print(' '.join(hex(byte) for byte in byte_array))