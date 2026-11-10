
# Global counter
count = 0

# Recursive Binary Search
def binary_search(arr, low, high, key):
    global count
    count += 1

    # Base condition
    if low > high:
        return -1

    # Find middle element
    mid = (low + high) // 2

    # Element found
    if arr[mid] == key:
        return mid

    # Search in right half
    elif arr[mid] < key:
        return binary_search(arr, mid + 1, high, key)

    # Search in left half
    else:
        return binary_search(arr, low, mid - 1, key)


# Main program
arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55,65]

search_values = [25, 45, 60,66]

print("Array:", arr)
print("\nElement\tIndex\tRecursive Calls")

for key in search_values:

    # Reset counter
    count = 0

    # Perform binary search
    result = binary_search(arr, 0, len(arr) - 1, key)

    # Display result
    print(key, "\t", result, "\t", count)
