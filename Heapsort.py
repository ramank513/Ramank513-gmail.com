import heapq

def heap_sort(arr):
    heapq.heapify(arr)  # turn list into min-heap
    sorted_arr = []

    while arr:
        sorted_arr.append(heapq.heappop(arr))  # pop smallest

    return sorted_arr


# Test
arr = [12, 3, 5, 7, 19, 0]
sorted_arr = heap_sort(arr)
print("Heap Sorted:", sorted_arr)
