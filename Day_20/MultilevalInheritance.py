class GrandPrarent:
    def property(self):
        print("Land")

class Parent(GrandPrarent):
    def newProperty(self):
        print("This is new property")


class Child(Parent):
    def childProperty(self):
        print("Bike..")


p1 = Parent()
p1.property()
p1.newProperty()


c1 = Child()
c1.property()
c1.newProperty()
c1.childProperty()