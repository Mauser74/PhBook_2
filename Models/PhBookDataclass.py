from dataclasses import dataclass

@dataclass
class Rectangle:
    width: float
    height: float

    def area(self):
        return self.width * self.height