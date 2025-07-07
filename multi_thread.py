import threading

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def threaded_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left_result = []
    right_result = []

    def sort_left():
        nonlocal left_result
        left_result = threaded_merge_sort(left)

    def sort_right():
        nonlocal right_result
        right_result = threaded_merge_sort(right)

    t1 = threading.Thread(target=sort_left)
    t2 = threading.Thread(target=sort_right)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    return merge(left_result, right_result)


data = [38, 27, 43, 3, 9, 82, 10,32,77,11,33]
print("Unsorted:", data)
sorted_data = threaded_merge_sort(data)
print("Sorted:", sorted_data)