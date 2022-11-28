# Made by Yu Cheng
# Student ID = 22302304
import numpy as np
from scipy.io import wavfile
import matplotlib
import matplotlib.pyplot as plt
import scipy
from scipy import interpolate
import scipy.interpolate
from scipy.interpolate import CubicSpline
from tqdm import tqdm
import time
from time import sleep

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
restored_data = sig_degrade
loc_zero = np.where(sig_detection == 0)[0]
loc_clicks = np.where(sig_detection > 0)[0]
length = len(loc_clicks)

#restored_data = scipy.interpolate.CubicSpline(loc_zero, sig_degrade[loc_zero],axis=0, bc_type='not-a-knot', extrapolate=None)
restored = interpolate.CubicSpline(loc_zero, sig_degrade[loc_zero])

for i in tqdm(range(0, 10)):
    sleep(0.1)
    for loc in loc_clicks:
        restored_data[loc] = restored(loc)

# end time
end = time.time()

if loc + 1 == length:
    print('done')

print("cubic_spline execution time: {}s".format(end-start))
print("Using median filter, clean VS output MSE: {}".format(
    MSE(sig_clean, restored_data)))

plt.subplot(312)
plt.plot(range(len(restored_data)), restored_data)
plt.title('output')

wavfile.write("output_cubic_spline.wav", fs, restored_data)

plt.subplot(313)
plt.plot(range(len(sig_clean)), sig_clean)
plt.title("clean audio")
plt.subplots_adjust(hspace=1)
plt.show()
