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
df = pd.read_excel('ltw11-amtlendergebnis-datenblatt.xlsx', sheetname=0, header=[1,2], index_col=None)
# customize the names of the headers
df.columns = pd.MultiIndex(levels=[['%', 'Anzahl Wahlbez.', 'BIG', 'BIG %', 'CDU', 'CDU %', 'DIE LINKE', 'DIE LINKE %', 'Ergebnisebene-Bezeichnung', 'FDP', 'FDP %', 'GRÜNE', 'GRÜNE %', 'Hellmer %', 'Hellmer (nur WK 35)', 'NPD', 'NPD %', 'PIRATEN', 'PIRATEN %', 'REP', 'REP %', 'RSB', 'RSB %', 'SPD', 'SPD %', 'Sonstige 2006', 'Sonstige%', 'StBezNr', 'StTeilNr', 'Stadtbezirk', 'Stadtteil', 'Summe Wahlber.', 'WGebNr', 'Wahlber.mit WS1', 'Wahlber.ohne WS', 'Wahlbezirknr.', 'Wahlgebäude', 'Wahlkreis', 'Weiß %', 'Weiß (nur WK 35)', 'Wähler insges.', 'Wähler mit WS', 'Wähler ohne WS', 'gültig%', 'gültige Stimmz.', 'mit WS %', 'ungültig%', 'ungültige Stimmz.', 'ödp', 'ödp %'], [2006, 2011, '']],
           labels=[[8, 35, 37, 27, 29, 28, 30, 32, 36, 1, 34, 33, 31, 45, 40, 0, 41, 42, 47, 46, 44, 43, 4, 5, 23, 24, 11, 12, 9, 10, 2, 3, 6, 7, 19, 20, 15, 16, 48, 49, 17, 18, 21, 22, 14, 13, 39, 38, 25, 26, 34, 33, 31, 45, 40, 0, 41, 42, 47, 46, 44, 43, 4, 5, 23, 24, 11, 12, 9, 10, 2, 3, 6, 7, 19, 20, 15, 16, 48, 49, 17, 18, 21, 22, 14, 13, 39, 38, 25, 26], [2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
           names=['Ergebnis', 'Wahljahr'])

#%% Results by Wahlkreis
df2 = df.loc[df['Ergebnisebene-Bezeichnung',''].isin(['Wahlkreis 35', 'Wahlkreis 36'])]
df2 = df2.set_index('Wahlkreis')
df2['FDP %'].plot(kind='barh',cmap='gnuplot', figsize=(5,6))
plt.legend(loc='center left', fontsize=8, bbox_to_anchor=(1, 0.5))
plt.show()

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

