from collections import deque

class LIFOAverage:
    def __init__(self, maxLength = 10):
        self.max_length = maxLength
        self.values = []

    def add_value(self, value):
        self.values.append(value)
        if len(self.values) > self.max_length:
            self.values = self.values[-self.max_length:]

    def get_average(self):
        return sum(self.values) / len(self.values) if self.values else 0
