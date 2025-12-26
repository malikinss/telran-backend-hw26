# ./tests/test_my_array.py

import unittest

from src import MyArray

LENGTH: int = 1_000_000_000


class TestMyArray(unittest.TestCase):
    """
    Unit tests for the `MyArray` class.

    These tests verify:
        - Correct behavior with extremely large array size
        - Setting and getting values at specific indices
        - setAll functionality
        - Index boundary validation
    """

    def setUp(self):
        self.array = MyArray(LENGTH)
        self.array.set(0, 100)
        self.array.set(LENGTH // 2, -60)
        self.array.set(LENGTH - 1, 80)

    def test_initial_values(self):
        """
        Test initial values after selective set operations.
        """
        test_data = [
            # index, expected value
            (1, None),
            (0, 100),
            (LENGTH - 1, 80),
            (LENGTH // 2, -60),
        ]

        for index, expected in test_data:
            print(f"Testing get({index}), expecting {expected}")
            with self.subTest(index=index):
                self.assertEqual(expected, self.array.get(index))

    def test_set_all(self):
        """
        Test that setAll overrides all values.
        """
        self.array.set_all(50)

        test_data = [
            1,
            0,
            LENGTH - 1,
            LENGTH // 2,
        ]

        for index in test_data:
            print(f"Testing get({index}) after setAll, expecting 50")
            with self.subTest(index=index):
                self.assertEqual(50, self.array.get(index))

    def test_index_errors(self):
        """
        Test that invalid indices raise IndexError for get and set.
        """
        test_data = [
            lambda: self.array.get(-1),
            lambda: self.array.get(LENGTH),
            lambda: self.array.set(-1, 10),
            lambda: self.array.set(LENGTH, 10),
        ]
        for operation in test_data:
            with self.subTest(operation=operation):
                with self.assertRaises(IndexError):
                    operation()


if __name__ == "__main__":
    print("Running MyArray tests...")
    unittest.main()
