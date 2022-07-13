"""
Author: Derek Gauger
Date: 07/07/2022

Purpose:
I wanted to start putting more useful things into my GitHub. I recently took an algorithms course where
I had to write each of these sorting algorithms from scratch. I figured I could do it again as practice,
and it would be a useful thing to have for the future, so I don't have to keep remaking them

Description:
This file is full of the following fully functional sorting algorithms:
 - insertion
 - selection
 - bubble
 - merge
 - quick
 - counting
"""
import random
import time


class SortingAlgorithms:
    INSERTION = 0
    SELECTION = 1
    BUBBLE = 2
    MERGE = 3
    QUICK = 4
    COUNTING = 5


class OrderTypes:
    RANDOM = 0
    ORDERED = 1
    REVERSED = 2


"""
Insertion sort goes through each of the elements in the list starting at index 1 (these are the keys)
It takes that key and checks with all the values to the left of the key to
see if there are any large values than that key.

This algorithm works from left to right on an array {start} [5,2,3,7,8,42,1] {End}
Steps:
1. Set key = 2
2. Compare with the values to the left [5]
3. Swap the values of 2 and 5 --> restart process
4. Set key = 3
5. Compare with the values to the left [2, 5]
6. 5 is larger than 3, 2 is less than 3. Swap the values of 3 and 5
6. Repeat until completion
"""
def insertion_sort(array):
    for i in range(1, len(array)):

        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key


"""
Selection sort works by passing through the list n number of times and getting the smallest value's index of the
remaining unsorted values everytime. The values to the left of the key are already sorted, the values to the right
are the ones that are being evaluated.

Example List: [5,2,3,8,6,42,1]
Steps:
1. Find smallest value '1' in the list, swap values with the current key '5'... List: [1,2,3,8,6,42,5]
2. Find the smallest unsorted value '2'. It is already in the correct position.
3. Find the smallest unsorted value '3'. It is already in the correct position.
4. Find the smallest unsorted value '5', swap values with the current key '8'... List: [1,2,3,5,6,42,8]
5. Continue process until sorted
"""
def selection_sort(array):
    for i in range(len(array)):
        mindex = i
        starting_index = i + 1
        for j in range(starting_index, len(array)):
            if array[mindex] > array[j]:
                mindex = j

        array[i], array[mindex] = array[mindex], array[i]


"""
Bubble sort works by comparing two values at a single time. It will go through the list n times,
comparing 2 values at a time, eventually the list will be sorted

Example List: [7,4,5,1,8]
Steps:
1. Compare 7 and 4, swap them... List: [4,7,5,1,8]
2. Compare 7 and 5, swap them... List: [4,5,7,1,8]
3. Compare 7 and 1, swap them... List: [4,5,1,7,8]
4. Compare 7 and 8, do nothing
5. Compare 4 and 5, do nothing
6. Compare 5 and 1, swap them... List: [4,1,5,7,8]
7. Compare 5 and 7, do nothing
8. Compare 7 and 8, do nothing
9. Compare 4 and 1, swap them... List: [1,4,5,7,8]
10. It will keep going with the pattern, but this will be the end result list.
"""
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(1, len(array)):
            first = array[j - 1]
            second = array[j]

            if first > second:
                print(first, second)
                array[j], array[j - 1] = array[j - 1], array[j]


"""
Merge sort is a divide/conquer/combine sorting algorithm. The idea is to divide the array into two parts,
then call the merge_sort method again on those sublists to keep dividing them until the arrays are as small as
they can be. Then it will take those subarrays and overwrite the original array's values with the values sorted.

Example List: [7,5,4,8,9]
Steps:
1. Divide list into [7,5,4] and [8,9]
2. Divide lists into [7,5], [4], [8], and [9]
3. Divide lists into [7], [5], [4], [8], and [9]
4. Check the values in [7] and [5] and combine them to be [5,7]
5. Check the values in [5,7] and [4] and combine them to be [4,5,7]
6. Check the values in [8] and [9] and combine them to be [8,9]
7. Check the values in [4,5,7] and [8,9] and combine them to be [4,5,7,8,9]
"""
def merge_sort(array):
    # Make sure the array is populated
    if len(array) > 1:

        # Divide
        r = len(array) // 2
        left_array = array[:r]
        right_array = array[r:]

        # Conquer
        merge_sort(left_array)
        merge_sort(right_array)

        # Combine
        _merge(array, left_array, right_array)


def _merge(array, left, right):
    i = j = k = 0

    # Iterate through each list (left and right)
    # Replace the value of each index in array with the next highest value
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    # Check if any element are left in the left array
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    # Check if any elements are left in the right array
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


