# Python Program for Arithmetic Operations:
def add_numbers(num1, num2):
    return float(num1) + float(num2)

def subtract_numbers(num1, num2):
    return float(num1) - float(num2)

def multiply_numbers(num1, num2):
    return float(num1) * float(num2)

def divide_numbers(num1, num2):
    return float(num1) / float(num2)

def perform_operations(num1, num2):
    # Display the sum
    print('The sum of {0} and {1} is {2}'.format(num1, num2, add_numbers(num1, num2)))

    # Display the substraction
    print('The difference of {0} and {1} is {2}'.format(num1, num2, subtract_numbers(num1, num2)))

    # Display the multiplication
    print('The product of {0} and {1} is {2}'.format(num1, num2, multiply_numbers(num1, num2)))
          
    # Display the division
    print('The division of {0} and {1} is {2}'.format(num1, num2, divide_numbers(num1, num2)))

if __name__ == '__main__':
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')

    # Perform operations recursively
    perform_operations(num1, num2)

# Output:
# Enter first number: 20
# Enter second number: 10
# The sum of 20 and 10 is 30.0
# The difference of 20 and 10 is 10.0
# The product of 20 and 10 is 200.0
# The division of 20 and 10 is 2.0