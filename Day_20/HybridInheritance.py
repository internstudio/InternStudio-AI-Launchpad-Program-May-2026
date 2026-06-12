class Father:
    def f1(self):
        print("This is function 1")


class Mother:
    def f2(self):
        print("This is funciton 2")


class Child1(Father,Mother):
    def f3(self):
        print("This is the function 3 from Child 1")


class Child2(Father,Mother):
    def f3(self):
        print("This is the function 3 from Child 2")


c1 = Child1()
c1.f1()
c1.f2()
c1.f3()


print("="*20)
c2 = Child2()
c2.f1()
c2.f2()
c2.f3()

# Mother                       Father
    # |                             |
       # Child1        Child2  