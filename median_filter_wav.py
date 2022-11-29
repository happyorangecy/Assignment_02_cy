# Made by Yu Cheng
# Student ID = 22302304

from scipy.io import wavfile
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from playsound import playsound
import tqdm
import scipy
from tqdm import tqdm
import time
from time import sleep


def MSE(a,b):
    """
    :for a: numpy array 1D []
    :for b: numpy array 1D []
    :the size of a and b must be equal
    :return: MSE
    """
    MSE = np.mean(np.square(a - b))
    return MSE

#Sampling Rate and signal
fs, sig_degraded = wavfile.read('degraded_cy.wav')
fs_1, sig_detection = wavfile.read('detectionfile_cy.wav')
fs_2, sig_clean = wavfile.read('clean_cy.wav')

plt.subplot(311)
plt.plot(range(len(sig_degraded)),sig_degraded)
plt.plot(range(len(sig_detection)),sig_detection)
plt.title("Degraded")



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
            #print(result)
        return result

filter_size = 13
# filter_size = 1, clean VS output MSE = 0.0280, execution time = 4.74s
# filter_size = 3, clean VS output MSE = 0.4106, execution time = 4.68s
# filter_size = 5, clean VS output MSE = 0.7322, execution time = 4.77s
# filter_size = 7, clean VS output MSE = 0.8781, execution time = 4.78s
# filter_size = 9, clean VS output MSE = 0.1066, execution time = 4.80s
# filter_size = 11, clean VS output MSE = 0.4279, execution time = 4.85s
# filter_size = 13, clean VS output MSE = 0.1989, execution time = 4.69s


length = len(sig_detection)
start = time.time()
padding = int(filter_size/2)
#print (padding)
for i in tqdm(range(0, 10)):
    sleep(0.1)
    for i in range(length):
        if sig_detection[i] > 0:
            if i+ padding < length and i- padding >=0:
             sig_degraded[i-padding -1  :i+padding +1 ] = median_filter(sig_degraded[i-padding -1  :i+padding +1].tolist(), filter_size)
            elif i-padding < 0:
             sig_degraded[i  :i+filter_size  ] = median_filter(sig_degraded[i:i+filter_size].tolist(), filter_size)
            else:
             sig_degraded[i-filter_size   :i] = median_filter(sig_degraded[i-filter_size  :i].tolist(), filter_size)

end = time.time()

if i +1 == length:
        print("Done!")

print("Median filter execution time:{}s".format(end-start))

plt.subplot(312)
plt.plot(range(len(sig_degraded)), sig_degraded)
plt.title("output_meadian_filter")

wavfile.write("output_median_filter.wav", fs, sig_degraded.astype(np.int16))

print("clean vs output MSE :{}".format(MSE(sig_clean,sig_degraded)))

plt.subplot(313)
plt.plot(range(len(sig_clean)), sig_clean)
plt.title("clean audio")
plt.subplots_adjust(hspace=1)
plt.show()



playsound("degraded_cy.wav")
#playsound('C:/Users/Chengyu/Desktop/Assignment_02_cy/degraded_cy.wav')

#playsound('C:/Users/chengyu/Desktop/Assignment_02_cy/output_median_filter.wav')

# here I used playsound 1.3.0, and it can not play one by one, it will stop after the first audio
#and then I uninstall and install playsound 1.2.2
time.sleep(3)
playsound("output_median_filter.wav")