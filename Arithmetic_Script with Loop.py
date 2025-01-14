cont = ''
while(cont!='stop'):
    num_1 = int(input("Enter the Number 1: "))
    num_2 = int(input("Enter the Number 2: "))
    sym_1 = input("Select 1: (+ - * / **) : ")

    if (sym_1 == '+'):
        opr = num_1 + num_2

    elif (sym_1 == '-'):
        opr = num_1 - num_2

    elif (sym_1 == '*'):
        opr = num_1 * num_2

    elif (sym_1 == '/'):
        opr = num_1 / num_2

    elif (sym_1 == '**'):
        opr = num_1 ** num_2
    else:
        opr = "Sorry! Invalid option, Please Select the options from the menu"

    print(opr)
    cont = input("Do you wish to continue or stop?:").lower()

print("Tata and Bye!")