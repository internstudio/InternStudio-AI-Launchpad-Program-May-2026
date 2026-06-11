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