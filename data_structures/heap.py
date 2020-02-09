"""Binary Heap"""
from typing import List


class EmptyHeapError(Exception):
    pass


class MinHeap:
    """Min Heap"""
    @staticmethod
    def _swap(l: List[int], i: int, j: int) -> None:
        """swaps values at indices i, j"""
        l[i], l[j] = l[j], l[i]

    @staticmethod
    def heapify(l: List[int]) -> None:
        pass

    @classmethod
    def from_list(cls, l: List[int]):
        cls.heapify(l)
        return cls(l)

    def __init__(self, heap: List[int] = None):
        self._heap = [] if heap is None else heap

    def __repr__(self):
        return f"MinHeap({self._heap})"

    @property
    def min(self) -> int:
        """Return min value in the heap (peek)"""
        return self.peek()

    def peek(self) -> int:
        """Peek at top of heap"""
        try:
            return self._heap[0]
        except IndexError:
            raise EmptyHeapError("The heap is empty")

    def put(self, x: int) -> None:
        """Add an integer into the heap"""
        self._heap.append(x)

        # bubble up to the correct position
        i = len(self._heap) - 1
        while i > 0:
            p = (i - 1) // 2
            if self._heap[p] < self._heap[i]:
                break

            MinHeap._swap(self._heap, p, i)
            i = p

    def pop(self) -> int:
        """Return min value and remove from heap"""
        if len(self._heap) == 0:
            raise EmptyHeapError("The heap is empty")

        MinHeap._swap(self._heap, 0, len(self._heap) - 1)
        result = self._heap.pop()

        # rebalance heap
        i = 0
        n = len(self._heap)
        while (l := 2*i + 1) < n:
            if (r := 2*i + 2) < n:
                min_child = l if self._heap[l] < self._heap[r] else r
            else:
                min_child = l

            if self._heap[i] <= self._heap[min_child]:
                break

            MinHeap._swap(self._heap, i, min_child)
            i = min_child

        return result
