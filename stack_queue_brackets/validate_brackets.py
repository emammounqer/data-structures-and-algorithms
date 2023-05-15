from stack_and_queue.stack import Stack


def validate_brackets(str: str):
    """
    write function that string argument and see it the string is balanced or not
    type of bracket : {} [] ()

    Input: str
    return: boolean
    """
    brackets_type = {"{": "}", "[": "]", "(": ")"}
    open_brackets = ["{", '[', '(']
    closed_brackets = ["}", ']', ')']
    open_stack = Stack()

    for c in str:
        if c in open_brackets:
            open_stack.push(c)
        if c in closed_brackets:
            if open_stack.is_empty():
                return False
            last_open_stack = open_stack.pop()
            if (brackets_type[last_open_stack] != c):
                return False

    if open_stack.is_empty():
        return True

    return False
