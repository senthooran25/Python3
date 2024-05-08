# from abc import ABC, abstractmethod
#
# class Car(ABC):
#     def __init__(self,name):
#         self.name = name
#
#     def description(self):
#         print("This the description function of class car.")
#
#     @abstractmethod
#     def price(self,x):
#         pass
# class new(Car):
#     def price(self,x):
#         print(f"The {self.name}'s price is {x} lakhs.")
# obj = new("Honda City")
#
# obj.description()
# obj.price(25)

# First product method.
# Takes two argument and print their
# product


def product(a, b):
	p = a * b
	print(p)

# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
	p = a * b*c
	print(p)

# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method
product(4, 5, 5)
