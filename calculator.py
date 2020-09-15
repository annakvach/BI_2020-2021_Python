print('Hello! This is a calculator-program. ')
print('It has two modes - UNI for operations (!, ln) and ')
print('BI for operations (+, -, *, /, ^(it is exponentiation))', )
print()

import math  # import math library for 2 "unitary" operations


# for type control
def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


mode = input('Chose mode (UNI/BI): ')
# UNI for "unitary" operations
if (mode == "UNI"):
    print('You can calculate the factorial(!), natural logarithm(ln)  .')
    operator = input('Enter one operator (!, ln): ')
    input_1 = input('Enter number: ', )  # input anything

    if (isDigit(input_1)):  # chek is "anything" a number?
        num_1 = float(input_1)
        if (operator == "!"):
            print("Result = ", math.gamma(num_1 + 1))
        elif (operator == "ln"):
            if (num_1 > 0):
                print("Result = ", math.log(num_1))
            else:
                print("Logarithm not defined. Number should be > 0")
        else:
            print("Sorry! Invalid operator")
    else:
        print("Sorry! Invalid type of number. Try again with number.")

# BI for "binary" operations
elif (mode == "BI"):
    input_1 = input('Enter first number: ', )  # input anything
    operator = input('Enter one operator (+, -, *, /, ^): ')
    input_2 = input('Enter second number: ', )  # input anything

    if ((isDigit(input_1)) and (isDigit(input_2))):  # chek is "anything" a number?
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

else:
    print('Sorry! Invalid mode. Try again - UNI or BI.')
