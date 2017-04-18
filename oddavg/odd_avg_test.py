__author__ = 'ylwoi'

import unittest
import odd_avg


class TestOddAverage(unittest.TestCase):

    def test_odd_average_numbers_1_to_5(self):
        self.assertEqual(odd_avg.odd_average([1, 2, 3, 4, 5]), 3)

    def test_odd_average_only_odd_numbers(self):
        self.assertEqual(odd_avg.odd_average([1, 5, 3, 7, 9]), 5)

    def test_odd_average_only_even_numbers(self):
        self.assertEqual(odd_avg.odd_average([2, 2, 6, 4, 8]), 0)
