# Loops: - Perform same operation, several times
# Loops can be traiggered with definite elements and indefinite elements
# Predefined Iterable - list, set, tuple, dict, range() - Definte Elements - Known count of items or len(iterable)
# user will provide input/ unkown count of items
# for, while
# for - known/definite elements - Very less probability for infinite loop
# for temp in iterable:
#     statement/operation within the for block
list_1 = [10,25,44,35,688]
print(len(list_1))

print("Loop Start!")
for item in list_1:
    if (item % 2 == 0):
        print(item,"is an Even Number")
    else:
        print(item,"is a Odd Number")
print("Loop Over!")

# while - known/unknown/definite/indefinite elements - High probability for infinite loop
# while - we need to write some operation/statement, which will get fails in some case
# while (condition is true):
#     statement/operation within the while block

# Index - iterable[index]
# Index number will always start from 0
print(list_1[2])

item = 0
list_2 = [2,4,6,8,10]
print("Loop Start!")
while (list_2[item] % 2 == 0):
    print(list_2[item],"is an Even Number")
    item = item + 1
    if item >= len(list_2):
        break # To Manually Make the loop to exit
print("Loop Over!")

# Python do not have do while loop
# implement do while loop alike with while(True) and if statement
list_2 = [5,4,6,8,10]
item = 0
# infinte
while(True):
    # print("Infinite loop")
    print(list_2[item],"is an Even Number")
    item = item + 1
    if item >= len(list_2):
        break # To Manually Make the loop to exit
    if (list_2[item] % 2 == 0):
        continue
    else:
        break

# While with indefinite elements

# Incrementation - Ascending
repetation = int(input("Enter how many times to repeat: "))
temp = 1
while (temp <= repetation):
    print(temp,"print")
    temp = temp + 1 # temp += 1

# Decrementation - Descending
repetation = int(input("Enter how many times to repeat: "))
temp = repetation
while (temp > 0):
    print(temp,"print")
    temp = temp - 1 # temp -= 1