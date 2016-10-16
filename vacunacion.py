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
df = pd.read_excel('pastovacunacion.xlsx', sheetname=0, index_col=None)
df.columns = ['municipio', 'codigodanemunicipio', 'annio', 'biologico',
       'poblacionasignada', 'vacunacionmensual', 1,
       2,3,4,5,6,7,8,9,10,11,12, 'ninosvacunadostotal',
       'coberturaacumulada1', 'coberturaacumulada2', 'coberturaacumulada3',
       'coberturaacumulada4', 'coberturaacumulada5', 'coberturaacumulada6',
       'coberturaacumulada7', 'coberturaacumulada8', 'coberturaacumulada9',
       'coberturaacumulada10', 'coberturaacumulada11', 'coberturaacumulada12',
       'coberturaprogramadamayorigual95']
# drop unnecessary columns
df = df.drop(df.columns[18:], axis=1)
df = df.drop(df.columns[:3], axis=1)

tidy = pd.melt(df, id_vars='biologico', 
               value_vars=[1,2,3,4,5,6,7,8,9,10,11,12], var_name='mes')

# plot ninos vacunados per mes per biologico
sns.set(style="whitegrid")
sns.factorplot(x='mes', y='value', hue='biologico', data=tidy, palette='Blues', 
               size=5, aspect=1.5)
sns.despine(left=True)

#%%
df.pivot_table(values='poblacionasignada', index='biologico').sort_values().plot(kind='barh')
df.pivot_table(values='poblacionasignada', index='biologico', columns=[1,2,3,4,5,6,7,8,9,10,11,12]).plot(kind='barh')
