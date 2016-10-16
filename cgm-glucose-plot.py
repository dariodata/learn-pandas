#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 22:00:45 2016

Reads a csv file with glucose levels and plots a histogram and moving average

@author: arcosdid
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

#%% Read the csv file
df = pd.read_csv('/Users/dario/Documents/learn-pandas/CGM-14yo.csv', header=0)
print(df)

#%% plot histogram for glucose
df['glucose'].plot.hist()

#%% Plot moving average for glucose
mvav = movingaverageperiod = 7*24*60/5
plt.plot(np.convolve(df['glucose'], np.ones((mvav,))/mvav, mode='valid'));
plt.show()

#%% plot histogram and moving average as subplots
plt.figure(figsize=(9,3))

plt.subplot(1, 2, 1)
plt.title('Histogram')
df['glucose'].plot.hist()

plt.subplot(1, 2, 2)
mvav = movingaverageperiod = 7*24*60/5
plt.title('Moving average')
plt.plot(np.convolve(df['glucose'], np.ones((mvav,))/mvav, mode='valid'))

plt.show()