"""
Quick sort is a divide and conquer algorithm. It works by partitioning the array around a certain value.
It puts the smaller elements on the left side of the pivot element and the larger element on the right side.

Example List: [8,4,6,7,1]
Steps:
1. Partition by setting the pivot = 1
2. Iterate through the list, if > 1 put on the right, if < 1 put on the left... List: [1,8,4,6,7]
3. Split into sublists and repeat the process... Sublists = [], [8,4,6,7]

4. Partition the non-empty list by setting the pivot = 7
5. Iterate through the list, if > 7 put on the right, if < 7 put on the left... List: [1,4,6,7,8]
6. This list is already sorted, but repeat until sorted.
"""
def quick_sort(array):
    _quick_sort_helper(array, 0, len(array) - 1)


def _quick_sort_helper(array, low, high):
    if high > low:

        # Divide
        pivot_index = _partition(array, low, high)

        # Conquer
        _quick_sort_helper(array, low, pivot_index - 1)
        _quick_sort_helper(array, pivot_index + 1, high)


def _partition(array, low, high):

    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if pivot > array[j]:
            i += 1
            array[i], array[j] = array[j], array[i]

    i += 1
    array[i], array[high] = array[high], array[i]
    return i


"""
Counting sort is an algorithm that uses indexes in arrays to store the number of elements that correspond to that 
index. Sounds a little confusing. Here is an example.

Original List: [2,5,6,4,5,1]
Indexes List: [0,1,1,0,1,2,1]
Indexes List after refactoring: [0,1,2,2,3,5,6]
"""
def counting_sort(array):
    indexes = []
    maximum_index = max(array)
    for i in range(maximum_index + 1):
        indexes.append(0)

    for value in array:
        indexes[value] += 1

    for i in range(1, len(indexes)):
        first = indexes[i - 1]
        second = indexes[i]

        indexes[i] = first + second

    output = []

    for i in range(len(indexes)):
        last_num = 0
        if i != 0:
            last_num = indexes[i - 1]
        iterations = indexes[i]
        while iterations - last_num > 0:
            output.append(i)
            iterations -= 1

    for i in range(len(array)):
        array[i] = output[i]


"""
This benchmarking method takes in 4 parameters:
    n : The number of elements to sort
    sorting_algorithm : A SortingAlgorithms class property value to determine which algorithm to use for sorting
    order_type : (REVERSE, ORDERED, RANDOM) Used to determine what order the unsorted list should be in
    pt : Boolean to determine whether or not to print the elapsed time out
"""
def benchmark(n, sorting_algorithm, order_type, pt=True):
    unsorted_list = []
    for i in range(n):
        if order_type == OrderTypes.ORDERED:
            unsorted_list.append(i)

        elif order_type == OrderTypes.REVERSED:
            unsorted_list.append(n - i - 1)

        elif order_type == OrderTypes.RANDOM:
            random_num = random.randint(0, n - 1)
            unsorted_list.append(random_num)

    sorted_list = sorted(unsorted_list)

    start = end = 0
    algorithm_string = ""

    if sorting_algorithm == SortingAlgorithms.INSERTION:
        start = time.perf_counter()
        insertion_sort(unsorted_list)
        end = time.perf_counter()
        algorithm_string = "Insertion Sort"

    elif sorting_algorithm == SortingAlgorithms.SELECTION:
        start = time.perf_counter()
        selection_sort(unsorted_list)
        end = time.perf_counter()
        algorithm_string = "Selection Sort"

    elif sorting_algorithm == SortingAlgorithms.BUBBLE:
        start = time.perf_counter()
        bubble_sort(unsorted_list)
        end = time.perf_counter()
        algorithm_string = "Bubble Sort"

    elif sorting_algorithm == SortingAlgorithms.MERGE:
        start = time.perf_counter()
        merge_sort(unsorted_list)
        end = time.perf_counter()
        algorithm_string = "Merge Sort"

    elif sorting_algorithm == SortingAlgorithms.QUICK:
        start = time.perf_counter()
        quick_sort(unsorted_list)
        end = time.perf_counter()
        algorithm_string = "Quick Sort"

    elif sorting_algorithm == SortingAlgorithms.COUNTING:
        start = time.perf_counter()
        counting_sort(unsorted_list)
        end = time.perf_counter()
        algorithm_string = "Counting Sort"

    elapsed_time = end - start

    if pt:
        if sorted_list == unsorted_list:
            print("{} - Elapsed Time: {} seconds - Correct".format(algorithm_string, elapsed_time))
        else:
            print("{} - Elapsed Time: {} seconds - Incorrect".format(algorithm_string, elapsed_time))

    return elapsed_time
   
