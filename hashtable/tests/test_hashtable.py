from pytest import fixture
from hashtable.hashtable import Hashtable


def test_hashtable_insert_one():
    ht = Hashtable()
    ht.set('apple', 5)
    assert ht.get('apple') == 5


def test_hashtable_insert_two():
    ht = Hashtable()
    ht.set('apple', 5)
    ht.set('banana', 6)
    assert ht.get('apple') == 5
    assert ht.get('banana') == 6


@fixture
def ht():
    hs = Hashtable()
    hs.set('apple', 5)
    hs.set('banana', 6)
    hs.set('carrot', 7)

    return hs


def test_hashtable_get_none(ht: Hashtable):
    assert ht.get('dinosaur') == None


def test_hashtable_get_value(ht: Hashtable):
    assert ht.get('apple') == 5


def test_hashtable_get_value_collision():
    ht = Hashtable(2)
    ht.set('apple', 5)
    ht.set('banana', 6)
    ht.set('carrot', 7)
    keys = ht.keys()
    keys.sort()
    assert keys == ['apple', 'banana', 'carrot']


def test_hashtable_has_key_true(ht: Hashtable):
    assert ht.has('apple') == True


def test_hashtable_has_key_false(ht: Hashtable):
    assert ht.has('dinosaur') == False


def test_hashtable_keys(ht: Hashtable):
    expected = ['apple', 'banana', 'carrot']
    actual = ht.keys()
    expected.sort()
    actual.sort()
    assert actual == expected
