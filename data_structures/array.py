"""Implements fixed size array in Python"""
from typing import Any, Sequence

class Array:
    """Vanilla Array in Python - esentially wraps list()"""

    @classmethod
    def from_sequence(cls, obj: Sequence[Any]=None):
        return cls(data=obj)

    def __init__(self, size: int=0, data: Sequence[Any]=None):
        self.data = size * [None] if data is None else list(data)
        self.size = len(self.data)

    def __repr__(self):
        return f"{self.__class__.__name__}(size={self.size})"

    def __str__(self):
        return self.data.__str__()

    def __getitem__(self, key):
        return self.data.__getitem__(key)

    def __setitem__(self, key, value):
        return self.data.__setitem__(key, value)

    def __len__(self):
        return self.size
