# list - iterable, mutable, sequence - index
# list - add, update, remove, delete...
list_1 = [74,25,44,85]
list_2 = list((74,45,84,79))
print(list_1)
print(list_2)

# list inbuilt function - 
list_1.append(58) # to add at last
print(list_1)
list_1.insert(1, 33) # to add at specific index
print(list_1)
list_1.pop() # remove the last
print(list_1)
list_1.reverse() # reverse the list
print(list_1)
list_1.sort() # sort the items in ascending
print(list_1)
list_1.sort(reverse=True) # sort the items in decending
print(list_1)

print(range(5)) # this will create a 

#dictionary - iterable, mutable, sequence - Index
# dictionary - key-value pair
# dictionart - all add, update, remove & access
dict_1 = {
    'name': "Hiran Ram Babu",
    'mobile': 8825410600
}

dict_2 = dict(name="HRB",mobile=882541060)

print(dict_1)
print(dict_2)

print(dict_1.items()) # Returns the items
print(dict_1.values()) # returns only values - RHS
print(dict_1.keys()) # returns only keys - LHS
# print(dict_1.fromkeys('name','HRB'))
print(dict_1)
print(dict_1.get('name')) # returns specified value for a key
dict_1.pop('name') # it removes specific key value
print(dict_1)
dict_1.popitem() # this removes the last item
print(dict_1)

# Statements - if, if else, ladder - if elif, nested - if if else else
# statement - conditions to check if it is True or False
# statement - if true, it will execute the block, else it will go to next block

# condition - operators - Relational operators
# > < >= <= != ==
# 1 > 2 - Greater Than ? No - False
# 1 >= 1 - Greater Than or Equals to ? Yes - True
# 1 == 1 - Equals to ? Yes - True

if (5>3):
    # block start - indentation (space at the start of the line) is there
    print("5 is bigger than 3")
# syntax
# if(condtion):
#   block

if (5>6):
    # block start - indentation (space at the start of the line) is there
    print("5 is bigger than 3")
    # Block will execute only if the condition returns true

# if else
if (5>6):
    # block start - indentation (space at the start of the line) is there
    print("5 is bigger than 3")
else:
    # on failure of condition, it enters else block (if available)
    print("5 is not bigger than 6")

# Ladder
if (5>6):
    print("5 is bigger")
elif (5<6):
    print("5 is smaller")
elif (5==5):
    print("both are equal")
else:
    print("Sorry")

# Nested
if(5>3):
    if(5>4):
        print("5 is greater than 3 & 4")

# membership operators -  in, not in - returns true or false
print(45 in list_2) # it checks if 45 is available in list_2 items
print(84 not in list_2)

# logical operator - and, or, not
# and - both condtions needs to be true
# or - any one condition needs to be true
# not - condition must be false
# when I need to check more than 1 condition, logical operator is used
if (5 > 3 and 5 > 4):
    print("5 is greater than 3 & 4")

if (5 > 3 or 2 > 3):
    print("either 5 is bigger than 3 or 2 is greater than 3")
if (not False):
    print("It works!")

# identity operator - is, is not
var_1 = "Hiran"
var_2 = "hiran"
var_3 = "HRB"

print(var_1 is var_2)
print(var_1 is not var_3)

# bitwise operator - &, |, ^, ~, <<, >>

# AND
a = 7 # 111
b = 4 # 100
# a&b # 100
print("a & b = ", a & b) # resutl will be 4

# OR
a = 7 # 111
b = 4 # 100
# a|b # 111
print("a | b = ", a | b) # resutl will be 7

# XOR
a = 7 # 111
b = 4 # 100
# a^b # 011
print("a ^ b = ", a ^ b) # resutl will be 3

# NOT
b = 4 # 100
# ~b  # 011
print("a ~ b = ", ~b) # resutl will be -5 # check on this again

# Right Shift
a = 10 # 1010
# a >> 1 # 0101 = 5
print("a >> 1 = ", a >> 1)

# Left Shift
b = 3 # 0011
# b << 1 # 0110 = 6
print("b << 1 = ", b << 1)

'''
simple scripts:
1. collect 2 input user
2. 1 extra input for calculator operation (+, -, *, /, %)
2. validate if the value has number
3. Calculator app
'''