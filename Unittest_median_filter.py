# Made by Yu Cheng
# Student ID = 22302304

import unittest
import numpy as np
from median_filter import median_filter
import scipy


class TestMyCode(unittest.TestCase):
    def test_median_filter(self):
        data_for_test = [1,    2,    3,    6,    10,    7,    2,    1]
        window = 3
        result = median_filter(data_for_test,window)
        out = scipy.signal.medfilt(data_for_test, kernel_size=window)
        print("out : ", out)
        print("result :", result)
        self.assertTrue((result == out).all())


if __name__ == "__main__":
    unittest.main()
    