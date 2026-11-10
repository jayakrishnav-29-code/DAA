
# Global counters
inversions = 0
comparisons = 0


# Merge function
def merge(arr, left, mid, right):
    global inversions, comparisons

    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    # Merge two halves using for loop
    for x in range(len(L) + len(R)):

        if i < len(L) and j < len(R):

            comparisons += 1

            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1

            else:
                arr[k] = R[j]

                # Count inversions
                inversions += len(L) - i

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


# Merge Sort function
def merge_sort(arr, left, right):

    if left < right:

        mid = (left + right) // 2

        # Divide left half
        merge_sort(arr, left, mid)

        # Divide right half
        merge_sort(arr, mid + 1, right)

        # Merge both halves
        merge(arr, left, mid, right)


# Main program
arr = [8, 4, 2, 1, 3, 5]

print("Original Array:", arr)

merge_sort(arr, 0, len(arr) - 1)

# Display results
print("Sorted Array:", arr)
print("Total Inversions:", inversions)
print("Total Comparisons:", comparisons)