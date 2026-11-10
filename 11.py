count = 0
  
def karatsuba(x, y):
    global count
    count += 1
    # Base condition
    if x < 10 or y < 10:
        return x * y

    # Find number of digits
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Divide the numbers
    power = 10 ** m

    a = x // power
    b = x % power

    c = y // power
    d = y % power

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ab_cd = karatsuba(a + b, c + d)


    result = (ac * 10 ** (2 * m)) + \
             ((ab_cd - ac - bd) * power) + bd

    return result

x = 12345678
y = 87654321


karatsuba_result = karatsuba(x, y)


conventional_result = x * y


print("First Number:", x)
print("Second Number:", y)

print("\nKaratsuba Product:", karatsuba_result)

print("Conventional Product:", conventional_result)

print("Both Results Equal:", karatsuba_result == conventional_result)

print("Total Recursive Multiplication Calls:", count)
