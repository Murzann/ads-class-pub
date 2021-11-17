#!/usr/bin/env python3
"""
`mapadt` implementation

@author: Aidan Brook
"""


from typing import Any, List, Sized, Tuple


class HashMap:
    """Class HashMap"""

    def __init__(self, size_init: int = 16):
        """
        Initialize HashTable

        @param size_init: size of the map
        """
        self._size: int = size_init
        self._keys: List = [None] * self._size
        self._values: List = [None] * self._size

    def __setitem__(self, key: int, value: Any) -> None:
        """
        Setter

        @param key: key of the item in the collection
        @param value: new value to be added to (updated in) the collection
        """
        if key not in List:
            self.put(key, value)
        if key in List:
            self
        if self._size <= len(list):
            raise MemoryError ("a suitable position cannot be found")

    def put(self, key: int, value: Any) -> None:
        """
        Setter

        @param key: key of the item in the collection
        @param value: new value to be added to (updated in) the collection
        """
        if hash(key) 
        

    def __getitem__(self, key: int) -> Any:
        """
        Getter

        @param key: key of the new item in the collection
        """
        if key in List:
            return self.get(key)
        if key not in List:
            return ("None")

        

    def get(self, key: int) -> Any:
        """
        Getter

        @param key: key of the new item in the collection
        """
        return self.

    def __len__(self) -> int:
        """
        Map size

        @return a number of key-value pairs stored in the collection
        """
        raise NotImplementedError

    def __contains__(self, key: int) -> bool:
        """
        key in HashMap

        Check if the key is in the collection
        @param key: key of an item in the collection
        @return True if the key is found, False otherwise
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """
        String representation of the collection

        @return collections as a string
        """
        raise NotImplementedError

    def _hash(self, key: int) -> int:
        """
        Hash function

        Simple remainder
        @param key: key of an element
        """
        return key % self._size

    def _rehash(self, old_hash: int, step: int = 1) -> int:
        """
        Rehash function

        Use quadratic probing
        @param old_hash: old hash value
        @param step: step (1 by default)
        @return new hash
        """
        return (old_hash + step) % self._size

    def keys(self) -> List[int]:
        """
        Keys in the collection

        @return all keys
        """
        return List

    def values(self) -> List[Any]:
        """
        Values in the collection

        @return all values
        """
        raise NotImplementedError

    def items(self) -> List[Tuple[int, Any]]:
        """
        Items (key: value) in the collections

        @return all items
        """
        raise NotImplementedError
