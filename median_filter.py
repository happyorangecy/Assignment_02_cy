# Made by Yu Cheng
# Student ID = 22302304
import numpy
import scipy
from scipy import signal
import copy

def median_filter(data_list, filter_size):
    """
    :for data_list: [1,2,3,6,10,7,2,1] 
    :for filter_size: int odd number (= 3)
    :return: must be a list
    """
    if (filter_size % 2) == 0 or filter_size <= 0:
        print("filter_size should be odd")
        return None
    else:
        result = [0]*len(data_list)
        data_new = copy.deepcopy(data_list)
        """
         :for data_list: [1,2,3,6,10,7,2,1] 
         :for data_new : copy data_list and exist as a seperate data
         :Result: 
         :      changing data_list will not affect data_new
         :      be useful in comparing when unittest
         """

        padding = int(filter_size/2)
        
        for i in range(padding):
            #add 0 from the first location
            data_new.insert(0, 0)
            #add 0 at the last location
            data_new.append(0)
            
        for i in range(len(result)):
            window = data_new[i:i+filter_size]
            # change the list in correct order
            sorted_window = sorted(window)
            mid = sorted_window[(filter_size-1)//2]
            result[i] = mid
            print(result)

        return result

if __name__ == "__main__":
    test_list = [1,    2,    3,    6,    10,    7,    2,    1]

    # out = scipy.signal.medfilt(test_list, kernel_size=3)
    # print("out : ", out)

    # result = median_filter(test_list, 3)
    # print("result :", result)

    # compare = out == result
    # equal = compare.all()
    # print(equal)

from median_filter import median_filter
import unittest

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
    