def power(x, n):
    assert n >= 0 and type(n) == int, "n must be positive integer"
    if n == 0:
        return 1
    return x * power(x, n - 1)

print(power(10, 2))