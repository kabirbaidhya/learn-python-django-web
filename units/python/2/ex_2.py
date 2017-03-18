# Input the equation in y = mx + c form.
equation = input('Equation: ')

# 'y', 'mx +c'
rhs = equation.split('=')[1]

# 'mx', 'c'
parts = rhs.split('+')

# Parse out the values of m & c
m = parts[0].replace('x', '').strip()
c = parts[1].strip()

# Print them out
print('Slope of line: {}'.format(m))
print('Y-Intercept: {}'.format(c))
