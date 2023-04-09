from array_binary_search.array_binary_search import binary_search


def test_binary_search():
    actual = binary_search([-131, -82, 0, 27, 42, 68, 179], 42)
    expected = 4
    assert actual == expected


def test_binary_search_not_found():
    actual = binary_search([-131, -82, 0, 27, 42, 68, 179], 500)
    expected = -1
    assert actual == expected


def test_binary_search_empty():
    actual = binary_search([], 500)
    expected = -1
    assert actual == expected


def test_binary_search_one():
    actual = binary_search([42], 42)
    expected = 0
    assert actual == expected
