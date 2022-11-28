# Made by Yu Cheng
# Student ID = 22302304
import numpy as np
#from median_filter import median_filter
import scipy.io
from scipy.io import wavfile

import scipy
from scipy import signal

import matplotlib
import matplotlib.pyplot as plt

from tqdm import tqdm
import time
from time import sleep


from playsound import playsound

# compute the MSE between the clean.wav and the output.wav
# both audios are 10 sec
def MSE(a, b):
    # docstrings
    MSE = np.mean(np.square(a-b))
    return MSE


# sampling rate and audio signal
fs, sig_degrade = wavfile.read('degraded_cy.wav')
fs_1, sig_detection = wavfile.read('detectionfile_cy.wav')
fs_2, sig_clean = wavfile.read('clean_cy.wav')
plt.subplot(311)
plt.plot(range(len(sig_degrade)), sig_degrade)
plt.title('degraded audio')

# start time and end time
start = time.time()

length = len(sig_detection)

restored_data = sig_degrade

filter_size = 5
# filter size = 3, mse = 0.046
# filter size = 13, mse = 0.389

padding = int(filter_size/2)


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
            sorted_window = np.sort(window)
            mid = sorted_window[(filter_size-1)//2]
            result[i] = mid 
        #print(result)     
        return result


if __name__ == "__main__":
    for i in tqdm(range(0, 10)):
        sleep(0.1)
        for i in range(length):

            if sig_detection[i] > 0:
        #restored_data[i] = median_filter(sig_detection[i - padding :i + padding].tolist(), filter_size)
             restored_data[i-padding: i+padding] = median_filter(
            sig_detection[i - padding:i + padding].tolist(), filter_size)
# end time
end = time.time()
if i + 1 == length:
    print('done')

data_for_test = restored_data        
result = median_filter(data_for_test, filter_size)
print(result) 

if __name__ == "__main__":
    print("median_filter execution time: {}s".format(end-start))
    print("Using median filter, clean VS output MSE: {}".format(
    MSE(sig_clean, restored_data)))

plt.subplot(312)
plt.plot(range(len(restored_data)), restored_data)
plt.title('output')

#wavfile.write("output_median_filter.wav", fs, restored_data)

#playsound("output_median_filter.wav")

plt.subplot(313)
plt.plot(range(len(sig_clean)), sig_clean)
plt.title("clean audio")
plt.subplots_adjust(hspace=1)
plt.show()



#############################
import unittest
from median_filter import median_filter
data_for_test = restored_data
class TestMyCode(unittest.TestCase):
    def test_median_filter(self):
        data_for_test = restored_data
        result = median_filter(data_for_test, filter_size)
        out = scipy.signal.medfilt(data_for_test, kernel_size = filter_size)
        #self.assertTrue((result == out).all())
        check = np.array_equal(out, result)
if __name__ == "__main__":
    unittest.main()

 

