import sys
import os

# Adiciona o diretório 'algorithms' ao sys.path para que o Python possa encontrar o módulo 'search.py'
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../") 


from algorithms.search import Search

import random

class TestSearch:
    def __init__(self):
        self.sorted_list = [3, 5, 7, 9, 27, 34, 63, 88, 89]

    def test_sequential_search(self):
        values = [random.randint(1, 100) for _ in range(5)]
    
        for v in values:
            result = Search.sequential_search(self.sorted_list, v)
            if v in self.sorted_list:
                expected = self.sorted_list.index(v)
                if result == expected:
                    print(f"Sequential search test for value {v} passed.")
                else:
                    print(f"Sequential search test for value {v} failed. Expected index: {expected}, Actual index: {result}")
            else:
                if result == -1:
                    print(f"Sequential search test for value {v} passed.")
                else:
                    print(f"Sequential search test for value {v} failed. Expected index: -1, Actual index: {result}")


    def test_binary_search(self):
        try:
            assert Search.binary_search(self.sorted_list, 34) == 5
            assert Search.binary_search(self.sorted_list, 88) == 7
            assert Search.binary_search(self.sorted_list, 50) == -1
            print("Binary search test passed.")
        except AssertionError:
            print("Binary search test failed.")


    def run_tests(self):
        self.test_sequential_search()
        self.test_binary_search()
        print("End of tests.")

if __name__ == '__main__':
    test_search = TestSearch()
    test_search.run_tests()
