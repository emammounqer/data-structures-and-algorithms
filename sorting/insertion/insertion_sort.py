def insert(sorted, value):
    i = 0
    sorted_len = len(sorted)
    while sorted_len > i and value > sorted[i]:
        i += 1
    while i < sorted_len:
        temp = sorted[i]
        sorted[i] = value
        value = temp
        i += 1
    sorted.append(value)


def insertion_sort(input):
    sorted = []
    if len(input) == 0:
        return sorted
    sorted.append(input[0])
    for i in range(1, len(input)):
        insert(sorted, input[i])
    return sorted


if __name__ == '__main__':
    insertion_sort([8, 4, 23, 42, 16, 15])
