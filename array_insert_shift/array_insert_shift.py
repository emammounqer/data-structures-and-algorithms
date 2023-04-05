def array_insert_shift(array: list, value: object):
    middle_index = -(-len(array) // 2)

    array.append(None)
    for i in range(len(array), middle_index, -1):
        print(array)
        array[i - 1] = array[i - 1 - 1]
    array[middle_index] = value
    return array


print(array_insert_shift([1, 2, 3, 4], 5))  # [1, 2, 5, 3, 4]
