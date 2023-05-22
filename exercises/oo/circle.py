# circle.py

import math

class Circle:
    num_instances = 0 # class attribute
    def __init__(self, radius):
        Circle.num_instances += 1
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        self._radius = value

    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 2)
