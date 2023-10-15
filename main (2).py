#python program to create Bankaccount class
#with both a deposit() and a withdraw() function
class Bank_Account:

  def __init__(self):
    self.balance = 0
    print("Hello!!! welcome to the deposit & withdrawal machine")

  def deposit(self):
    amount = float(input("Enter the amount to be deposited: "))
    self.balance += amount
    print("\n Amount Deposited:", amount)

  def withdraw(self):
    amount = float(input("Enter the amount to be withdrawn: "))
    if self.balance >= amount:
      self.balance -= amount
      print("\n you withdrew:", amount)
    else:
      print("\n Insufficient balance")

  def display(self):
    print("\n Net available Balance= ", self.balance)


#Driver code
#creating an object of values
s = Bank_Account()
#calling functions with that class object
s.deposit()
s.withdraw()
s.display()
