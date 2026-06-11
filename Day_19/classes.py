# syntax 
# class class_name


# class creation
class Student:

    def __init__(self,name):
        print("Object Created",name)


    def greetUser(self):
        print("Hey! Welcome to OOP")

s1  = Student("S1")
s2  = Student("S2")
s3  = Student("S3")

# Instance Variables

class Student:
    def __init__(self, nameInput, ageInput):
        self.name = nameInput
        self.age = ageInput
    
    def sayHello(self):
        print("Hello",self.name)

s1 = Student("Rahul", 20)
print(s1.name)
print(s1.age)
s1.sayHello()


s2 = Student("Vivek",30)
print(s2.name)
print(s2.age)
s2.sayHello()



# Class Variables

class Student:
    def __init__(self, nameInput, ageInput):
        self.name = nameInput
        self.age = ageInput
    
    # class variable
    college = "COE Pune"
    
    def sayHello(self):
        print("Hello",self.name)

s1 = Student("Rahul", 20)
print(s1.name)
print(s1.age)
print(s1.college)
s1.sayHello()

print("*="*30)

s2 = Student("Vivek",30)
print(s2.name)
print(s2.age)
s2.college = "PICT"
print(s2.college)
s2.sayHello()


s3 = Student("V",2)
print(s3.college)


# Encapsulation
class BankAccount:
 def __init__(self):
    # public variable
    self.name = "Account Holder name"

    # protected
    self._accountNo = 123456789090

    # private
    self.__balance = 100000

 def show_balance(self):
    print(self.__balance)

 def set_balance(self,balance):
    self.__balance = balance

acc = BankAccount()
acc.show_balance()
acc.set_balance(30000)
acc.__balance = 90
acc.show_balance()