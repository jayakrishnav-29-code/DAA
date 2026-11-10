# Global counters
dc_count = 0
normal_count = 0
# Divide and Conquer Power
def dc(a, n):
    global dc_count
    dc_count += 1

    if n == 0:
        return 1

    half = dc(a, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return a * half * half


# Normal Recursive Power
def normal(a, n):
    global normal_count
    normal_count += 1

    if n == 0:
        return 1

    return a * normal(a, n - 1)


# Main program
values = [(2, 10), (3, 15), (5, 20)]

print("Base\tExponent\tResult\tDC Calls\tNormal Calls")

for a, n in values:

    # Reset counters
    dc_count = 0
    normal_count = 0

    # Divide and Conquer
    result1 = dc(a, n)

    # Normal Recursion
    result2 = normal(a, n)

    print(a, "\t", n, "\t\t", result1,
          "\t", dc_count, "\t\t", normal_count)
