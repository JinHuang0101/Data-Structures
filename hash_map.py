# Author: Jin Huang
# Description: Implement the HashMap class.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map it in human-readable form
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def calculateIndex(self, key):
        """
        Takes a hash map and key,
        Calculates the index associated with the given key
        """
        hash = self.hash_function(key)
        size = self.capacity
        index = hash % size
        return index


    def clear(self) -> None:
        """
        Takes a hash map and clears the content of the map.
        """
        empty = LinkedList()
        size = self.capacity

        for i in range(size):
            self.buckets.set_at_index(i, empty)
            self.size = 0
        return


    def get(self, key: str) -> object:
        """
        Takes a hash map and key, returns the value associated with the given key.
        If the key is not in the map, returns None.
        """
        if self.contains_key(key) is False:
            return None
        else:
            index = self.calculateIndex(key)
            value = self.buckets.get_at_index(index).contains(key).value
            return value


    def put(self, key: str, value: object) -> None:
        """
        Takes a key and value and updates the key/value pair in the hash map.
        If the key already exists, its value is replaced with the new value.
        If the key is new, adds a new key/value pair.
        """
        index = self.calculateIndex(key)

        bucketSize = self.capacity

        linkListLength = self.buckets.get_at_index(index).length()

        if linkListLength == 0:
            for i in range(bucketSize):
                if i == index:
                    newLinkList = LinkedList()
                    newLinkList.insert(key,value)
                    self.buckets.set_at_index(i, newLinkList)
                    self.size += 1
                    break


        elif self.buckets.get_at_index(index).contains(key) is not None:
            for i in range(bucketSize):
                if i == index:
                    linkList = self.buckets.get_at_index(i)
                    linkList.remove(key)
                    self.size -= 1
                    linkList.insert(key, value)
                    self.buckets.set_at_index(i, linkList)
                    self.size += 1
                    break


        elif self.buckets.get_at_index(index).contains(key) is None:
            for i in range(bucketSize):
                if i == index:
                    linkList = self.buckets.get_at_index(i)
                    linkList.insert(key,value)
                    self.buckets.set_at_index(i, linkList)
                    self.size += 1
                    break

        return



    def remove(self, key: str) -> None:
        """
        Takes a hash map and key,
        Removes the given key and value pair.
        If the given key doesn't exist, does nothing.
        """
        if self.contains_key(key) is False:
            return
        else:
            index = self.calculateIndex(key)
            #linkedContent = self.buckets.get_at_index(index).contains(key).value
            self.buckets.get_at_index(index).remove(key)
            self.size -= 1
            return



    def contains_key(self, key: str) -> bool:
        """
        Takes a hash map and key.
        Returns True if the given key exists; otherwise, returns False.
        """
        index = self.calculateIndex(key)

        linkedContent = self.buckets.get_at_index(index)
        if linkedContent.contains(key) is not None:
            return True
        else:
            return False



    def empty_buckets(self) -> int:
        """
        Takes a hash table and returns the number of empty buckest in the hash table.
        """
        emptyCount = 0
        size = self.capacity

        for i in range(size):
            if self.buckets.get_at_index(i).length() == 0:
                emptyCount += 1

        return emptyCount



    def table_load(self) -> float:
        """
        Takes a hash table and returns the current load factor
        """
        loadFactor = self.size / self.capacity

        return loadFactor


    def resize_table(self, new_capacity: int) -> None:
        """
        Takes a hash table and integer, changes the capacity of the hash table to the new integer.
        All existing key/value pairs remain in the new hash map and all hash table links are rehashed.
        Do nothing if integer is less than 1
        """
        if new_capacity < 1:
            return
        else:
            oldSize = self.capacity
            newHashTable = DynamicArray()
            newkeyList = LinkedList()
            emptyLinkedList = LinkedList()

            # create a new dynamic array with new linked lists
            for i in range(new_capacity):
                newHashTable.append(emptyLinkedList)

            # get the existing linked lists, get the existing nodes,
            # insert into newkeyList
            for i in range(oldSize):
                linkedList = self.buckets.get_at_index(i)
                if linkedList.length() > 0:
                    for node in linkedList:
                        newkeyList.insert(node.key, node.value)

            self.size = 0
            self.capacity = new_capacity
            self.buckets = newHashTable

            # re-hash and updates hash table
            for node in newkeyList:
                self.put(node.key, node.value)

            return



    def get_keys(self) -> DynamicArray:
        """
        Takes a hash map and returns a DynamicArray that contains all keys
        stored in the map.
        """
        newArr = DynamicArray()
        size = self.buckets.length()

        for i in range(size):
            node = self.buckets.get_at_index(i)
            for j in node:
                newArr.append(j.key)

        return newArr
