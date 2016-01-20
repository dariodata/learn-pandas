#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:18:08 2016

@author: arcosdid
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

#%% Read the file to a Dataframe
df = pd.read_excel('ltw11-amtlendergebnis-datenblatt.xlsx', sheetname=0, header=[1,2], parse_cols='H,N,X:AS,BD:CG', index_col=None, skip_footer=283-65)
print(df)

#%% Clean the NaNs from the index and rename index, columns
df = df.reset_index().dropna().set_index('index')
df.index.name = 'Stadtteil'
df.columns.names = ['Partei', 'Jahr']
print(df)

#%% Plot a sample subset after sorting
df['FDP'].sort_values(by=2011).plot(kind='barh', cmap='gnuplot', figsize=(5,10))

#%% Read the csv file
df = pd.read_csv('CGM-14yo.csv', header=0)
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
