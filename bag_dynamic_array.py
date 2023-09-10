# Author: Jin Huang
# Description: Implement a Bag ADT class using Dynamic Array.

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        """
        return self.da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Adds a new element to the bag. O(1) amortized complexity.
        """
        # use Dynamic Array append method
        self.da.append(value)

        return self.da


    def remove(self, value: object) -> bool:
        """
        Removes any one element from the bag that matches the value object.
        Returns True if the removal is successful.
        Otherwise, returns False.
        O(N) runtime complexity
        """
        for i in range(self.da.length()):
            bag_value = self.da.get_at_index(i)
            if bag_value == value:
                self.da.remove_at_index(i)
                return True
        return False


    def count(self, value: object) -> int:
        """
        Counts the number of elements in the bag that match "value". O(N) runtime complexity.
        """
        counter = 0
        for i in range(self.da.length()):
            bag_value = self.da.get_at_index(i)
            if bag_value == value:
                counter += 1
        return counter


    def clear(self) -> None:
        """
        Clears the contents of the bag. O(1) runtime
        """
        # empty bag to clear
        if self.da.length() == 0:
            return self
        else:
            # use slice to create an empty dynamic array
            new_arr = self.da.slice(0,0)

            self.da = new_arr           # assign to the original array

        return self


    def equal(self, second_bag: object) -> bool:
        """
        Compares the contents of a bag with the contents of a second bag.
        Returns True if equal (have the same number of elements && contain the same elements)
        Returns False otherwise
        Empty bag is equal to another empty bag
        """
        bag1_size = self.da.length()
        bag2_size = second_bag.da.length()

        # empty bags
        if bag1_size == bag2_size == 0:
            return True

        if bag1_size != bag2_size:
            return False

        # use count method and compare the count of each element in two bags
        if bag1_size == bag2_size:
            for i in range(bag1_size):
                bag1_value = self.da.get_at_index(i)
                bag1_value_count = self.count(bag1_value)
                bag2_value_count = second_bag.count(bag1_value)
                if bag1_value_count != bag2_value_count:
                    return False
            return True

