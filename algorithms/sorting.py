import random
import time

class Sorting:

    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    @staticmethod
    def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
    
    @staticmethod
    def insertion_sort(arr): 
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    @staticmethod
    def mergeSort(arr):
        aux = [0] * len(arr)
        Sorting.mergesort(arr, aux, 0, len(arr) - 1)

    @staticmethod
    def merge(arr, aux, left, mid, right):
        
        for k in range(left, right + 1):
            aux[k] = arr[k]

        i = left
        j = mid + 1

        for k in range(left, right + 1):
            if i > mid:
                arr[k] = aux[j]
                j += 1
            elif j > right:
                arr[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                arr[k] = aux[j]
                j += 1
            else:
                arr[k] = aux[i]
                i += 1

    @staticmethod
    def mergesort(arr, aux, left, right):
        if right <= left:
            return
        
        mid = (left + right) // 2

        #
        Sorting.mergesort(arr, aux, left, mid)

       
        Sorting.mergesort(arr, aux, mid + 1, right)


        Sorting.merge(arr, aux, left, mid, right)

    @staticmethod
    def quick_sort(arr):
        Sorting.quicksort(arr, 0, len(arr) - 1)
    
    @staticmethod
    def quicksort(arr, low, high):
        if low < high:

            # Pivot
            pivot = Sorting.partition(arr, low, high)

            # Ordering the elements before and after the pivot
            Sorting.quicksort(arr, low, pivot - 1)
            Sorting.quicksort(arr, pivot + 1, high)

    @staticmethod
    def partition(arr, low, high):
        pivot =  arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1 ], arr[high] = arr[high], arr[i + 1]
        return i + 1

  
    

arr = [random.randint(0, 100) for _ in range(500)]

arr2 = [12, 30, 32, 13, -1, -2, 5, 9, 56]

def test_bubblesort(arr):
    time1 = time.time()
    Sorting.bubble_sort(arr)
    time2 = time.time()
    return time2 - time1

def test_selectionsort(arr):
    time1 = time.time()
    Sorting.selection_sort(arr)
    time2 = time.time()
    return time2 - time1

def test_mergesort(arr):
    time1 = time.time()
    Sorting.mergeSort(arr)
    time2 = time.time()
    return time2 - time1

def test_quicksort(arr):
    time1 = time.time()
    Sorting.quick_sort(arr)
    time2 = time.time()
    return time2 - time1


print("Time to execute Bubble Sort's algorithm was: ", test_bubblesort(arr))
print("Time to execute Merge Sort's algorithm was: ", test_mergesort(arr))
print("Time to execute Selection Sort's algorithm was: ", test_quicksort(arr))
print("Time to execute Seleection Sort's algorithm was: ", test_selectionsort(arr))




# print("Original List", arr2)
# Sorting.selection_sort(arr2)
# print("Ordered List", arr2)

# print("Bubble sorted array: ", Sorting.selection_sort(arr.copy()))

        
    


# arr1 = [3, 2, 1, 5, 4]
# sorted_arr1 = Sorting.bubble_sort(arr1)
# print(arr1)
    
# random_numbers = [random.randint(1, 1000) for _ in range(1000)]

