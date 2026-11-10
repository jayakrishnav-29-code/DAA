
# Global comparison counter
count = 0

# Divide and Conquer function
def find_min_max(arr, low, high):
    global count

    # Case 1: Only one element
    if low == high:
        return arr[low], arr[low]

    # Case 2: Two elements
    if high == low + 1:
        count += 1

        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide the array into two halves
    mid = (low + high) // 2

    # Find minimum and maximum in left half
    min1, max1 = find_min_max(arr, low, mid)

    # Find minimum and maximum in right half
    min2, max2 = find_min_max(arr, mid + 1, high)

    # Combine the results
    count += 2

    minimum = min(min1, min2)
    maximum = max(max1, max2)

    return minimum, maximum


# Main program
arr = [45, 12, 89, 3, 67, 23, 91, 5, 34, 78]

# Find minimum and maximum
minimum, maximum = find_min_max(arr, 0, len(arr) - 1)

# Display results
print("Given Array:", arr)
print("Minimum Element:", minimum)
print("Maximum Element:", maximum)
print("Total Comparisons:", count)
