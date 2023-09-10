# Author: Jin Huang
# Description: Implement a MaxStack ADT class using the Dynamic Array data structure.

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    """
    pass


class MaxStack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da_val = DynamicArray()
        self.da_max = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "MAX STACK: " + str(self.da_val.length()) + " elements. ["
        out += ', '.join([str(self.da_val[i]) for i in range(self.da_val.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da_val.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da_val.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        Adds a new element to the top of the stack.
        O(1) amortized runtime complexity.
        """

        # push value to the da_max stack
        if self.da_max.is_empty():
            self.da_max.append(value)

        else:
            last_max_index = self.da_max.length()-1
            max_value = self.da_max.get_at_index(last_max_index)
            if value >= max_value:                      # append new largest value
                self.da_max.append(value)
            else:                                       # or else, append the old largest value again
                self.da_max.append(max_value)

        # append value to the end of the array
        self.da_val.append(value)

        return self


    def pop(self) -> object:
        """
        Removes the top element from the stack and returns its value.
        O(1) amortized runtime complexity.
        If empty stack: raise "StackException"
        """
        if self.da_val.length() == 0:           # empty array
            raise StackException
        else:

            # remove the last element from the array
            last_index = self.da_val.length() - 1
            last_element = self.da_val.get_at_index(last_index)     # get the last element
            self.da_val.remove_at_index(last_index)                 # remove the last element

            # remove the last (largest) element from the da_max stack
            last_max_index = self.da_max.length()-1
            self.da_max.remove_at_index(last_max_index)


            return last_element


    def top(self) -> object:
        """
        Returns the value of the top element of the stack without removing it.
        O(1) runtime complexity.
        If empty stack: raises "StackException"
        """
        if self.da_val.length() == 0:           # empty array
            raise StackException
        else:
            last_index = self.da_val.length() - 1
            last_element = self.da_val.get_at_index(last_index)     # get the last element

            return last_element


    def get_max(self) -> object:
        """
        Returns the max value currently stored in the stack.
        O(1) runtime complexity.
        If empty stack: raises "StackException"
        """
        if self.da_val.length() == 0:       # empty array
            raise StackException
        else:
            last_max_index = self.da_max.length()-1
            return self.da_max.get_at_index(last_max_index)

