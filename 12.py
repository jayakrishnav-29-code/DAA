# Global counter
count = 0

# Divide and Conquer Multiplication
def divide_conquer(x, y):
    global count
    count += 1

    # Base condition
    if x < 10 or y < 10:
        return x * y

    # Find number of digits
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Divide numbers into two parts
    power = 10 ** m

    a = x // power
    b = x % power

    c = y // power
    d = y % power

    # Recursive multiplication (4 calls)
    ac = divide_conquer(a, c)
    ad = divide_conquer(a, d)
    bc = divide_conquer(b, c)
    bd = divide_conquer(b, d)

    # Combine results
    result = (ac * 10 ** (2 * m)) + \
             ((ad + bc) * power) + bd

    return result

# Main program
x = 12345678
y = 87654321

# Divide and Conquer multiplication
dc_result = divide_conquer(x, y)

# Conventional multiplication
normal_result = x * y

# Display results
print("First Number:", x)
print("Second Number:", y)

print("\nDivide and Conquer Product:", dc_result)

print("Conventional Product:", normal_result)

print("Both Results Equal:", dc_result == normal_result)

print("Total Recursive Multiplication Calls:", count)
