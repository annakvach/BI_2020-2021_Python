
print('Hello! This is a calculator-program. ')
print('It has two modes - uni for unitary operations and bi for binary operations ',)
print()
mode = input('Chose mode (uni/bi): ')

import math #import library

if (mode == "uni"):
    print('You can calculate the factorial, .')
    operator = input('Enter operator (!): ')
    num_2 = float(input('Enter number: ',))

    if (operator == "!"):
        result = 1
        for i in range(2, int(num_2 + 1)):
            result *= i
        print("Result = ", result)

elif (mode == "bi"):
    num_1 = float(input('Enter first number: ',))
    operator = input('Enter one operator (+, -, *, /, **): ')
    num_2 = float(input('Enter second number: ',))

    if (operator == "+"):
        result = num_1 + num_2
        print("Result = ", result)
    elif (operator == "-"):
        result = num_1 - num_2
        print("Result = ", result)
    elif (operator == "*"):
        result = num_1 * num_2
        print("Result = ", result)
    elif (operator == "/"):
        if (num_2 == 0):
            print('Error! You cannot divide by Zero!')
        else:
            result = num_1 / num_2
            print("Result = ", result)
    elif (operator == "**"):
        result = num_1 ** num_2
        print("Result = ", result)












