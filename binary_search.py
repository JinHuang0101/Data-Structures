# Author: Jin Huang
# Description: Write binary_search and binary_search_rotated functions.

import random
import time
from static_array import *


# ------------------- PROBLEM 1 - -------------------------------------------


def binary_search(arr: StaticArray, target: int) -> int:
    """
    Receives a sorted StaticArray and an integer target.
    If target exists, returns the index of target.
    Otherwise, returns -1.
    Runtimecomplexity O(logN)
    """
    # one-element array
    if arr.size() == 1:
        if arr.get(0) == target:
            return 0
        else:
            return -1


    low = 0
    high = arr.size() - 1
    mid = 0

    # ascending
    if arr.get(low) < arr.get(high):
        while low <= high:
            mid = (low + high) // 2
            if arr.get(mid) < target:
                low = mid + 1

            elif arr.get(mid) > target:
                high = mid - 1

            # target is mid
            else:
                return mid
        return -1

    elif arr.get(low) > arr.get(high):
        while low <= high:
            mid = (low + high) // 2

            if arr.get(mid) < target:
                high = mid - 1

            elif arr.get(mid) > target:
                low = mid + 1

            # target is mid
            else:
                return mid
        return -1



# ------------------- PROBLEM 2 - -------------------------------------------
def binary_search_rotated(arr: StaticArray, target: int) -> int:
    """
    Receives an ascending StaticArray and an integer target.
    Before being processed, the input array will be rotated an unknown number of steps (right or left).
    If target exists, returns the index of target.
    Otherwise, returns -1.
    Runtimecomplexity O(logN)
    """
    low = 0
    arrLength = arr.size()
    high = arrLength - 1

    while low <= high:
        mid = (low + high)//2

        if arr.get(mid) == target:
            return mid

        elif target > arr.get(mid):
            # if this half is sorted and target is out of bound,
            # then target is not in this half
            if arr.get(mid) < arr.get(high) and target > arr.get(high):
                high = mid - 1
            # else, target is in this half, narrow down
            else:
                low = mid + 1

        else:
            # else, if target < arr.get(mid):
            # if this half is sorted and target is less than get(low),
            # then target is not in this half
            if arr.get(low) <= arr.get(mid) and target < arr.get(low):
                low = mid + 1
            # else, target is in this half, narrow down
            else:
                high = mid - 1



    return -1