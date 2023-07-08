from hashtable.hashtable import Hashtable


def hashmap_left_join(table1: Hashtable, table2: Hashtable):
    """
    Function to left join two hashmaps.

    Args:
        table1 (Hashtable): Hashtable to be joined.
        table2 (Hashtable): Hashtable to join with.

    Returns:
        list[list]: List of lists containing the key, value from table1, and value from table2.
    """
    arr = []
    for key in table1.keys():
        arr.append([key, table1.get(key), table2.get(key)])
    return arr
