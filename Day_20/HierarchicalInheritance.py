class Parent:
 def display(self):
  print("Parent Class")
  
class Child1(Parent):
 def display1(self):
  print("Parent Class")
  
class Child2(Parent):
 def display2(self):
  print("Parent Class")


c1 = Child1()
c1.display()
c1.display1()

c2 = Child2()
c2.display()
c2.display2()
