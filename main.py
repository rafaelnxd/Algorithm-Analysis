# main.py

from algorithms.sorting import Sorting
from algorithms.search import Search
import random
import time
import matplotlib.pyplot as plt

def measure_execution_time(algorithm, lst, target=None):
 
    start_time = time.time()
    if target is not None:
        algorithm(lst, target)
    else:
        algorithm(lst)
    end_time = time.time()
    return end_time - start_time

def generate_test_data(size):

    return [random.randint(1, 1000) for _ in range(size)]

def analyze_performance(algorithms, sizes, type):

    results = {}

    for name, algorithm in algorithms.items():
        execution_times = []
        for size in sizes:
            if type == 'Sorting':
                lst = generate_test_data(size)
            elif type == 'Search':
                lst = sorted(generate_test_data(size))  # Ensure a sorted list for search
                target = random.choice(lst)
            time_taken = measure_execution_time(algorithm, lst, target if type == 'Search' else None)
            execution_times.append(time_taken)
        results[name] = execution_times

    return results

def generate_plot(results, sizes, type):

    plt.figure(figsize=(10, 6))
    for name, execution_times in results.items():
        plt.plot(sizes, execution_times, label=name)
    plt.xlabel('Size of List')
    plt.ylabel('Execution Time (s)')
    plt.title(f'Performance of {type} Algorithms')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'report_plot_{type.lower()}.png')
    plt.show()


def main():
    sorting_algorithms = {
        'Bubble Sort': Sorting.bubble_sort,
        'Selection Sort': Sorting.selection_sort,
        'Insertion Sort': Sorting.insertion_sort,
        'Merge Sort': Sorting.mergeSort,
        'Quick Sort': Sorting.quick_sort
    }

    search_algorithms = {
        'Binary Search': Search.binary_search,
        'Sequential Search': Search.sequential_search
    }

    test_sizes = [100, 1000, 10000]  # Example test list sizes

    sorting_results = analyze_performance(sorting_algorithms, test_sizes, 'Sorting')
    generate_plot(sorting_results, test_sizes, 'Sorting')

    search_results = analyze_performance(search_algorithms, test_sizes, 'Search')
    generate_plot(search_results, test_sizes, 'Search')

if __name__ == "__main__":
    main()
