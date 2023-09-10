# Author: Jin Huang
# Description: Implement a Dynamic Array class using StaticArray objects.

from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        """
        self.size = 0
        self.capacity = 4
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:               # read value in start_array one by one
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        self.data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True if array is empty / False otherwise
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        """
        return self.size

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Takes a positive integer (new_capacity) and changes the capacity of the storage for the array elements.
        If not positive or if new_capacity < self.size: exit.
        """
        old_data = self.data
        if new_capacity is None:
            self.capacity = self.capacity * 2
            self.data = StaticArray(self.capacity)
        elif new_capacity > 0 and new_capacity >= self.size:
            self.capacity = new_capacity
            self.data = StaticArray(self.capacity)

        # copy from old to new
        start_index = 0
        for i in range(self.size):
            old_value = old_data.__getitem__(i)
            self.set_at_index(start_index, old_value)
            start_index += 1

        return self


    def append(self, value: object) -> None:
        """
        Adds a new value at the end of the dynamic array.
        If the storage is full, double the capacity, then add new a new value.
        """
        starting_index = self.size
        if self.size == self.capacity:
            double_capacity = self.capacity * 2
            self.resize(double_capacity)

        self.size += 1
        self.set_at_index(starting_index, value)

        return self.data



    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a new value at the specified index position in the dynamic array.
        If index invalid: raises a "DynamicArrayException".
        If storage is full, double the dynamic array's capacity, then add a new value.
        """

        # # insert at the last index: append
        # if index == self.size -1 and index != 0:
        #     self.append(value)
        #     return self.data

        if index < 0:
            raise DynamicArrayException

        if self.size != 0 and index > self.size:
            raise DynamicArrayException

        # index out of boundary
        arr_boundary = self.size + 1
        if index >= arr_boundary:
            raise DynamicArrayException


        # empty array
        if self.size == 0:
            self.size += 1
            self.set_at_index(0, value)
            return self.data

        # insert at the end of array
        if index == self.size:
            self.append(value)
            return self.data

        if self.size == self.capacity:
            double_capacity = self.capacity * 2
            self.resize(double_capacity)

        # copy old value starting from index
        temp_arr = StaticArray(self.size)
        temp_arr_index = 0
        temp_arr_counter = 0
        for i in range(index, self.size):
            temp = self.get_at_index(i)
            if temp is not None:
                temp_arr.__setitem__(temp_arr_index, temp)
                temp_arr_index += 1
                temp_arr_counter += 1
        final_temp_arr = StaticArray(temp_arr_counter)
        final_temp_index = 0
        for i in range(temp_arr_counter):
            temp_val = temp_arr.__getitem__(i)
            final_temp_arr.set(final_temp_index, temp_val)
            final_temp_index += 1

        # insert value at index
        self.set_at_index(index, value)

        # copy the rest to the array
        starting_index = index+1
        self.size += 1
        for i in range(final_temp_arr.size()):
            arr_val = final_temp_arr.__getitem__(i)
            self.set_at_index(starting_index, arr_val)
            starting_index += 1

        return self.data


    def remove_at_index(self, index: int) -> None:
        """
        Removes the element at the specified index position.
        If invlaid index: raises DynamicArrayException
        Valid indices: [0, N-1]
        If elements before removal < 1/4 of current capacity:
            Reduction: Capacity reduced to 2 * current elements (before removal)
                If current capacity (before reduction) <= 10:
                    No reduction
                If current capacity (before reduction) > 10:
                    Reduced capacity must remain >= 10
        """
        # out of boundary
        if index >= self.size or index < 0:
            raise DynamicArrayException

        # Reduction
        if self.size < self.capacity * 0.25:
            if self.capacity <= 10:
                pass
            elif self.capacity > 10:
                if self.size * 2 < 10:
                    self.resize(10)
                else:
                    self.resize(self.size * 2)

        # remove the last element
        if index == self.size - 1:
            self.size -= 1
            return self.data

        # copy old values
        temp_arr = StaticArray(self.size - 1)
        temp_arr_index = 0
        temp_counter = 0
        for i in range(index+1, self.size):
            val = self.get_at_index(i)
            temp_arr.__setitem__(temp_arr_index, val)
            temp_arr_index += 1
            temp_counter += 1

        final_temp_arr = StaticArray(temp_counter)
        final_temp_index = 0
        for i in range(final_temp_arr.size()):
            temp_val = temp_arr.get(i)
            final_temp_arr.set(final_temp_index, temp_val)
            final_temp_index += 1


        # update the dynamic array
        self.size -= 1
        da_index = index
        for i in range(final_temp_arr.size()):
            new_val = final_temp_arr.get(i)
            self.set_at_index(da_index, new_val)
            da_index += 1

        return self.data


    def slice(self, start_index: int, size: int) -> object:
        """
        Returns a new Dynamic Array object that contains the requested number of elements from the original array.
        Non-negative integer is a valid size.
        If start index or size is invalid or if not enough elements:
            Raises DynamicArrayException.
        """
        if size < 0 or start_index < 0:
            raise DynamicArrayException

        # out of boundary
        if start_index >= self.size:
            raise DynamicArrayException
        arr_boundary = self.size+1
        if start_index + size >= arr_boundary:
            raise DynamicArrayException

        end_index = start_index + size

        # out of bound
        if end_index > self.size:
            raise DynamicArrayException

        new_arr = DynamicArray()

        # use the append method to construct a new dynamic array
        for i in range(start_index, end_index):
            value = self.get_at_index(i)
            new_arr.append(value)

        return new_arr

    def merge(self, second_da: object) -> None:
        """
        Takes another Dynamic Array and appends all elements to the current array.
        """
        second_da_index = 0
        for i in range(second_da.size):
            second_da_value = second_da.get_at_index(i)
            self.append(second_da_value)

        return self


    def map(self, map_func) -> object:
        """
        Creates a new Dynamic Array, where the value of each element is derived by applying a given map_func
        to the corresponding value from the original array.
        """
        new_arr = DynamicArray()

        for i in range(self.size):
            val = self.get_at_index(i)
            new_val = map_func(val)
            new_arr.append(new_val)

        return new_arr


    def filter(self, filter_func) -> object:
        """
        Creates a new Dynamic Array, populated with those elements from the original array for which filter_func returns True.
        """
        new_arr = DynamicArray()

        for i in range(self.size):
            value = self.get_at_index(i)
            filter_result = filter_func(value)
            if filter_result is True:
                new_arr.append(value)

        return new_arr


    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Sequentially applies the reduce_func to all elements of the Dynamic Array and returns the resulting value.
        If no initializer: the first value in the array is the initializer.
        If the array is empty: returns the value of the initializer or None if not provided.
        """

        if self.size == 0:
            if initializer is not None:
                return initializer
            else:
                return None

        # update the first value with an initializer

        if type(initializer) is str:
            final_result = ""
        else:
            final_result = 0


        if initializer is not None:

            value1 = self.get_at_index(0)
            result1 = reduce_func(initializer, value1)
            final_result += result1

            for i in range(1, self.size):
                y_value = self.get_at_index(i)
                temp_result = reduce_func(final_result, y_value)
                final_result = temp_result



        else:
            # apply reduce function to each element
            final_result = self.get_at_index(0)
            for i in range(1, self.size):
                y_value = self.get_at_index(i)
                temp_result = reduce_func(final_result, y_value)
                final_result = temp_result

        return final_result

