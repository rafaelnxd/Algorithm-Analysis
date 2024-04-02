
from algorithms.sorting import Sorting
from algorithms.search import Search
import random
import time
import matplotlib.pyplot as plt
import numpy as np

def plot_big_o():
    
    sizes = np.linspace(1, 10000, 100)

    bubble_sort = sizes ** 2
    selection_sort = sizes ** 2
    insertion_sort = sizes ** 2
    merge_sort = sizes * np.log(sizes)
    quick_sort = sizes * np.log(sizes)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, bubble_sort, label="Bubble Sort (O(n^2))")
    plt.plot(sizes, selection_sort, label="Selection Sort (O(n^2))")
    plt.plot(sizes, insertion_sort, label="Insertion Sort (O(n^2))")
    plt.plot(sizes, merge_sort, label="Merge Sort (O(n*log(n)))")
    plt.plot(sizes, quick_sort, label="Quick Sort (O(n*log(n)))")
    plt.xlabel('Size of Input')
    plt.ylabel('Time Complexity')
    plt.title('Big O Notation of Sorting Algorithms')
    plt.legend()
    plt.grid(True)
    plt.savefig('big_o_notation.png')
    plt.show()

# Função para medir o tempo de execução de um algoritmo
def measure_execution_time(algorithm, lst, target=None):
 
    start_time = time.time()  
    if target is not None:
        algorithm(lst, target)  
    else:
        algorithm(lst)  
    end_time = time.time() 
    return end_time - start_time  

# Função para gerar dados de teste aleatórios
def generate_test_data(size):

    return [random.randint(1, 1000) for _ in range(size)]  # Gera uma lista de inteiros aleatórios com o tamanho especificado

# Função para analisar o desempenho dos algoritmos
def analyze_performance(algorithms, sizes, type):

    results = {}  # Dicionário para armazenar os resultados de desempenho

    for name, algorithm in algorithms.items():  
        execution_times = []  
        for size in sizes:  
            if type == 'Sorting':
                lst = generate_test_data(size)  
            elif type == 'Search':
                lst = sorted(generate_test_data(size))  
                target = random.choice(lst)  
            time_taken = measure_execution_time(algorithm, lst, target if type == 'Search' else None)  
            execution_times.append(time_taken)  
        results[name] = execution_times  

    return results  

# Função para gerar gráficos de desempenho
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
# Função principal
def main():

    plot_big_o()

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

    test_sizes = [100, 1000, 10000]  # Tamanhos de lista de teste

    sorting_results = analyze_performance(sorting_algorithms, test_sizes, 'Sorting')  # Analisa o desempenho dos algoritmos de ordenação
    generate_plot(sorting_results, test_sizes, 'Sorting')  # Gera um gráfico para os algoritmos de ordenação

    search_results = analyze_performance(search_algorithms, test_sizes, 'Search')  # Analisa o desempenho dos algoritmos de busca
    generate_plot(search_results, test_sizes, 'Search')  # Gera um gráfico para os algoritmos de busca

if __name__ == "__main__":
    main()
