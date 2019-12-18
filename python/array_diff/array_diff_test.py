import unittest
from unittest import TestCase

from array_diff import array_diff


class ArrayDiffTest(TestCase):

    def test_equals_arrays(self):
        for i in range(5):
            result = array_diff([i], [i])
            self.assertEqual([], result)
    
    def test_arrays(self):
        result = array_diff([1, 2, 3], [1])
        self.assertEqual([2, 3], result)

        result = array_diff([1, 2, 3], [1, 2])
        self.assertEqual([3], result)

        result = array_diff([1, 2, 3], [1, 2, 3])
        self.assertEqual([], result)

        result = array_diff([1, 2, 3, 4, 5, 6], [1, 2])
        self.assertEqual([3, 4, 5, 6], result)


if __name__ == '__main__':
    unittest.main()