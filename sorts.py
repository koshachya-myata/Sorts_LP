import time
import random

def create_rnd_list_int(size, start, end):
    a = [0] * size
    for i in range(0, size):
        a[i] = random.randint(start, end)
    return a
def create_rnd_list_float(size, start, end):
    a = [0] * size
    for i in range(0, size):
        a[i] = random.uniform(start, end)
    return a

def bubble_sort_time(arr): # bubble
    time_stamp = time.time()
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return time.time() - time_stamp

def insert_sort_time(arr): #insert
    time_stamp = time.time()
    for i in range(len(arr)):
        j = i - 1
        key = arr[i]

        while arr[j] > key and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return time.time() - time_stamp
def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

def quick_sort_time(arr):
    time_stamp = time.time()
    quick_sort(arr)
    return time.time() - time_stamp

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:

            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)
def merge_sort_time(arr):
    time_stamp = time.time()
    merge_sort(arr)
    return time.time() - time_stamp

def count_sort(arr, type_of_nums):
    if type_of_nums == "int":
        t = count_sort_int_time(arr)
    else:
        t = count_sort_float_time(arr)
    return t
def count_sort_int_time(arr):

    time_stamp = time.time()
    min_num = min(arr)
    scope = max(arr) + abs(min_num) + 1
    C = [0] * scope
    for x in arr:
        C[x + abs(min_num)] += 1
    arr[:] = []
    for number in range(scope):
        arr += [number-  abs(min_num)] * C[number]
    return time.time() - time_stamp

def count_sort_float_time(arr):
    time_stamp = time.time()
    d = dict()
    for el in arr:
        if el not in d:
            d[el] = 1
        else:
            d[el] += 1
    list_keys = list(d.keys())
    merge_sort(list_keys) # Any sort
    arr[:] = []
    for i in list_keys:
        arr += [i] * d[i]
    return time.time() - time_stamp


