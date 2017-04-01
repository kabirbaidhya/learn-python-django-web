import test # Import the test module here


def main():
    n = int(input('Enter a Number: '))

    series = test.fibo(n)
    print('Fibonacci Series up to {}: \n {}'.format(n, series))
    print('Factorial of {}: {}'.format(n, test.factorial(n)))


main()
