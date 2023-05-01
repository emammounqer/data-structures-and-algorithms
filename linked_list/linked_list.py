
from linked_list.node import Node


class LinkedList:
    """
    A linked list

    Attributes:
        head (Node): The head of the linked list
        length (int): The length of the linked list
    """

    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        return self.to_string()

    def insert(self, value):
        """
        Insert a new node at the head of the linked list

        Args:
            value (any): The value of the new node
        """
        old_node = self.head
        new_node = Node(value)

        new_node.next = old_node
        self.head = new_node
        self.length += 1

    def insert_before(self, value, new_value):
        """
        Insert a new node before a node with a given value

        Args:
            value (any): The value of the node to insert before
            new_value (any): The value of the new node
        """
        new_node = Node(new_value)
        curr = self.head
        prev = None
        while curr is not None:
            if curr.value == value:
                if prev is not None:
                    prev.next = new_node
                else:
                    self.head = new_node
                new_node.next = curr
                return

            prev = curr
            curr = curr.next

        raise ValueError("Value not found")

    def insert_after(self, value, new_value):
        """
        Insert a new node after a node with a given value

        Args:
            value (any): The value of the node to insert after
            new_value (any): The value of the new node
        """
        new_node = Node(new_value)
        curr = self.head
        while curr is not None:
            if curr.value == value:
                new_node.next = curr.next
                curr.next = new_node
                return
            curr = curr.next
        raise ValueError("Value not found")

    def insert_multiple(self, *values):
        """
        Insert multiple nodes at the head of the linked list

        Args:
            *values (any): The values of the new nodes
        """
        for value in values:
            self.insert(value)

    def append(self, value):
        """
        Append a new node to the end of the linked list

        Args:   
            value (any): The value of the new node
        """
        new_node = Node(value)
        if (self.head is None):
            self.head = new_node
            self.length += 1
            return

        curr = self.head
        while (curr.next is not None):
            curr = curr.next
        curr.next = new_node
        self.length += 1

    def delete(self, value):
        """
        Delete a node with a given value

        Args:
            value (any): The value of the node to delete
        """
        curr = self.head
        prev = None

        while (curr is not None):
            if (curr.value == value):
                if (prev is None):
                    self.head = curr.next
                else:
                    prev.next = curr.next
                self.length -= 1
                return
            prev = curr
            curr = curr.next

    def includes(self, value):
        """
        Check if a node with a given value exists

        Args:
            value (any): The value of the node to check for

        Returns:
            bool: True if the node exists, False otherwise  
        """
        curr = self.head
        while (curr is not None):
            if (curr.value == value):
                return True
            curr = curr.next
        return False

    def to_string(self):
        """
        Convert the linked list to a string

        Returns:
            str: The string representation of the linked list
        """
        output = ""
        curr = self.head
        while (curr is not None):
            output += f"{{ {curr.value} }} -> "
            curr = curr.next
        output += "NONE"
        return output

    def get_item(self, index: int):
        """
        Get the value of the node at a given index

        Args:
            index (int): The index of the node

        Returns:
            The value of the node at the given index
        """
        if index < 0:
            raise IndexError("Index must be positive")

        curr = self.head

        if (curr is None):
            raise IndexError("Index out of range")

        while curr is not None and index >= 0:
            if (index == 0):
                return curr.value
            index -= 1
            curr = curr.next

        raise IndexError("Index out of range")

    def kth_from_end(self, k: int):
        """
        Get the value of the node at a given index from the end of the linked list

        Args:
            k (int): The index from the end of the linked list

        Returns:
            The value of the node at the given index from the end of the linked list

        """
        if k < 0:
            raise IndexError("Index must be positive")
        if k > self.length:
            raise IndexError("Index out of range")

        index = self.length - k - 1
        return self.get_item(index)

    @staticmethod
    def zip_lists(list1: 'LinkedList', list2: 'LinkedList'):
        """
        Zip two linked lists together

        Args:
            list1 (LinkedList): The first linked list
            list2 (LinkedList): The second linked list

        Returns:
            LinkedList: The zipped linked list
        """
        if list1.head is None:
            return list2
        if list2.head is None:
            return list1

        curr1 = list1.head
        curr2 = list2.head

        while curr1 is not None and curr2 is not None:
            next1 = curr1.next
            next2 = curr2.next

            curr1.next = curr2
            curr2.next = next1 or next2

            curr1 = next1
            curr2 = next2

        return list1
