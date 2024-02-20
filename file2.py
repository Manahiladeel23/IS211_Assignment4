import time
import random


def sequential_search(arr, target):
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == target:
            return True, time.time() - start_time
    return False, time.time() - start_time


def ordered_sequential_search(arr, target):
    arr.sort()  # Ensure the list is sorted
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == target:
            return True, time.time() - start_time
        elif arr[i] > target:
            return False, time.time() - start_time
    return False, time.time() - start_time


def binary_search_iterative(arr, target):
    arr.sort()  # Ensure the list is sorted
    start_time = time.time()
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True, time.time() - start_time
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False, time.time() - start_time


def binary_search_recursive(arr, target):
    arr.sort()  # Ensure the list is sorted
    start_time = time.time()

    def recursive_search(low, high):
        if low > high:
            return False
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            return recursive_search(mid + 1, high)
        else:
            return recursive_search(low, mid - 1)

    result = recursive_search(0, len(arr) - 1)
    return result, time.time() - start_time


def main():
    sizes = [500, 1000, 5000]
    for size in sizes:
        total_time = 0
        for _ in range(100):
            random_list = [random.randint(1, 1000000) for _ in range(size)]
            result, time_taken = sequential_search(random_list, 99999999)
            total_time += time_taken

        average_time = total_time / 100
        print(f"Sequential Search took {average_time:10.7f} seconds on average for size {size}")



if __name__ == "__main__":
    main()

    import time
import random


def insertion_sort(arr):
    start_time = time.time()
    # Insertion sort implementation
    # ...
    return time.time() - start_time


def shell_sort(arr):
    start_time = time.time()
    # Shell sort implementation
    # ...
    return time.time() - start_time


def python_sort(arr):
    start_time = time.time()
    arr.sort()
    return time.time() - start_time


def main():
    sizes = [500, 1000, 5000]
    for size in sizes:
        total_time_insertion = 0
        total_time_shell = 0
        total_time_python_sort = 0

        for _ in range(100):
            random_list = [random.randint(1, 1000000) for _ in range(size)]

            total_time_insertion += insertion_sort(random_list.copy())
            total_time_shell += shell_sort(random_list.copy())
            total_time_python_sort += python_sort(random_list.copy())

        average_time_insertion = total_time_insertion / 100
        average_time_shell = total_time_shell / 100
        average_time_python_sort = total_time_python_sort / 100

        print(f"Insertion Sort took {average_time_insertion:10.7f} seconds on average for size {size}")
        print(f"Shell Sort took {average_time_shell:10.7f} seconds on average for size {size}")
        print(f"Python's Sort took {average_time_python_sort:10.7f} seconds on average for size {size}")


if __name__ == "__main__":
    main()