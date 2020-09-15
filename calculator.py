print('Hello! This is a calculator-program. ')
print('It has two modes - uni for operations (!, ln) and ')
print('bi for operations (+, -, *, /, ^(it is exponentiation))',)
print()

import math #import math library

mode = input('Chose mode (uni/bi): ')
# uni for "unitary" operations
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



#bi for "binary" operations
elif (mode == "bi"):
    input_1 = input('Enter first number: ',)
    operator = input('Enter one operator (+, -, *, /, ^): ')
    input_2 = input('Enter second number: ',)

    if ((input_1 is float) and (input_2 is float)):
        num_2 = float(input_2)
        num_1 = float(input_1)

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
        elif (operator == "^"):
            result = num_1 ** num_2
            print("Result = ", result)
    else:
        print("Sorry! Invalid type of numbers (one or both). Try again with two numbers.")

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
    print('Sorry! Invalid mode. Try again - uni or bi.')
