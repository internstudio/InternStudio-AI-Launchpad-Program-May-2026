class Father:
    def f1(self):
        print("This is function 1")


class Mother:
    def f2(self):
        print("This is funciton 2")


class Child(Father,Mother):
    def f3(self):
        print("This is the function 3")


c1 = Child()

c1.f1()
c1.f2()
c1.f3()

f1 = Father()
f1.f1()
f1.f2()