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
df = pd.read_excel('precioscombustible.xlsx', sheetname=0, index_col=None)
# shorten a long name
df.departamento.replace('ARCHIPIELAGO DE SAN ANDRES. SANTA CATALINA Y PROVIDENCIA', 'SAN ANDRES Y P.', inplace=True)

df['prodcategoria'] = np.where(df['producto'].str.contains('GASOLINA EXTRA'),'GASOLINA EXTRA', 
np.where(df['producto'].str.contains('GASOLINA CORRIENTE'),'GASOLINA CORRIENTE', np.where(df['producto'].str.contains('DIESEL'),'DIESEL', 'KEROSENE')))
#%%
# departamento mean price overview
df.groupby('departamento').mean().precio.sort_values().plot(kind='barh', figsize=(5,6))
# producto mean price overview
df.groupby('producto').mean().precio.sort_values().plot(kind='barh', figsize=(5,6))
# prices per municipio in a particular departamento
df.loc[df['departamento'] == 'META'].groupby('municipio').mean().precio.sort_values().plot(kind='barh', figsize=(5,6))

#%% Pivot table
df.pivot_table(values='precio', index='departamento', columns='producto')
df.pivot_table(values='precio', index='bandera', columns='producto').plot(kind='barh',cmap='gnuplot', figsize=(5,10))
plt.legend(loc='center left', fontsize=8, bbox_to_anchor=(1, 0.5))
plt.show()

#%% plot precio per bandera and prodcategoria
sns.factorplot(x='precio', y='bandera', hue='prodcategoria', 
               data=df.sort_values(by='precio'), 
               palette="coolwarm", size=5, aspect=1.25)
#%%
sns.factorplot(x='precio', y='departamento', hue='prodcategoria', 
               data=df.loc[df['bandera']=='TERPEL'].sort_values(by='precio'),
               palette="coolwarm", size=5, aspect=1.25)
#%%
g = sns.barplot(x='departamento', y='precio', data=df.sort('precio'), palette="RdBu_r")
for item in g.get_xticklabels():
    item.set_rotation(90)
g
#%%
g = sns.factorplot(x='producto', y='precio', hue='bandera', data=df, palette="RdBu_r")
for item in g.get_xticklabels():
    item.set_rotation(90)
g
#%%
planets = sns.load_dataset("planets")
years = np.arange(2000, 2015)
g = sns.factorplot(x="year", data=planets, kind="count",
                   palette="BuPu", size=6, aspect=1.5, order=years)
g.set_xticklabels(step=2)