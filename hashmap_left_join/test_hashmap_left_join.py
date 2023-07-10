from hashmap_left_join.hashmap_left_join import hashmap_left_join
from hashtable.hashtable import Hashtable


def test_hashmap_left_join():
    """Function to test hashmap_left_join."""
    table1 = Hashtable()
    table1.set('fond', 'enamored')
    table1.set('wrath', 'anger')
    table1.set('diligent', 'employed')
    table1.set('outfit', 'garb')
    table1.set('guide', 'usher')
    table2 = Hashtable()
    table2.set('fond', 'averse')
    table2.set('wrath', 'delight')
    table2.set('diligent', 'idle')
    table2.set('guide', 'follow')
    table2.set('flow', 'jam')

    expected = [['wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], [
        'outfit', 'garb', None], ['guide', 'usher', 'follow'], ['fond', 'enamored', 'averse']]
    expected.sort()
    actual = hashmap_left_join(table1, table2)
    actual.sort()
    assert actual == expected


def test_hashmap_left_join_empty():
    """Function to test hashmap_left_join with empty hashmaps."""
    table1 = Hashtable()
    table2 = Hashtable()

    expected = []
    actual = hashmap_left_join(table1, table2)
    assert actual == expected
