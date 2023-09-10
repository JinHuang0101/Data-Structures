# Student Name: Jin Huang
# Description: Implement a Queue ADT class using the Dynamic Array data structure.

from dynamic_array import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new queue based on Dynamic Array
        """
        self.da = DynamicArray()

    def __str__(self):
        """
        Return content of stack in human-readable form
        """
        out = "QUEUE: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da[i]) for i in range(self.da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        """
        return self.da.length()

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        Adds a new value to the end of the queue.
        O(1) amortized runtime complexity.
        """
        self.da.append(value)
        return self


    def dequeue(self) -> object:
        """
        Removes and returns the value at the beginning of the queue.
        O(N) runtime complexity.
        If empty queue: raises "QueueException".
        """
        if self.da.length() == 0:
            raise QueueException

        else:
            first_value = self.da.get_at_index(0)
            self.da.remove_at_index(0)
            return first_value
