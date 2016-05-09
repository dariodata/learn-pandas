#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 22:00:45 2016
Reads a list of events by date and plots a moving average

Modules:
fechas.py -- a file where the events are documented and contains two variables
events -- internal events
eventssolo -- external events

@author: arcosdid
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib import style
#style.use('ggplot')
import seaborn as sns
sns.set_palette('Paired')
sns.set_style("whitegrid")

from fechas import *

#%% READ DATA AND CALCULATE MOVING AVERAGE

# Read the internal events
df1 = pd.DataFrame(events)
df1 = pd.to_datetime(df1[0]*10000 + df1[1]*100 + df1[2], format='%Y%m%d')
df1 = pd.DataFrame(df1)
df1['Int'] = pd.Series(np.ones(len(df1)+10))
df1.columns=(['Date', 'Int'])

# Read the external events
df2 = pd.DataFrame(eventssolo)
df2 = pd.to_datetime(df2[0]*10000 + df2[1]*100 + df2[2], format='%Y%m%d')
df2 = pd.DataFrame(df2)
df2['Ext'] = pd.Series(np.ones(len(df2)+10))
df2.columns=(['Date', 'Ext'])

# Concatenate both dataframes into one
df = pd.concat([df1, df2], ignore_index=True)
df = df.set_index('Date')
df = df.sort_index()
df = df.resample('1d', how='sum').fillna(0) # to complete every day

# Calculate moving average
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

# Plot relevant columns from dataframe
df.loc[:,['Int', 'Ext Moving average 8w', 'Int Moving average 8w']].\
plot(cmap='Blues') #figsize=(8,4) possible
plt.xlim(df.index[0], df.index.max()+10)
plt.title('Moving average of events per week')
plt.show()

#%% DAY OF THE WEEK ANALYSIS

# create column for day of the week
df['Day'] = df.index.dayofweek
df['Day'] = df.Day.astype('category')
df.Day.cat.categories = ['Mon','Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# create column for type
df['Type'] = np.where(df['Int']>0, 'internal', np.where(df['Ext']>0, 'external', np.nan))
df['Type'] = df['Type'].astype('category')
df['Type'] = df['Type'].cat.remove_categories(['nan'])

# show count for each day
#df[(df.Int == 1)&(df.Day == 'Mon')].Day.count()

# plot count data per day of the week
plt.figure()
plt.title('Event count per day of the week')
sns.countplot(data=df, x='Day', hue='Type') # data since 2016 --> df[440:]
sns.despine(left=True)
plt.show()

# joint histograms
plt.figure()
df['Ext Moving average 8w'].hist(alpha=.9)
df['Int Moving average 8w'].hist(alpha=.9)
plt.title('Histogram of event frequency per week')
plt.show()

#%% histograms side-by-side
#df.loc[:,['Ext Moving average 8w', 'Int Moving average 8w']].hist()
#plt.show()

# With seaborn
#sns.distplot(df['Int Moving average 8w']), sns.distplot(df['Ext Moving average 8w'])

#%% First DRAFT using only the internal events
'''
# Read the events list and make time series index
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
'''
