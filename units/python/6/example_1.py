n, sum = 0, 0

while n < 5:
    value = input('Enter Number %s: ' % (n + 1))

    try:
        value = float(value)
        sum = sum + value
        n += 1
    except ValueError:
        print('Invalid Input. Please enter a numeric value.\n')

print('\nSum = %.2f' % sum)

