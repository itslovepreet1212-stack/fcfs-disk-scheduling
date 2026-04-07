"""
Custom Stack Class Implementation
A simple stack data structure for tracking disk cylinder traversal.
"""


class Stack:
    """
    A custom Stack class implementing basic stack operations.
    Used to record the sequence of cylinder positions visited during FCFS disk scheduling.
    """

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    def push(self, item):
        """
        Push an item onto the stack.
        
        Args:
            item: The cylinder position to add to the stack.
        """
        self._items.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.
        
        Returns:
            The last item added to the stack.
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def peek(self):
        """
        Return the top item without removing it.
        
        Returns:
            The last item added to the stack.
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if stack has no items, False otherwise.
        """
        return len(self._items) == 0

    def size(self):
        """
        Return the number of items in the stack.
        
        Returns:
            int: Number of items in the stack.
        """
        return len(self._items)

    def display(self):
        """
        Display all items in the stack from bottom to top.
        
        Returns:
            list: A copy of all items in the stack.
        """
        return self._items.copy()

    def clear(self):
        """Remove all items from the stack."""
        self._items.clear()
