import os
import sys
import random
import unittest
from algorithms.sorting import Sorting


sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../") 
    
class TestSorting:
    def __init__ (self):
        self.unsorted_list = [random.randint(0, 100) for _ in range(10)]
        self.sorted_list = sorted(self.unsorted_list)

    
    def test_bubble_sort(self):
        arr1 = [3, 7, 33, 59, 71]
        self.assertEqual(Sorting.bubble_sort(arr1.copy()), sorted(arr1))
       