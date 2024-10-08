def valid_number(number):
    while True:
        user_input = input(number)
        try:
            return float(user_input) # try converting user_input to a float 
        except ValueError:
            print('Invalid number, please enter a valid number.') # print if user input an invalid number

while True: #wrap the code in while loop to keep the calculator running

# input first number
    num1 = valid_number('Please enter the 1st number: ')

    # input operator
    operator = input('Enter an operator (+, -, *, /, ^): ')

    # input second number
    num2 = valid_number('Please enter the 2nd number: ')

    # Perform the calculation
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Cannot divide by zero'
    elif operator == '^':
        result = num1 ** num2
    else:
        result = 'Invalid operator'

    print (num1, operator, num2, '=', result)

    # Ask if user wants to perform another calculation
    continue_calculation = input('Do you want to perform another calculation? (y/n): ')

    if continue_calculation.lower() != 'y': #If the user input something other than 'y', exit calculator.
        print('Exiting calculator...')
        break