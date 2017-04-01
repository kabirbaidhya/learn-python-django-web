import sys

def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

print('Command line arguments:', sys.argv)

 
if __name__ == '__main__':
    n = int(sys.argv[1])
    fib(n)
