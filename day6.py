# OOP - Object Oriented Programming
# 2 Wheeler - Class - blueprint - definition
# it needs to have - Property
    # 2 wheels - Wheels
    # 1 Frame - Frame
    # 2 brakes - brack
    # Brand - 
    # model name - 
# it can perform - Actions/Fuctions/Methods
    # move from 1 place to other

# From a class, we create an Object - Instance of a class
# BSA SLR - Object
# Hero Splendor - Object
# Honda Shine - Object

class Employee: # Class Name needs to be represent starting with a Capital letter
    def __init__(self, name, empID, mobile, emailID): # __init__ = built in function name, which initializes, when the class is called
        self.name = name # Property
        self.empID = empID
        self.mobile = mobile
        self.emailID = emailID

    def introduce(self): # Method
        print("My name is {} with an Employee ID of {}!".format(self.name,self.empID))

emp1 = Employee('Hiran',123, 8825410600, 'hrb@mjit.in') # Object Creation
emp2 = Employee('HRB',354, 8825410600, 'hrb@mjit.in') # Object Creation
emp3 = Employee('Lalith',8798159, 8825410600, 'hrb@mjit.in') # Object Creation
emp4 = Employee('Saan',745896, 8825410600, 'hrb@mjit.in') # Object Creation
emp1.introduce()
emp2.introduce()
emp3.introduce()
emp4.introduce()

class BankAccount:
    __balance = None # deifintion of private property
    def __init__(self, account_holder, account_number, __balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = __balance # Private

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print("Amount of Rs. {} added successfully. Current available balance is Rs. {}".format(amount, self.__balance))

    def withdraw(self, amount):
        self.__balance = self.__balance - amount
        print("Amount of Rs. {} withdrawn successfully. Current available balance is Rs. {}".format(amount, self.__balance))
    
    def check_balance(self):
        print("Current available balance is Rs. {}".format(self.__balance))
    
    def pass_balance(self): # Public Method
        return self.__balance # returning a private property

account1 = BankAccount("Lalith", 111222333, 9000)
account2 = BankAccount("HRB", 222333444, 7000)
account3 = BankAccount("Saan", 333444555, 12000)

account1.deposit(500)
account2.withdraw(200)
account3.check_balance()
account1.withdraw(100)
account1.check_balance()
print(account1.account_holder) # Access a public property
# print(account1.__balance) # accessing a Private property


# Inhertance - Parent to Child relationship. Creation of a child class from a parent class
# polymorphism - redife a method of child class from the actual parent class's method - In python, we only have method overriding
# Encapsulation - securing. defining what is public, what is private and what is protected - This is called as access Specifiers - protected - _variable, Private - __variable
# Public - accessed from anywhere or also from main program
# Protected - will not list while asking, but can be accessed from anywhere with _
# Private - cannot be accessed out of the class
# Abstaction - To define a structure lik emandate property, method etc., Python do not have abstraction by default, but can be acheived with abc module

class SavingsAccount(BankAccount): # SavingsAccount is a child of BankAccount class - Inheritance
    __balance = None
    def __init__(self, account_holder, account_number, __balance, interest):
        super().__init__(account_holder, account_number, __balance)
        self.__balance = __balance
        self.interest = interest
  
    # Method Overriding    
    def check_balance(self):
        bal = self.pass_balance() # Grabbing the Private property of parent by accessing via public method
        self.__balance = bal + (bal*(self.interest/100))
        print("Current available balance is Rs. {}".format(self.__balance))

saving1 = SavingsAccount("Abi", 789456123, 5000, 5)
saving1.deposit(500)
saving1.check_balance()

# Task:
"""
Class Vehicle - make, model, year - make as private
Child Car, Bike, electricVehicle
car - doors
actions/methods - add relavant methods
Handle Inheritance, Encapulation (Public, Private & Protected), Method Overriding
"""