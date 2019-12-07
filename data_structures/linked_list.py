"""Implements LinkedList in vanilla Python"""
from typing import Any, Sequence
from .exceptions import NoSuchElementException


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"{self.__class__.__name__}(data={self.data})"

class LinkedList:
    """Vanilla Linked List"""

    @classmethod
    def from_sequence(cls, obj: Sequence[Any]):
        head = Node(obj[0])
        tmp = head
        for x in obj[1:]:
            tmp.next = Node(x)
            tmp = tmp.next

        return cls(head)

    def __init__(self, head: Node=None):
        self.head = head

    def __repr__(self):
        return f"{self.__class__.__name__}(head={self.head})"

    def print_all(self):
        tmp = self.head
        print(f"{self.__class__.__name__}(")
        while tmp is not None:
            print(f"\t{tmp} ->")
            tmp = tmp.next
        print(")")

    def get_first(self):
        """Get First Item in list
            Complexity: O(1)"""
        if self.head is None:
            raise NoSuchElementException(f"The {self.__class__.__name__} is empty")
        return self.head.data

    def get_last(self):
        """Get Last Item in list
            Complexity: O(n)"""
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        return tmp.data

    def contains(self, data: Any):
        """Returns true if data in list
            Complexity: O(n)"""
        tmp = self.head
        while tmp is not None:
            if tmp.data == data:
                return True
            tmp = tmp.next
        return False

    def insert_first(self, data: Any):
        """Insert data into front of list
            Complexity: O(1)"""
        tmp = self.head
        self.head = Node(data)
        self.head.next = tmp

    def insert_last(self, data: Any):
        """Insert data into back of list
            Complexity: O(n)"""
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = Node(data)
