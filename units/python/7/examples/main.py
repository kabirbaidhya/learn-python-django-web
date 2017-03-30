import util # Import the util module here

def main():
    n = int(input('Enter a Number: '))

    series = util.fibo(n)
    print('\nFibonacci Series up to {:d}:\n{}'.format(n, series))
    print('\nFactorial of {:d}:\n{}'.format(n, util.factorial(n)))

main()
