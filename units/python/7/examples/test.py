def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


def fibo(n):
    result = []
    a, b = 0, 1

    while b < n:
        result.append(b)
        a, b = b, a+b

    return result

