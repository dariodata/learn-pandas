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
df = pd.read_excel('ltw11-amtlendergebnis-datenblatt.xlsx', sheetname=0, 
                   header=[1,2], parse_cols='H,N,X:AS,BD:CG', index_col=None, skip_footer=283-65)
print(df)

#%% Clean the NaNs from the index and rename index, columns
df = df.reset_index().dropna().set_index('index')
df.index.name = 'Stadtteil'
df.columns.names = ['Partei', 'Jahr']
print(df)

#%% Plot a sample subset after sorting
df['FDP'].sort_values(by=2011).plot(kind='barh', cmap='gnuplot', figsize=(5,10))
plt.show()

