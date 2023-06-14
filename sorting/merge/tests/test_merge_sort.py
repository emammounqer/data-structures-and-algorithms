from ..merge_sort import merge_sort


def test_happy_path():
    """Test happy path."""
    assert merge_sort([8, 4, 23, 42, 16, 15]) == [4, 8, 15, 16, 23, 42]


def test_empty():
    """Test empty."""
    assert merge_sort([]) == []


def test_reverse_order():
    """Test reverse order."""
    assert merge_sort([20, 18, 12, 8, 5, -2]) == [-2, 5, 8, 12, 18, 20]


def test_few_uniques():
    """Test few uniques."""
    assert merge_sort([5, 12, 7, 5, 5, 7]) == [5, 5, 5, 7, 7, 12]


def test_nearly_sorted():
    """Test nearly sorted."""
    assert merge_sort([2, 3, 5, 7, 13, 11]) == [2, 3, 5, 7, 11, 13]
