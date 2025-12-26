# ./src/my_array.py

from typing import Generic, TypeVar, Dict, Optional

T = TypeVar("T")


class MyArray(Generic[T]):
    """
    An array-like structure optimized for setting all values at once.

    Supports:
    - O(1) set_all
    - O(1) set by index
    - O(1) get by index

    Internally stores only overridden indices.
    """

    def __init__(self, size: int) -> None:
        """
        Initializes the array with a fixed size.

        Args:
            size (int): Number of elements in the array.

        Raises:
            ValueError: If size is less than 1.
        """
        if size < 1:
            raise ValueError("Array size must be at least 1")

        self._size: int = size
        self._default_value: Optional[T] = None
        self._overrides: Dict[int, T] = {}

    def set_all(self, value: T) -> None:
        """
        Sets all elements of the array to the same value.

        Args:
            value (T): Value to assign to all indices.
        """
        self._default_value = value
        self._overrides.clear()

    def set(self, index: int, value: T) -> None:
        """
        Sets a value at a specific index.

        Args:
            index (int): Index to update.
            value (T): Value to set.

        Raises:
            IndexError: If index is out of bounds.
        """
        self._check_index(index)
        self._overrides[index] = value

    def get(self, index: int) -> Optional[T]:
        """
        Returns the value at a specific index.

        Args:
            index (int): Index to retrieve.

        Returns:
            T: Stored value or default value if not overridden.

        Raises:
            IndexError: If index is out of bounds.
        """
        self._check_index(index)
        res = self._overrides.get(index, self._default_value)
        return res

    def _check_index(self, index: int) -> None:
        """
        Validates index bounds.

        Args:
            index (int): Index to validate.

        Raises:
            IndexError: If index is out of bounds.
        """
        if not (0 <= index < self._size):
            raise IndexError(index)
