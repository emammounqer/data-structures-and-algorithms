# Challenge Title

## class 30

Create Hashtable that has the following methods:

- set: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

- get: takes in the key and returns the value from the table.

- has: takes in the key and returns a boolean, indicating if the key exists in the table already.

- keys: returns an array of the keys in the table.

- hash: takes in an arbitrary key and returns an index in the collection.

## Approach & Efficiency

| Method | Time | Space |
|--------|------|-------|
| set    | O(1) | O(1)  |
| get    | O(1) | O(1)  |
| has    | O(1) | O(1)  |
| keys   | O(n) | O(n)  |
| hash   | O(1) | O(1)  |

## Code

- [Hashtable](./hashtable.py)
