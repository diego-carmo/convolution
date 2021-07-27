# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 23:33:00 2021

@author: Guest
"""

# Constant overlap-add (COLA) property test for Hann windon
# for more dinformation see equation 9.2 in
# https://www.dsprelated.com/freebooks/sasp/Overlap_Add_OLA_STFT_Processing.html

import matplotlib.pyplot as plt
import numpy as np

    
winLen = 256 # window length

# direct use of the hanning window does not result in perfect reconstruction
# in time domain
win1 = np.hanning(winLen)

# solution for Hanning window to meet the COLA property.
# 'periodic' parameter in matlab 'hann' function:
# https://www.mathworks.com/help/signal/ref/hann.html
win2 = np.hanning(winLen+1)
win2 = win2[:winLen]

hopSizePerc = 50 # hop size between sucessive windows (in percent) 
hopSizeSamp =(winLen*hopSizePerc)//100 # hop size (in samples)
numWin = 5 # number of windows to test the Constant Overlap-add property
sigLen = (numWin-1)*winLen+hopSizeSamp
colaSignal1 = np.zeros( (sigLen,) )
colaSignal2 = np.zeros( (sigLen,) )
windx = np.array(range(winLen), int)

# test COLA(R) for R = hopSizeSamp
for m in range(numWin):
    colaSignal1[ windx + m*hopSizeSamp ] = colaSignal1[ windx + m*hopSizeSamp ] + win1
    colaSignal2[ windx + m*hopSizeSamp ] = colaSignal2[ windx + m*hopSizeSamp ] + win2


# Data for plotting
fig, (ax1, ax2) = plt.subplots(2,1)

ax1.plot(colaSignal1)
ax1.plot(colaSignal2)
ax1.set(ylabel='Normalized Amplitude', title='COLA Property')
ax1.grid()

ax2.plot(colaSignal1)
ax2.plot(colaSignal2)
ax2.set(xlabel='sample', ylabel='Normalized Amplitude', ylim=(0.992,1.001))
ax2.grid()
#ax2.set_ylim(0.992, 1.001)

plt.show()