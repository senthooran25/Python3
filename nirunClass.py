class Car:
    def __init__(self, name):
        self.name = name

    def Drive(self):
        print(f"{self._name} can drive fast")
    def Brake(self):
        print(f"{self._name} can brake ")

class Audi(Car):
    def Seated(self):
        print(f"{self.__name} has leather seated")

class Honda(Car):
    def Seated(self):
        print(f"{self._name} has NON leather seated")

class Boat():
    def Seated(self):
        print(f"{self.name} has NON leather seated")



b = Boat()
b.Seated()