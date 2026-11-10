
# Partition function
def partition(arr, low, high):

    # Select last element as pivot
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# Quick Select function
def quick_select(arr, low, high, key):

    if low <= high:

        # Find pivot position
        pi = partition(arr, low, high)

        # Check pivot position
        if pi == key:
            return arr[pi]

        # Search left half
        elif pi > key:
            return quick_select(arr, low, pi - 1, key)

        # Search right half
        else:
            return quick_select(arr, pi + 1, high, key)

    return -1


# Main program
arr = [12, 3, 5, 7, 19, 1, 8, 15, 4]

print("Original Array:", arr)

# Values of k
k_values = [3, 4, 6]

for k in k_values:

    # Create a copy of original array
    temp = arr.copy()

    # Quick Select uses zero-based indexing
    result = quick_select(temp, 0, len(temp) - 1, k - 1)

    print(k, "rd/smallest element:",result)
