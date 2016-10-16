#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 22:00:45 2016

PCA and clustering of data from the UK National Diabetes Audit.

@author: arcosdid
"""
from sklearn import cluster, decomposition
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import style
style.use('ggplot')

#%% Read the csv file
df = pd.read_csv('pandas-exercises/2010-11_NDA_Rept1.csv', header=0, index_col=(0,1))
# Remove the % sign
for column in list(df.columns.values):
    df[column] = df[column].str.replace('%','')
# change format to float
df = df.astype(float)
print(df.head())

#%% plot histogram of hba1c for patients in centers
df[['hba1c<=10','hba1c<=7.5','hba1c<6.5']].plot.hist(cmap='gnuplot', bins=100)
plt.legend(loc='center left', fontsize=8, bbox_to_anchor=(1, 0.5))
plt.show()

#%% plot histogram of smoking for patients in centers
df.plot.hist(subplots=True, layout=(11,2), cmap='gnuplot', bins=50, alpha=0.75, legend=False)
#plt.legend(loc='center left', fontsize=8, framealpha=0.5, bbox_to_anchor=(1, 0.5))
plt.show()

#%% Plot prevalences sorted by center
df[['Type 1 10/11 prev', 'Type 2 10/11 prev']].sort_values(
by='Type 1 10/11 prev').plot(kind='barh', cmap='gnuplot', 
figsize=(5,15), fontsize=5)
plt.show()

#%%
# scatter plot
df[['Type 1 10/11 prev', 'Type 2 10/11 prev']].plot(x='Type 1 10/11 prev', 
y='Type 2 10/11 prev', kind='scatter')
plt.show()
#%% 
# Clustering of data
k_means = cluster.KMeans(n_clusters=2)
k_means.fit(df[['Type 1 10/11 prev', 'Type 2 10/11 prev']])

# scatter plot
df[['Type 1 10/11 prev', 'Type 2 10/11 prev']].plot(x='Type 1 10/11 prev', 
y='Type 2 10/11 prev', kind='scatter', c=k_means.labels_, cmap='summer')
plt.show()
#%% 
# Clustering of data
k_means = cluster.KMeans(n_clusters=2)
k_means.fit(df[['hba1c<=10','hba1c<=7.5','hba1c<6.5']])

# scatter plot
df[['hba1c<=10','hba1c<=7.5','hba1c<6.5']].plot(x='hba1c<=10', y='hba1c<6.5', 
kind='scatter', c=k_means.labels_, cmap='summer')
plt.show()
#%% scatter plot without clustering
df[['hba1c<=10','hba1c<=7.5','hba1c<6.5']].plot(x='hba1c<=10', y='hba1c<6.5', 
kind='scatter')

#%%
# clustering
k_means = cluster.KMeans(n_clusters=2)
k_means.fit(df)

# dimension reduction
pca = decomposition.PCA(n_components=3)
pca.fit(df)
X = pca.transform(df)
df2 = pd.DataFrame(X)

#3-D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', axisbg='white')
ax.scatter(xs=df2[0], ys=df2[1], zs=df2[2], zdir=u'z', c=k_means.labels_, cmap='prism', depthshade=True)

#add labels to axes
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Feature 3')
#remove ticks from axes
ax.set_xticks([])                               
ax.set_yticks([])                               
ax.set_zticks([])
plt.show()

#%%
from pandas.tools.plotting import radviz

data = df
plt.figure()
radviz(data, 'cholesterol')