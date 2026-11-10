# Global comparison counter
count = 0

# Merge function
def merge(arr, left, mid, right):
    global count

    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    # Compare and merge elements
    for x in range(len(L) + len(R)):

        if i < len(L) and j < len(R):
            count += 1

            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1

            k += 1

        elif i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        elif j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    print("After merging:", arr)


# Merge Sort function
def merge_sort(arr, left, right):

    if left < right:

        mid = (left + right) // 2

        merge_sort(arr, left, mid)

        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)


# Main program
arr = [38, 27, 43, 3, 9, 82, 10, 15]

print("Original Array:", arr)

merge_sort(arr, 0, len(arr) - 1)

print("\nFinal Sorted Array:", arr)
print("Total Comparisons:", count)