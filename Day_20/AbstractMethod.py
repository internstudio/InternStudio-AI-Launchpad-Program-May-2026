from abc import ABC, abstractmethod
class Vehicle(ABC):
 @abstractmethod
 def start(self):
  pass
 
class Car(Vehicle):
 def start(self):
  print("Car Started with the key")


class Bike(Vehicle):
 def start(self):
  print("Bike Started with the cick")

b = Bike()
b.start()
