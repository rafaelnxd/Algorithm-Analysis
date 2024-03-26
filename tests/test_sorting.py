import os
import sys
import random
from algorithms.sorting import Sorting
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../") 
    
arr = [random.randint(0, 100) for _ in range(1000)]

arr2 = [12, 30, 32, 13, -1, -2, 5, 9, 56]


def test_func(arr):
    time1 = time.time()
    Sorting.selection_sort(arr)
    time2 = time.time()
    return time2 - time1

print("Time to execute Selection Sort's algorithm was: ", test_func(arr))
