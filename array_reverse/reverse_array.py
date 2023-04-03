def reverse_array(array):
    reverse_array = []
    for i in range(len(array)):
        reverse_array.append(array[len(array) - 1 - i])
    return reverse_array
