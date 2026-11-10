import matplotlib.pyplot as plt

# Global counters
count1 = 0
count2 = 0
count3 = 0
# Function 1: Linear Recursion
def f1(n):
    global count1
    count1 += 1

    if n <= 1:
        return 1

    return f1(n - 1)

# Function 2: Binary Recursion
def f2(n):
    global count2
    count2 += 1

    if n <= 1:
        return 1

    return f2(n - 1) + f2(n - 1)


# Function 3: Fibonacci Recursion
def f3(n):
    global count3
    count3 += 1

    if n <= 2:
        return 1

    return f3(n - 1) + f3(n - 2)


# Input values
values = [5, 10, 15, 20, 25]

calls1 = []
calls2 = []
calls3 = []

print("N\tF1 Calls\tF2 Calls\tF3 Calls")

for n in values:

    # Reset counters
    count1 = 0
    count2 = 0
    count3 = 0

    # Call recursive functions
    f1(n)
    f2(n)
    f3(n)

    # Store function call counts
    calls1.append(count1)
    calls2.append(count2)
    calls3.append(count3)

    print(n, "\t", count1, "\t\t", count2, "\t\t", count3)


# Plot comparison graph
plt.figure(figsize=(10, 6))

plt.plot(values, calls1, marker='o', label='F1 - Linear Recursion')
plt.plot(values, calls2, marker='s', label='F2 - Binary Recursion')
plt.plot(values, calls3, marker='^', label='F3 - Fibonacci Recursion')

plt.xlabel("Input Size (n)")
plt.ylabel("Number of Function Calls")

plt.title("Comparison of Recursive Function Calls")

plt.legend()
plt.grid(True)

plt.show()