"""Implements Hash Table in Python

    NOTE: this is for practice and understanding. You'll want to use builtin
        dict() object for real-life applications

    with help from the Python dict() source:
        http://svn.python.org/projects/python/trunk/Objects/dictobject.c
    and from Laurent Luce's Blog:
        https://www.laurentluce.com/posts/python-dictionary-implementation/
"""
import collections
from collections import namedtuple
from typing import Any, Hashable

from .array import Array


class HashTableEntry(namedtuple('HashTableEntry', ('key', 'value', 'key_hash'))):
    __slots__ = ()
    def __new__(cls, key: Hashable, value: Any):
        return super(HashTableEntry, cls).__new__(cls, key, value, hash(key))

class _HashTable(collections.abc.MutableMapping):
    SCALE_THRESHOLD = 5e5
    PRETURB_SHIFT = 5

    def _get_mask_value(self, size):
        return size - 1

    def _get_resized_table(self):
        used = self.__len__()
        min_used = 4 * used if used < HashTable.SCALE_THRESHOLD else 2 * used

        new_size = len(self._table)
        while new_size < min_used: new_size << 1
        return Array(new_size)

    def _get_index(self, key):
        return hash(key) & (len(self._table) - 1)

    def _lookup(self, key: Hashable):
        initial = self._table[self._get_index(key)]
        if initial.key is None or initial.key == key:
            return initial

        # probe
        raise ValueError('not implemented')

    def __init__(self, **kwargs):
        self._table = Array(len(kwargs))
        for key, value in kwargs.items():
            self.__setitem__(key, value)

    def __len__(self):
        return len(self.keys())

    def __setitem__(self, key, value):
        pass

    def __getitem__(self, key):
        return self._lookup(key).value

    def __delitem__(self, key):
        pass

    def __iter__(self):
        pass


class HashTable(collections.abc.MutableMapping):
    SCALE_THRESHOLD = 5e5
    PRETURB_SHIFT = 5

    def _get_mask_value(self, size):
        return size - 1

    def _get_resized_table(self):
        used = self.__len__()
        min_used = 4 * used if used < HashTable.SCALE_THRESHOLD else 2 * used

        new_size = len(self._table)
        while new_size < min_used: new_size << 1
        return Array(new_size)

    def __init__(self, **kwargs):
        self._table = Array(len(kwargs))
        for key, value in kwargs.items():
            self.__setitem__(key, value)

    def __len__(self):
        return len(self.keys())

    def __setitem__(self, key, value):
        pass

    def __getitem__(self, key):
        pass

    def __delitem__(self, key):
        pass

    def __iter__(self):
        pass
