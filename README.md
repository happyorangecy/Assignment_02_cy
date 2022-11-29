# Add here a title for the project
Yu_Cheng_CM_assignment 2
## High-level Description of the project
This assignment builds on Assignment I. We assume that we have successfully detected the clicks and we are applying different interpolation methods to restore the audio, such as
- median filtering
- cubic splines

---

## Installation and Execution

Provide details on the Python version and libraries (e.g. numpy version) you are using. One easy way to do it is to do that automatically:
```sh                                 
pip3 install pipreqs

pipreqs $project/path/requirements.txt
```
For more details check [here](https://github.com/bndr/pipreqs)

Details on the Python version and libraries are:
```sh   
matplotlib==3.6.2
numpy==1.22.4
playsound==1.3.0
scipy==1.7.3
tqdm==4.64.1
```
Afer installing all required packages you can run the demo file simply by typing:
```sh
python demo_audio_restoration.py
```
---

## Methodology and Results
Describe here how you have designed your code, e.g. a main script/routine that calls different functions, is the unittesting included in the main routine? 

__<font size= '4' color="#0000FF">Median filter: </font>__

(1) In my median_filter, the simple median filter is first designed for a data list [1,2,3,6,10,7,2,1]. I set Window size equal to 3. Hence it will replace every sample with the running median over 3 samples. Zero padding is required to keep the size of original input. So median filter picks the values in the size of window size, and then use sort function to make them in correct order. Then only keep the mid one. 

 (Tips: I use the unittesting in my simple median_filter. Here 'copy.deepcopy' should be used, which helps remain the original data when do some changes on it . It is useful for doing unittesting.)

To apply the median filter to restore a degraded .wav audio, first read the sample rate and signal data for three audios.
```sh
fs, sig_degraded = wavfile.read('degraded_cy.wav')
fs_1, sig_detection = wavfile.read('detectionfile_cy.wav')
fs_2, sig_clean = wavfile.read('clean_cy.wav')
```
degraded_cy      : restore this audio to out_median_filter.wav

detectionfile_cy : check the location of all clicks

clean_cy         : the original clean audio, compare the clean audio and the out_median_filter to observe the mse



I design it considering three situations.

<img src="design_mdian_filter_wav.png" width="350">

First, I ignore the first element or the last element is noise (where click = 1), this is the easiest situation, just do median filter in the range [i-padding :i+padding ], to make the result more accurate, also can choose the range: [i - padding - 1  : i + padding +1].

Second, if the first element is the click, there is nothing left can be used to do median filter, so I use the values after this element. The range is [i  : i + filter_size ]. 

Third, if the last element is the click, there is nothing right can be used to do median filter, so I use the values before this element. The range is [i - filter_size : i].

__<font size= '4' color="#0000FF">Cubic Spline filter: </font>__

I deisgn it in the process below:

<img src="design_cubic_wav.png" width="350">

First, I have the degraded data [1, 2, 1000, 3, 4], and the 1000 is my click.
The spline can be controlled by the knots and draw the most suitable curve for these knots. So, I can get an ideal curve without all the clicks. Here, I use the scipy.interpolate .CubicSpline function to complete this step.

Second, after I having the ideal curve, I can use the amplitude in the ideal curve to replace the amplitude in the click.


**Results**

1. For the median filter, different lengths were explored to test the effectiveness of the restoration. In particular, different median filter lengths were tested and its corresponding MSE value between clean audio and output audio was observed to deliver the lowest MSE, as shown in the figure below.

<img src="filter length VS MSE.png" width="350">

The restored waveform <output_medianFilter.wav> with the optimal filter length is given below:

<img src="waveform_median.png" width="350">

2. Using the cubic splines, we observe that it can run faster than the other way.

The restored waveform <output_cubicSplines.wav> with the optimal filter length is given below:

<img src="waveform_cubic.png" width="350">

3. Comparing the two different interpolation methods, we notice that Cubic Spline Filter method  achieves a lower MSE on average. The runtime of Cubic filter method is much shorter obviously.

<img src="comparison_table.png" width="350">

<img src="Comparison.png" width="350">

From above figures, we can see that the Cubic filter(green column) performs better than median filter(orange column) with less MSE.


After listening to the two restored files, I notice that my clean audio has no clicks sound. And these two output audios are all without clicks. But cubic filter can deal with the clicks faster and better. 


---
## Credits

This code was developed for purely academic purposes by happyorangecy (add github profile name) as part of the module ..... 

Resources:
- XXXX
- XXX





