
# Method overriding
class Animal:
    def sound(self):
        print("Animal Sound")

    def __init__(self):
        print("This is the constructor of Animal class")

class Cat(Animal):
    def sound(self):
        print("Meow")
    super()

class Dog(Animal):
    def sound(self):
        print("Bark")


a = Animal()
a.sound()

a = Cat()
a.sound()

a = Dog()
a.sound()