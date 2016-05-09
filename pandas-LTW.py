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
import seaborn as sns

#%% Read the file to a Dataframe
df = pd.read_excel('LTW.xlsx', sheetname=0, index_col=None, header=[1,2], skiprows=0)

df2 = df.groupby('departamento')

#%% Results by Wahlkreis
df2 = df.loc[df['Ergebnisebene-Bezeichnung','Wahljahr'].isin(['Wahlkreis 35', 'Wahlkreis 36'])]
df2 = df2.set_index('Wahlkreis')
df2['FDP %'].plot(kind='barh',cmap='gnuplot', figsize=(5,6))
plt.legend(loc='center left', fontsize=8, bbox_to_anchor=(1, 0.5))
plt.show()

#%%
sns.factorplot(df2['FDP %'].groupby('Wahljahr'), palette="BuGn_d")

#%% Results by Stadtbezirk
df2 = df.loc[df['Ergebnisebene-Bezeichnung',''] == 'Stadtbezirke']
df2 = df2.set_index('Stadtbezirk')
df2['FDP'].plot(kind='barh',cmap='gnuplot', figsize=(5,6))
plt.legend(loc='center left', fontsize=8, bbox_to_anchor=(1, 0.5))
plt.show()

#%% Results by Stadteil, difference 2011-2006
df3 = df.loc[df['Ergebnisebene-Bezeichnung',''] == 'Stadtteile']
df3 = df3.set_index('Stadtteil')
df3['FDP %'].diff(periods=-1,axis=1).sort_values(by=2011).plot(kind='barh',cmap='gnuplot', figsize=(5,6))
plt.legend(loc='center left', fontsize=8, bbox_to_anchor=(1, 0.5))
plt.show()

#%% Results by Wahlgebäude, difference 2011-2006
df4 = df.loc[df['Ergebnisebene-Bezeichnung',''] == 'Wahlgebäude']
df4 = df4.set_index('Stadtteil')
df4[('FDP %')].diff(periods=-1,axis=1).plot(kind='barh',cmap='gnuplot', figsize=(5,10))
plt.legend(loc='center left', fontsize=8, bbox_to_anchor=(1, 0.5))
plt.show()

#%% SECOND METHOD
Read the file to a Dataframe
df = pd.read_excel('ltw11-amtlendergebnis-datenblatt.xlsx', sheetname=0, 
                   header=[1,2], parse_cols='H,N,X:AS,BD:CG', index_col=None, skip_footer=283-65)

#Clean the NaNs from the index and rename index, columns
df = df.reset_index().dropna().set_index('index')
df.index.name = 'Stadtteil'
df.columns.names = ['Partei', 'Jahr']
print(df)

# Plot a sample subset after sorting
df['FDP'].sort_values(by=2011).plot(kind='barh', cmap='gnuplot', figsize=(5,10))
plt.show()

