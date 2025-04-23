num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operation = input("Enter operation (+, -, *, /): ")
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def modulus(x, y):
    return x % y

def exponent(x, y):
    return x ** y

def floor_division(x, y):
    return x // y

def calculator(num1, num2, operation):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)
    elif operation == '%':
        return modulus(num1, num2)
    elif operation == '**':
        return exponent(num1, num2)
    elif operation == '//':
        return floor_division(num1, num2)
    else:
        return "Invalid operation"