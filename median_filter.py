# Made by Yu Cheng
# Student ID = 22302304
import numpy
import scipy
from scipy import signal


def median_filter(data_list, filter_size):
    if (filter_size % 2) == 0 or filter_size <= 0:
        print("filter_size should be odd")
        return None
    else:
        result = [0]*len(data_list)
        padding = int(filter_size/2)
        # if padding > 0:
        for i in range(padding):
            data_list.insert(0, 0)
            data_list.append(0)
            # print(len(result))
        for i in range(len(result)):
            window = data_list[i:i+filter_size]
            sorted_window = sorted(window)
            mid = sorted_window[(filter_size-1)//2]
            result[i] = mid
            print(result)
        return result

#if name == "main": 
test_list = [1,    2,    3,    6,    10,    7,    2,    1]

out = scipy.signal.medfilt(test_list, kernel_size=3)
print("out : ", out)

result = median_filter(test_list, 3)
print("result :", result)

compare = out == result
equal = compare.all()
print(equal)
