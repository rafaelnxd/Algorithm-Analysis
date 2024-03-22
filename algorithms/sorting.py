class Sorting:

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    


# arr1 = [3, 2, 1, 5, 4]
# sorted_arr1 = Sorting.bubble_sort(arr1)
# print(arr1)
    
    