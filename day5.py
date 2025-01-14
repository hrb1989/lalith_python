# range() - return range of elements or items
# ex., range(5), range(0,5)
# range(5) - range(0,5) - start from 0 and return 5 elements - total it returns 5 elements
# range starts always from 0

# for temp in range(5): # 0,1,2,3,4
#     print(temp)

# for temp in range(1,5): # 1,2,3,4 - return only 4 elements
#     print(temp)

# for temp in range(4,5): # 4 - return only 1 element
#     print(temp)

# # definite loop
# for temp in range(5): # this loop will execute exactly 5 times
#     num_1 = int(input("Enter the Number 1: "))
#     num_2 = int(input("Enter the Number 2: "))
#     sym_1 = input("Select 1: (+ - * / **) : ")

#     if (sym_1 == '+'):
#         opr = num_1 + num_2

#     elif (sym_1 == '-'):
#         opr = num_1 - num_2

#     elif (sym_1 == '*'):
#         opr = num_1 * num_2

#     elif (sym_1 == '/'):
#         opr = num_1 / num_2

#     elif (sym_1 == '**'):
#         opr = num_1 ** num_2
#     else:
#         opr = "Sorry! Invalid option, Please Select the options from the menu"

#     print(opr)

# Function - small snippet of code, which can be reused
# def functionName():
#   block

# called function
def my_function():
    print("Hey Lalith!")

# calling a function
my_function()

def my_func_1(name): # name is an argument
    print("Hey", name + '!')

my_func_1("Lalith") # Lalith is passing a value to the argument
my_func_1("Hiran")

# Definite args
# positional args
def sum_func(num_1, num_2): # Posisitional Args - num_1 is at position 0 and num_2 is at position 1
    print(num_1+num_2)

sum_func(5,8)
sum_func(8,2)
# sum_func(8,) # this will throw error as positional args are mandate

# keyword args
def diff_func(num_1, num_2):
    print(num_1-num_2)

diff_func(num_1=5, num_2=3) # Keyword args
# diff_func(num_1=5) #  this will throw error as Keyword args are mandate

# default args
def product_func(num_1=1, num_2=1): # we have defined the default values for each args as num_1=1, num_2=1
    print(num_1 * num_2)

product_func() # while calling a function, which has default value, args are not mandate
product_func(8)
product_func(8,5)

# function needs block statements as mandate
# to create a dummy or empty function, we use pass

def div_func():
    pass

# position only args
def func_1(num_1, num_2, /): # / in the args, make the args before that as position only args
    pass

func_1(2,3)
# func_1(num_1=2,num_2=3) # this will not work, as the func accepts only positionals

# keyword only args
def func_2(*,num_1, num_2): # * in the args, make the args after that as keyword only args
    pass

func_2(num_1=2,num_2=3) 
# func_2(2,3) # this will not work, as the func accepts only keywords

# positional args needs to be at first, later keyword args needs to be placed
# mixed args
def func_3(num_1, num_2, /, *, num_3, num_4):
    pass

func_3(7,8,num_3=9, num_4=7)

# indefinte args:
# arbitary args - *args - *variable

def func_4(*values):
    pass

func_4(1,2,3)
func_4(1)

# arbitary keyword args - **kwargs - **variable

def func_5(**name):
    if name['fname'] and name['lname']:
        print("The full name is",name['fname'], name['lname'])
    elif name['fname']:
        print("The full name is",name['fname'])
    elif name['lname']:
        print("The full name is",name['lname'])
    else:
        print("Please pass either fname or lname or both")

# func_5(fname='Hiran Ram Babu')
func_5(fname='Hiran Ram Babu', lname='Ontivillu')

######################################################################
# Ananymous function - unknown or unnamed function
# lambda - it is small, unnamed function
# it can accept any number of ards but only one expression, statement it returns
# sytax
# lambda args: expr
# lamba must return some value
doubling = lambda a : a*a
print(doubling(5))
print(doubling(2))
print(doubling(7))

summing = lambda a,b: a+b
print(summing(5,8))
print(summing(2,2))
print(summing(6,4))


# power of lambda with function:

def multing (num):
    return lambda a:a*num

doubler = multing(2) # allocate the multing num as 2
tripler = multing(3) # allocate the multing num as 3

print(doubler(2)) # allocate the multing a as 2
print(tripler(2)) # allocate the multing a as 2