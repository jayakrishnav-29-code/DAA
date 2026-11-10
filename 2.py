
import time
import matplotlib.pyplot as plt

# Global counter
count = 0

# Iterative Fibonacci
def fib_iterative(n):
    a, b = 0, 1
    series = []

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series


# Recursive Fibonacci
def fib_recursive(n):
    global count
    count += 1

    if n <= 1:
        return n

    return fib_recursive(n - 1) + fib_recursive(n - 2)


# Input values
values = [5, 10, 15, 20, 25, 30]

iterative_times = []
recursive_times = []

print("N\tIterative Time\tRecursive Time\tRecursive Calls")

for n in values:

    # Iterative execution time
    start = time.perf_counter()
    iter_result = fib_iterative(n)
    end = time.perf_counter()
    

    iter_time = end - start
    iterative_times.append(iter_time)

    # Reset counter
    count = 0

    # Recursive execution time
    start = time.perf_counter()

    rec_result = [fib_recursive(i) for i in range(n)]

    end = time.perf_counter()

    rec_time = end - start
    recursive_times.append(rec_time)

    # Print results
    print(n, "\t", iter_time, "\t", rec_time, "\t", count)

    print("Iterative Series:", iter_result)
    print("Recursive Series:", rec_result)
    print()


# Plot execution time comparison
plt.figure(figsize=(10, 6))

plt.plot(values, iterative_times, marker='o',
         label='Iterative Fibonacci')

plt.plot(values, recursive_times, marker='s',
         label='Recursive Fibonacci')

plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Fibonacci: Iterative vs Recursive")
plt.legend()
plt.grid(True)
plt.show()
