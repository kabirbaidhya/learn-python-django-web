n = 0
sum = 0

# Calculate the sum of 5 numbers entered by user
while n < 5:
    value = input('Enter Number %s: ' % (n + 1))
    sum = sum + float(value)
    n += 1

print('Sum = %.2f' % sum)

