def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        print(mid)
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


print(binary_search([-131, -82, 0, 27, 42, 68, 179], 42))
