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
from fechas import *

#%% Read the events list and make time series index
df1 = pd.DataFrame(events)
df1 = pd.to_datetime(df1[0]*10000 + df1[1]*100 + df1[2], format='%Y%m%d')
df1 = pd.DataFrame(df1)
df1['Int'] = pd.Series(np.ones(60))
df1.columns=(['Date', 'Int'])
#df2 = df2.set_index('Date')

df2 = pd.DataFrame(eventssolo)
df2 = pd.to_datetime(df2[0]*10000 + df2[1]*100 + df2[2], format='%Y%m%d')
df2 = pd.DataFrame(df2)
df2['Ext'] = pd.Series(np.ones(60))
df2.columns=(['Date', 'Ext'])
#dfe = dfe.set_index('Date')

df = pd.concat([df1, df2], ignore_index=True)
df = df.set_index('Date')
df = df.sort_index()
df = df.resample('1d', how='sum').fillna(0) # resampled to complete every day

# Plot moving average
for i in [7*4, 7*4*2]:
    mvav = i # moving average period, i.e. number of points to average
    dfi = np.convolve(df['Int'], 
                      np.ones((mvav,))*7/mvav # factor for obtaining average
                      , mode='full')
    df['Int Moving average %sw' % (int(i/7))] = dfi[:-(i-1)]
    dfj = np.convolve(df['Ext'], 
                      np.ones((mvav,))*7/mvav # factor for obtaining average
                      , mode='full')
    df['Ext Moving average %sw' % (int(i/7))] = dfj[:-(i-1)]

df.loc[:,['Int', 'Ext Moving average 8w', 'Int Moving average 8w']].plot(figsize=(8,4), cmap='Blues')
#plt.ylim(0, 2)
plt.show()

#%% histogram
df.loc[:,['Ext Moving average 8w', 'Int Moving average 8w']].hist(figsize=(8,4))
#plt.ylim(0, 2)
plt.show()

#%% Read the events list and make time series index
df = pd.DataFrame(events)
df2 = pd.to_datetime(df[0]*10000 + df[1]*100 + df[2], format='%Y%m%d')
df2 = pd.DataFrame(df2)
df2['Event'] = pd.Series(np.ones(60))
df2.columns=(['Date', 'Event'])
df2 = df2.set_index('Date')

df2 = df2.resample('1d', how='sum').fillna(0) # resampled to complete every day
#df3 = df2.resample('7d', how='sum', label='right').fillna(0) # resampled to weeks

# Plot moving average
for i in [7*4, 7*4*2]:
    mvav = i # moving average period, i.e. number of points to average
    df4 = np.convolve(df2['Event'], 
                      np.ones((mvav,))*7/mvav # factor for obtaining average
                      , mode='full')
    df2['Moving average %sw' % (int(i/7))] = df4[:-(i-1)]
df2.plot(figsize=(8,4), cmap='Reds')
plt.ylim(0, 4)
plt.show()

#%% plot histogram for moving average 8 weeks
df['Ext Moving average 8w'].hist(alpha=.9)
df['Int Moving average 8w'].hist(alpha=.9)
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

