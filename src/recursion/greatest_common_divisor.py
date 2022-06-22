def gcd(a, b):
    assert type(a) == int and type(b) == int, "error"

    if a < 0: a *= -1
    if b < 0: b *= -1

    if a < b:
        temp = a
        a = b
        b = temp
        
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))