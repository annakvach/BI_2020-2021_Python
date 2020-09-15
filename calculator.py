print('Hello! This is a calculator-program. ')
print('It has two modes - uni for unitary operations (!, ln) and ')
print('bi for binary operations (+, -, *, /, **)',)
print()

import math #import math library

mode = input('Chose mode (uni/bi): ')
# uni for unitary operations
if (mode == "uni"):
    print('You can calculate the factorial(!), natural logarithm(ln)  .')
    operator = input('Enter one operator (!, ln): ')
    num_2 = float(input('Enter number: ',))

    if (operator == "!"):
        print("Result = ", math.gamma(num_2 + 1))
    if (operator == "ln"):
        if (num_2 > 0):
            print("Result = ", math.log(num_2))
        else:
            print("Logarithm not defined. Number should be > 0")



#bi for binary operations
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

#bi for binary operations
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

else:
    print('invalid first number or second number')
