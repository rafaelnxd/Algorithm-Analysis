import random

class Sorting:


    def bubble_sort(arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    

    def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
    
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    

    

    
arr = [random.randint(0, 100) for _ in range(10)]

print("Bubble sorted array: ", Sorting.selection_sort(arr.copy()))

        
    


# arr1 = [3, 2, 1, 5, 4]
# sorted_arr1 = Sorting.bubble_sort(arr1)
# print(arr1)
    
# random_numbers = [random.randint(1, 1000) for _ in range(1000)]

# print("Lista de 1000 números aleatórios:")
# print(random_numbers[:10])