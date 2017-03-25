a = int(input('First Number: '))
b = int(input('Second Number: '))

try:
    result = a / b
except ZeroDivisionError:
    print('Error: Division by Zero')

