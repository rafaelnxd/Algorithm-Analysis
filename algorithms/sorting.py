import random
import time

class Sorting:


    ## Algorithms Methods # #

        # Bubble Sort #

    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

        # Selection Sort #
    
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
    
        # Insertion Sort #
    
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
    
        # Merge Sort #
    
    @staticmethod
    def mergeSort(arr):
        aux = [0] * len(arr)
        Sorting.mergesort(arr, aux, 0, len(arr) - 1)
        return arr

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

        # Quick Sort #

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

  
