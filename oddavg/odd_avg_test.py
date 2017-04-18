__author__ = 'ylwoi'

import unittest
import odd_avg


class TestOddAverage(unittest.TestCase):

    def test_odd_average_numbers_1_to_5(self):
        self.assertEqual(odd_avg.odd_average([1, 2, 3, 4, 5]), 3)
