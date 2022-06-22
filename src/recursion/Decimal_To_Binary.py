def toBinary(n):
    assert type(n) == int, "n must be integer"

    minus = 1
    if n < 0:
        n *= -1
        minus = -1

    if n == 0 or n == 1:
        return n
    return n % 2 + toBinary(n // 2) * 10 * minus

print(toBinary(16))