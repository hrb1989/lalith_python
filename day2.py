# To store a value - we need a variable
# must start with alphabet and can contain numbers & _
# PEP 8 Standards
# Variable is snake_case num_1 input_value first_name; camelCase num1 inputValue firstName
# Not Recommended - SnakeCase inputvalue
# not allowed - 1num num.1 $inputvalue input
# always use meaningful variable names, avoid a, x, i, t

num_1 = 10 # value 10 is stored in variable num_1

# LHS - Variable; RHS - Value

# We cannot us Keywords - string which has inbuilt meaning in Python
# examples - for, if, else, elif, while, do, import, def, class
# variable can also be called as Identifiers
# values can also be called as Literals; ex., datatype = literal type
# string, integer, float, list, tuple, set & dictionary
# each datatype is a class in Python.


# Reassignment is possible
print(num_1)
print(type(num_1)) # <class 'int'>
num_1 = 44
print(num_1)
print(type(num_1)) # <class 'int'>
num_1 = "String"
print(num_1)
print(type(num_1)) # <class 'str'>

# multiple assignment is possible
num_2, str_3 = 7,"Hiran"
print(num_2)
print(str_3)

# input - inbuilt function - input()
input()

# input can be stored in an identifier or variable
input_value = input()

# to display/show the input, we can use print()
print(input_value)
print(type(input_value))

#  We can also share some instruction to the user for input()
input_value2 = input("Enter Value 2: ")
print(input_value2)

# by default the input() stores values as string literals.
print(type(input_value2))

# to change the datatype or literal type, we need to typecast
# typecast - conversion from 1 literal to another
# str(), int(), float(), list(), set(), tuple(), dict()

input_value3 = int(input("Enter Value 3: "))
print(input_value3)

print(type(input_value3))

str(num_1)
print(type(num_1))

# integers & float - Numbers
num_1 = 10
num_2 = 20
# Atithmetic opration with numbers
sum = num_1 + num_2 # expression to sum/add
diff = num_1 - num_2 # expression to subtract
mul = num_1 * num_2 # expression to multiply
div = num_1 / num_2 # expression to division - return quotient
sqr = num_1 ** 2 # expression to power of 2
# return the reminder
modulus = 5 % 2 # expression to find remainder - this will help to identify divisible

print(sum)
print(diff)
print(mul)
print(div)
print(sqr)
print(modulus)

# to access the inbuilt functions or properties we use . operator
int_check = num_1.is_integer() # this returns if this is true or false
print(str(int_check))

flo_1 = 10.5
int_check = flo_1.is_integer()
print(str(int_check))

# inbuilt function used for numbers is is_integer()

# strings
str_1 = "hiran Ram Babu"
print(str_1)

# string has inbuilt functions - we have too many for strings, below are few
print(str_1.capitalize()) # makes only the first letter capital
print(str_1.upper()) # complete capital case
print(str_1.lower()) # complete lower case
print(str_1.count('ra')) # returns how many such characters/string available
print(str_1.lower().count('ra')) # can use multiple inbuilt functions
print(str_1.split(' ')) # splits into list with space as a delimeter
print(str_1.strip()) # remove white spaces at the end & start

# we can join 2 strings - concat using + operator

str_2 = str_1 + str_3
print(str_2)

# iterables - list, tuple, set & dictionary
# Try these functions on iterables - CRUD operation - usally used in Database, but this applied to all iterables
    # add a new item - Create
    # access an individual item - Read
    # change an existing item - Update
    # delete an existing item - Delete
# mutable - we can change the value or modify the value - list, set & dictionary
# immutable - we cannot change the value or cannot modify the value - tuple
# tuple - immutable
tup_1 = (7,88,42)
tup_2 = tuple((7,88,42))
print(tup_1)
print(tup_2)

# we can perform the CRUD using inbuilt functions
# tuple - immutable, so we cannot add, modify or delete an item
# tuple - we can only perform read
# tuple - stores the information in as it is sequence, we can use that with index
# tuple inbuilt function - count & index
print(tup_1.count(2) ) # returns number of times a item is available
print(tup_1.index(88) ) # returns index of a value mentioned
# index - tuple(7,88,42) - index is 0,1,2
# index 0 - 7
# index 1 - 88
# index 2 - 42
# access the value with index with []
print(tup_1[1])
print(tup_1[0])

# set - iterable, mutable, it avoids duplicates and does not store in sequence; it will be so similart to list
# set - add an item, remove, read all items, by default removes duplicate
set_1 = {25,66,25,44,12,33}
print(set_1)

# inbuilt functions of set - add, pop & remove - also these make permanent change to the actual variable
set_1.add(88) # add a new item anywhere
print(set_1)
set_1.pop() # it tries to remove the first item
print(set_1)
set_1.pop()
print(set_1)
set_1.remove(12) # remove specifically an item with the mentioned value
print(set_1)