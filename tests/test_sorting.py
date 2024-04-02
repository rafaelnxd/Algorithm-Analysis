import os
import sys
import random



sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../") 

from algorithms.sorting import Sorting


class TestSorting:
    def __init__ (self):
        pass


    def test_bubble_sort(self):
        arr = [random.randint(0, 100) for _ in range(10)]
        sorted_arr = sorted(arr)
        try:
            assert Sorting.bubble_sort(arr.copy()) == sorted_arr
            print("The Bubble Sort's test have been successful.")
        except AssertionError:
            print("The Bubble Sort's test have failed.")

    def test_selection_sort(self):
        arr = [random.randint(0, 100) for _ in range(10)]
        sorted_arr = sorted(arr)
        try:
            assert Sorting.selection_sort(arr.copy()) == sorted_arr
            print("Teste de Selection Sort passou.")
        except AssertionError:
            print("Teste de Selection Sort falhou.")
            return


    def test_insertion_sort(self):
        arr = [random.randint(0, 100) for _ in range(10)]
        sorted_arr = sorted(arr)
        try:
            assert Sorting.insertion_sort(arr.copy()) == sorted_arr
            print("Teste de Insertion Sort passou.")
        except AssertionError:
            print("Teste de Insertion Sort falhou.")
            return

  
    def test_merge_sort(self):
        arr = [random.randint(0, 100) for _ in range(10)]
        sorted_arr = sorted(arr)
        try:
            Sorting.mergeSort(arr)
            assert arr == sorted_arr
            print("Teste de Merge Sort passou.")
        except AssertionError:
            print("Teste de Merge Sort falhou.")
            return


    def test_quick_sort(self):
        arr = [random.randint(0, 100) for _ in range(10)]
        sorted_arr = sorted(arr)
        try:
            Sorting.quick_sort(arr)
            assert arr == sorted_arr
            print("Teste de Quick Sort passou.")
        except AssertionError:
            print("Teste de Quick Sort falhou.")
            return

   
    def run_tests(self):
        self.test_bubble_sort()
        self.test_selection_sort()
        self.test_insertion_sort()
        self.test_merge_sort()
        self.test_quick_sort()
        print("Fim dos testes.")

if __name__ == '__main__':
    testes = TestSorting()
    testes.run_tests()

            

       