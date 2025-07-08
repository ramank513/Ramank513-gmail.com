def quick_sort(arr):
    if len(arr) <= 1:
        return arr  

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


# Test
arr = [29, 10, 14, 37, 13]
sorted_arr = quick_sort(arr)
print("Sorted Array:", sorted_arr)
