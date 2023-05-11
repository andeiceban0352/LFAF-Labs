#Andrei Ceban FAF-211

import matplotlib.pyplot as plt
import time
import random


#  Heap sort
# ------------------------------------------------------------------------------------------------------------------------
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)


# Insertion Sort
# ------------------------------------------------------------------------------------------------------------------------
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Quick Sort
# ------------------------------------------------------------------------------------------------------------------------
def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    return quickSort(left) + [pivot] + quickSort(right)


# Quick Sort
# ------------------------------------------------------------------------------------------------------------------------
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


#Calculate the time for each function
def calc_quicksort_time(array):
    start_time = time.time()
    quickSort(array.copy())
    end_time = time.time()

    return end_time - start_time

def calc_mergesort_times(array):
    start_time = time.time()
    mergeSort(array.copy())
    end_time = time.time()

    return end_time - start_time

def calc_heapSort_time(array):
    start_time = time.time()
    heapSort(array.copy())
    end_time = time.time()

    return end_time - start_time

def calc_insertionSort_time(array):
    start_time = time.time()
    insertionSort(array.copy())
    end_time = time.time()

    return end_time - start_time

quick = []
merge = []
heap  = []
insertion = []


# Generate random arrays to sort
arr = [10, 100,1000,2000, 5000, 10000]
arrays = {}


for size in arr:
    arrays[size] = [random.randint(1, size) for x in range(size)]

    quick.append(calc_quicksort_time(arrays[size]))
    merge.append(calc_mergesort_times(arrays[size]))
    heap.append(calc_heapSort_time(arrays[size]))
    insertion.append(calc_insertionSort_time(arrays[size]))

algorithms = ["Heap sort","Insertion sort", "Merges ort", "Quick sort" ]
time = [heap[-1], insertion[-1], merge[-1], quick[-1]]
plt.bar(algorithms, time, label="Heapsort", )
plt.legend()
plt.xlabel("Algorithms ")
plt.ylabel("Runtime (Seconds)")
plt.show()

plt.plot(arr, heap, label="Heapsort")
plt.plot(arr, insertion, label="insertionsort")
plt.plot(arr, merge, label="Mergesort")
plt.plot(arr, quick, label="Quicksort")
#
plt.legend()
plt.xlabel("Array Size")
plt.ylabel("Runtime (Seconds)")

plt.show()