from stack_queue_brackets.validate_brackets import validate_brackets


def test_validate_brackets_1():
    actual = validate_brackets('{}')
    expected = True
    assert actual == expected


def test_validate_brackets_2():
    actual = validate_brackets('{}(){}')
    expected = True
    assert actual == expected


def test_validate_brackets_3():
    actual = validate_brackets('()[[Extra Characters]]')
    expected = True
    assert actual == expected


def test_validate_brackets_4():
    actual = validate_brackets('(){}[[]]')
    expected = True
    assert actual == expected


def test_validate_brackets_5():
    actual = validate_brackets('{}{Code}[Fellows](())')
    expected = True
    assert actual == expected


def test_validate_brackets_6():
    actual = validate_brackets('[({}]')
    expected = False
    assert actual == expected


def test_validate_brackets_7():
    actual = validate_brackets('(](')
    expected = False
    assert actual == expected


def test_validate_brackets_8():
    actual = validate_brackets('{(})')
    expected = False
    assert actual == expected


def test_validate_brackets_9():
    actual = validate_brackets('{')
    expected = False
    assert actual == expected
