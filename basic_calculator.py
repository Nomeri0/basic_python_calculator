def valid_number(number):
    while True:
        user_input = input(number)
        try:
            return float(user_input) # try converting user_input to a float 
        except ValueError:
            print('Invalid number, please enter a valid number.') # print if user input an invalid number

# input first number
num1 = valid_number('Please enter the 1st number: ')

# input operator
operator = input('Enter an operator (+, -, *, /): ')

# input second number
num2 = valid_number('Please enter the 2nd number: ')

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
else:
    result = 'Invalid operator'
    
print(f'The result is: {result}')
