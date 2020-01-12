"""Module containing sorting algorithms implemented in Python"""
_MEDIAN_OF_THREE_THRESHOLD = 30  # should be emperically chosen


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
    """Merge Sort (recursive implementation)

    Features:
        - stable

    Complexities:
        Time:
            Best:
            Average:
            Worst:
        Space: O(N)
    """
    def merge(L, R):
        n, m = len(L), len(R)
        while True:
            if L[n - 1] > R[m - 1]:
                n -= 1
                arr[n + m] = L[n]
                if n == 0:
                    arr[:m] = R[:m]
                    return
            else:
                m -= 1
                arr[n + m] = R[m]
                if m == 0:
                    arr[:n] = L[:n]
                    return

    if len(arr) > 1:
        mid = len(arr) // 2
        # these are copies
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)
        merge(L, R)


def _partition(arr, lo, hi):
    """unlike lomuto, results in best case if array is sorted and handles
        repeated elements well

    overview: work inward from ends, inverting if elements should be swapped
    """
    # median of 3 partitioning
    def median_of_three():
        # place median at end and return median(low, high, middle)
        mid = (hi + lo) // 2
        if arr[hi] < arr[lo]:
            arr[lo], arr[hi] = arr[hi], arr[lo]
        if arr[mid] < arr[lo]:
            arr[lo], arr[mid] = arr[mid], arr[lo]
        if arr[hi] < arr[mid]:
            arr[hi], arr[mid] = arr[mid], arr[hi]
        return arr[mid]

    if hi - lo > _MEDIAN_OF_THREE_THRESHOLD:
        pivot = median_of_three()
    else:
        # choose middle
        pivot = arr[(hi + lo) // 2]

    i, j = lo - 1, hi + 1
    while True:
        while True:
            # move inward from start
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            # move inward from end
            j -= 1
            if arr[j] <= pivot:
                break
        if i >= j:
            return j

        # swap
        arr[i], arr[j] = arr[j], arr[i]


def _quick_sort_recursive(arr, lo, hi):
    """recursive quick sort helper.
    lo: starting index
    hi: ending index
    """
    if lo < hi:
        pi = _partition(arr, lo, hi)

        _quick_sort_recursive(arr, lo, pi)
        _quick_sort_recursive(arr, pi + 1, hi)


def quick_sort(arr):
    """Merge Sort

    Features:

    Complexities:
        Time:
            Best:
            Average:
            Worst:
        Space: O(N)
    """
    _quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr


def heap_sort(arr):
    pass


def tim_sort(arr):
    """Hybrid insertion sort and merge sort.

    Features:
    - take advantage of quadratic time for small arrays
    - stable (that's why we use merge sort)
    """
