while True:
    a = float(input('First Number: '))
    b = float(input('Second Number: '))

    try:
        result = a / b
        print('Result = {}'.format(result))

    except ZeroDivisionError:
        print('Error: Division by Zero')

    try_again = input('\nTry Again (Y/N)? ')

    # If the user doesn't want to try again exit the loop.
    if try_again.upper() != 'Y':
        break

    print()

# Program will exit finally
print('Good Bye!')

