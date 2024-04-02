import os
import sys
import random



sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../") 

from algorithms.sorting import Sorting


import sys
import os

# Adiciona o diretório 'algorithms' ao sys.path para que o Python possa encontrar o módulo 'search.py'
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../") 


from algorithms.search import Search

import random

class TestSorting:
    def __init__(self):
        pass

    def test_bubble_sort(self, arr):
        sorted_arr = sorted(arr)
        try:
            assert Sorting.bubble_sort(arr.copy()) == sorted_arr
            print("O teste do Bubble Sort foi bem-sucedido.")
        except AssertionError:
            print("O teste do Bubble Sort falhou.")

    def test_selection_sort(self, arr):
        sorted_arr = sorted(arr)
        try:
            assert Sorting.selection_sort(arr.copy()) == sorted_arr
            print("O teste do Selection Sort foi bem-sucedido.")
        except AssertionError:
            print("O teste do Selection Sort falhou.")
            return

    def test_insertion_sort(self, arr):
        sorted_arr = sorted(arr)
        try:
            assert Sorting.insertion_sort(arr.copy()) == sorted_arr
            print("O teste do Insertion Sort foi bem-sucedido.")
        except AssertionError:
            print("O teste do Insertion Sort falhou.")
            return

    def test_merge_sort(self, arr):
        sorted_arr = sorted(arr)
        try:
            Sorting.mergeSort(arr)
            assert arr == sorted_arr
            print("O teste do Merge Sort foi bem-sucedido.")
        except AssertionError:
            print("O teste do Merge Sort falhou.")
            return

    def test_quick_sort(self, arr):
        sorted_arr = sorted(arr)
        try:
            Sorting.quick_sort(arr)
            assert arr == sorted_arr
            print("O teste do Quick Sort foi bem-sucedido.")
        except AssertionError:
            print("O teste do Quick Sort falhou.")
            return

    def run_tests(self):
        test_cases = [
            ([3, 7, 33, 59, 71], "vetor ordenado crescente"),
            ([71, 7, 3, 9, 7], "vetor não ordenado"),
            ([71, 59, 33, 7, 3], "vetor ordenado descrescente"),
            ([], "Vetor vazio"),
            ([42], "Vetor com um único elemento"),
            ([3, 7, 3, 9, 7], "Vetor com elementos repetidos"),
            ([-5, -3, -9, -1], "Vetor com elementos negativos"),
            ([random.randint(0, 100) for _ in range(100)], "Lista de 100 números aleatórios")
        ]

        for arr, desc in test_cases:
            print(f"Testando {desc}: {arr}")
            self.test_bubble_sort(arr)
            self.test_selection_sort(arr)
            self.test_insertion_sort(arr)
            self.test_merge_sort(arr)
            self.test_quick_sort(arr)
            print()

        print("Fim dos testes.")

if __name__ == '__main__':
    testes = TestSorting()
    testes.run_tests()
