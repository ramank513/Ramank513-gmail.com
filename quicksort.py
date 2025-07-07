def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)   # Left of pivot
        quick_sort(arr, pivot_index + 1, high)  # Right of pivot

def partition(arr, low, high):
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1        # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot
    return i + 1

arr = [10, 7, 8, 9, 1, 5]
print("Unsorted array:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)