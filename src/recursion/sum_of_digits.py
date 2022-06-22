def sumOfDigits(n):
    assert n >= 0 and type(n) == int, "n must be positive integer"

    if n == 0:
        return 0
    return n % 10 + sumOfDigits(n // 10)

print(sumOfDigits(234))