
import random
import time

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        deterministic_quick_sort(arr, low, p - 1)
        deterministic_quick_sort(arr, p + 1, high)

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def randomized_quick_sort(arr, low, high):
    if low < high:
        p = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, p - 1)
        randomized_quick_sort(arr, p + 1, high)

arr = list(map(int, input("Enter array elements separated by spaces: ").split()))

arr1 = arr.copy()
arr2 = arr.copy()

start = time.perf_counter()
deterministic_quick_sort(arr1, 0, len(arr1) - 1)
time1 = time.perf_counter() - start

start = time.perf_counter()
randomized_quick_sort(arr2, 0, len(arr2) - 1)
time2 = time.perf_counter() - start

print("\nDeterministic Quick Sort:", arr1)
print("Execution time:", time1, "seconds")

print("\nRandomized Quick Sort:", arr2)
print("Execution time:", time2, "seconds")

print("\nBoth sorted correctly:", arr1 == arr2)
