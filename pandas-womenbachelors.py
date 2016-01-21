#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 22:00:45 2016

@author: arcosdid
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

#%% Read the csv file
df = pd.read_csv('percent-bachelors-degrees-women-usa.csv', header=0, index_col=0)
print(df)

#%% plot
df.plot.line(cmap='gnuplot')
plt.legend(loc='center left', fontsize=8, framealpha=0.5, bbox_to_anchor=(1, 0.5))
plt.show()

#%% plot selected columns
df[['Business', 'Biology', 'Engineering','Foreign Languages']].plot.line(cmap='gnuplot')
plt.legend(loc='center left', fontsize=8, framealpha=0.5, bbox_to_anchor=(1, 0.5))
plt.show()

#%% Plot moving average for a column
mvav = movingaverageperiod = 5
plt.plot(np.convolve(df['Biology'], np.ones((mvav,))/mvav, mode='valid'))
plt.ylim(0,100)
plt.show()

