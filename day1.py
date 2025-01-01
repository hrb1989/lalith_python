# To Comment a single line
# Comments will not get executed
'''
This is a multi line comment
This is a multi line comment
This is a multi line comment
This is a multi line comment
This is a multi line comment
This is a multi line comment
'''
"""
This is also a multi line comment
This is also a multi line comment
This is also a multi line comment
This is also a multi line comment
This is also a multi line comment
This is also a multi line comment
"""
# To execute - python day1.py
# output - print() - inbuilt function of Python
# Text/String - "" or ''
# numbers/integers/float/double - no "" or '' required
print("Hello Lalith!") 
# print "Hello Lalith!" - Older version of Python 2.x
# Automatic Language - Auto Identifies the Data Type of the variable/value - literals
# Inbuilt functions - print() type() count() len()
print(type("Hello Lalith!")) # String
print(type(101)) # int
print(type(101.65)) # float
print(type(True)) # boolean
print(type([1,2,3])) # list - []
print(type((1,2,3))) # tuple - ()
print(type({1,2,3})) # set - {}
print(type({"name":"Hiran","Mobile":8825410600,"Email":"info@mji.in"})) # dictionary - {}

# data types/literals - string, int, float, boolean, list, tuple, set, dictionary

# Declation of variable - Declaration will always happen with definition

name = "Hiran"
mobile = 8825410600
isActive = True
vehiclesTuple = ("bike", "car") # bike is an item, car is an item
vehiclesList = ["bike", "car"] # bike is an item, car is an item
vehiclesSet = {"bike", "car"} # bike is an item, car is an item
vehiclesDict = {"bike":"Avenger 220 Cruice", "car":"Tata Altroz"} # bike is a key & Avenger 220 Cruice is a value; key: value pair

print(name)
print(type(mobile))
print(len(vehiclesTuple)) # len() will return or provide number of items in an interable - tuple, list, set or dictionary
print(len(vehiclesDict))
print(vehiclesDict)

num1 = 10
num2 = 20
sum = num1 + num2 # Expression or Operation or manipulation
print(sum)

print(len(name)) # len() here gives number of characters