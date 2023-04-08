from array_insert_shift.array_insert_shift import array_insert_shift


def test_array_insert_shift_basic():
    actual = array_insert_shift([1, 2, 3, 4], 5)
    expected = [1, 2, 5, 3, 4]
    assert actual == expected


def test_array_insert_shift_empty():
    actual = array_insert_shift([], 5)
    expected = [5]
    assert actual == expected


def test_array_insert_shift_odd():
    actual = array_insert_shift([1, 2, 3, 4, 5], 6)
    expected = [1, 2, 3, 6, 4, 5]
    assert actual == expected
