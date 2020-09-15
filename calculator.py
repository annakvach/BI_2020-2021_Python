
print('Hello! This is a calculator-program. ')
print('You can calculate the addition, subtraction, multiplication, division for two numbers.')
print('')
num_1 = float(input('Enter one number: ',))
operator = input('Enter one operator (+, -, *, /): ')
num_2 = float(input('Enter one number: ',))


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



