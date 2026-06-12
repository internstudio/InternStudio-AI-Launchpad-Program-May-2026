class Bird:
 def sound(self):
  print("Bird Sound")
class Sparrow(Bird):
 def sound(self):
  print("Chirp")
class Crow(Bird):
 def sound(self):
  print("Caw")

b1 = Sparrow()
b2 = Crow()

b1.sound()
b2.sound()
