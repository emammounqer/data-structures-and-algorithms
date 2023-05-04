# Stack and a Queue Implementation

## Approach

### Stack methods

- push

    arguments: value
    adds a new node with that value to the top of the stack with an O(1) Time performance.

- pop

    arguments: none
    Returns: the value from node from the top of the stack
    Removes the node from the top of the stack
    Should raise exception when called on empty stack

- peek

    arguments: none
    Returns: Value of the node located at the top of the stack
    Should raise exception when called on empty stack

- is_empty

    arguments: none
    returns: Boolean indicating whether or not the stack is empty.

### Queue methods

- enqueue

    arguments: value
    adds a new node with that value to the back of the queue with an O(1) Time performance.

- dequeue

    arguments: none
    Returns: the value from node from the front of the queue
    Removes the node from the front of the queue
    Should raise exception when called on empty queue

- peek  

    arguments: none
    Returns: Value of the node located at the front of the queue
    Should raise exception when called on empty queue

- is_empty

    arguments: none
    returns: Boolean indicating whether or not the queue is empty.  

## Efficiency

### Stack Efficiency

| Method | Time | Space |
|--------|------|-------|
| push | O(1) | O(1) |
| pop | O(1) | O(1) |
| peek | O(1) | O(1) |
| is_empty | O(1) | O(1) |

### Queue Efficiency

| Method | Time | Space |
|--------|------|-------|
| enqueue | O(1) | O(1) |
| dequeue | O(1) | O(1) |
| peek | O(1) | O(1) |
| is_empty | O(1) | O(1) |

## Code

- [Stack](./stack.py)
- [Queue](./queue.py)
