class Parent:
    def showResult(self):
        print("Those are the result")

    counter = 10

class Child(Parent):
    def display(self):
        print("This is the display method")
        print(self.counter)

    

c1 = Child()
c1.showResult()
c1.display()
