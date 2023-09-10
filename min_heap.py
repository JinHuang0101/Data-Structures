# Aurthor: Jin Huang
# Description: Implement a MinHeap class.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        """
        return self.heap.length() == 0

    def bubbleUp(self, index):
        """
        Takes a MinHeap and an index, sort the heap so that
        min value is on top.
        """
        parent_index = (index-1) // 2

        # if node at given index is smaller than parent, swap them
        while index != 0:
            if self.heap.get_at_index(index) < self.heap.get_at_index(parent_index):
                self.heap.swap(index, parent_index)
                index = parent_index
                parent_index = (index-1) // 2
            else:
                return

        return



    def add(self, node: object) -> None:
        """
        Takes a MinHeap and a node, adds the new node to the MinHeap maintaining heap property.
        Runtime complexity must be O(logN).
        """
        self.heap.append(node)
        heapLength = self.heap.length()
        nodeIndex = heapLength - 1
        if nodeIndex != 0:
            return self.bubbleUp(nodeIndex)
        return



    def get_min(self) -> object:
        """
        Takes a MinHeap and returns a min key without removing it from the heap.
        Raises MinHeap Exception if the heap is empty.
        """
        if self.is_empty():
            raise MinHeapException

        minValue = self.heap.get_at_index(0)
        return minValue

    def bubbleDown(self, index):
        """
        Takes a MinHeap and an index, sort the heap so that
        min value is at the leftmost bottom.
        """
        heapLength = self.heap.length()
        heapLastIndex = heapLength - 1

        leftChildIndex = index * 2 + 1
        rightChildIndex = leftChildIndex + 1

        minIndex = index


        if leftChildIndex <= heapLastIndex:
            if self.heap.get_at_index(leftChildIndex) < self.heap.get_at_index(minIndex):
                minIndex = leftChildIndex

        if rightChildIndex <= heapLastIndex:
            if self.heap.get_at_index(rightChildIndex) < self.heap.get_at_index(minIndex):
                minIndex = rightChildIndex

        # After comparison, if current index node is not the smallest, swap
        if index != minIndex:
            self.heap.swap(minIndex, index)
            return self.bubbleDown(minIndex)

        return



    def remove_min(self) -> object:
        """
        Takes a MinHeap and removes the object with a min key.
        Raises MinHeapException if empty heap.
        Swap with the left child, if both children have the same value.
        Runtime complexity is O(logN).
        """
        if self.is_empty():
            raise MinHeapException

        # find the min node, swap with the last node, and remove
        minNode = self.get_min()
        lastNodeIndex = self.heap.length() - 1
        self.heap.swap(0,lastNodeIndex)
        self.heap.pop()

        # call bubbleDown to sort the MinHeap
        self.bubbleDown(0)
        return minNode



    def build_heap(self, da: DynamicArray) -> None:
        """
        Takes a dynamic array and builds a MinHeap for the array.
        Runtime complexity is O(N)
        """
        tempHeap = DynamicArray()
        arrLength = da.length()
        lastIndex = arrLength - 1

        for i in range(arrLength):
            value = da.get_at_index(i)
            tempHeap.append(value)

        self.heap = tempHeap

        parentLastIndex = (lastIndex-1)//2

        # bubble down all non-parent nodes in reverse
        while parentLastIndex != -1:
            self.bubbleDown(parentLastIndex)
            parentLastIndex -= 1

        return