"""Module containing sorting algorithms implemented in Python"""


def insertion_sort(arr, reverse=False):
    """Insertion Sort.

    Features:
        - quadratic: Do not use for larger arrays (say 10).
        - adaptive: efficient for near sorted arrays
        - stable
        - online
        - in place

    Complexities:
        Time:
            Best: O(N)
            Average: O(N^2)
            Worst: O(N^2)
        Space: O(1)
    """
    def stop_swap(j):
        """given an index, is the value at the index sorted?"""
        if reverse:
            return arr[j - 1] > arr[j]
        return arr[j - 1] < arr[j]

    # start at the second element in the array
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if stop_swap(j):
                break

            # swap left
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


def merge_sort(arr):
    pass


def quick_sort(arr):
    pass


def heap_sort(arr):
    pass
