def find_smallest(arr):
    if not arr:
        raise ValueError("Array is empty")

    smallest = arr[0]
    for num in arr[1:]:
        if num < smallest:
            smallest = num
    return smallest

def find_largest(arr):
    if not arr:
        raise ValueError("Array is empty")

    largest = arr[0]
    for num in arr[1:]:
        if num > largest:
            largest = num
    return largest

arr = [5, 2, 9, 1, 7]

print("Smallest:", find_smallest(arr))
print("Largest:", find_largest(arr))