# Print Fibonacci series upto n
a = 0
b = 1
n = 25

while a < n:
    print(a)
    (a, b) = (b, a + b)


