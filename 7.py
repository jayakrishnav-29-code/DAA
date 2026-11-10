
# Partition function
def partition(arr, low, high):

    # Select last element as pivot
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1

            # Swap elements
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    print("Pivot:", pivot)
    print("Array after partition:", arr)
    print()

    return i + 1


# Quick Sort function
def quick_sort(arr, low, high):

    if low < high:

        # Partition the array
        pi = partition(arr, low, high)

        # Sort left subarray
        quick_sort(arr, low, pi - 1)

        # Sort right subarray
        quick_sort(arr, pi + 1, high)


# Main program
arr = [29, 10, 14, 37, 13, 25, 8, 42]

print("Original Array:", arr)
print("\nPartition Operations:\n")

# Apply Quick Sort
quick_sort(arr, 0, len(arr) - 1)

# Display sorted array
print("Final Sorted Array:", arr)