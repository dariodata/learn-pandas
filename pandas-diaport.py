#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:18:08 2016

@author: arcosdid
"""
import datetime as DT
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

#%% Read the file to a Dataframe
df = pd.read_excel('DiaPort_PatientenRegister.xlsx', sheetname=0, header=3, index_col=None)
df = df.dropna(how='all')
print(df)
# create age column
now = pd.Timestamp(DT.datetime.now())
df['age'] = (now - df['Geb.Datum']).astype('<m8[Y]')
print(df)

#%% plot the ages grouped by sex
df['age'].groupby(by=df['Anrede']).plot.hist(sharex=True, stacked=True, bins=20,range=(10,100),alpha=.8)
plt.legend(loc='center left', fontsize=8, bbox_to_anchor=(1, 0.5))
#df['age'].hist(by=df['Anrede'], stacked=True, bins=20,range=(10,100), alpha=.8)
plt.show()

#%% PYTHON 2.7!!!
from geopy.geocoders import Nominatim

geolocator = Nominatim()
#Test getting the coordinates for a city
#location = geolocator.geocode(df['Stadt'][1])
#print(location.latitude)

# fill two empty lists with lat and lon
latlist=[]
lonlist=[]
for i in df['Stadt']:
    loc = geolocator.geocode(i)
    latlist.append(loc.latitude)
    lonlist.append(loc.longitude)

# add lat and lon columns to dataframe
df['Latitude'] = latlist
df['Longitude'] = lonlist

#%% plot the map with the coordinates
from mpl_toolkits.basemap import Basemap

fig = plt.figure(figsize=(20,10))
ax = fig.add_axes([0.05,0.05,0.9,0.85])
# These coordinates form the bounding box of Germany
bot, top, left, right = 5.87, 15.04, 47.26, 55.06 # just to zoom in to only Germany
map = Basemap(projection='merc', resolution='l',
    llcrnrlat=left,
    llcrnrlon=bot,
    urcrnrlat=right,
    urcrnrlon=top)
# plots the state boundaries:
map.readshapefile('./DEU_adm_shp/DEU_adm1', 'adm_1', drawbounds=True)  
#map.drawcoastlines()
map.fillcontinents(color='azure')
# plot the coordinates from the dataframe
x, y = map(np.array(df['Longitude']), np.array(df['Latitude']))
map.plot(x,y,'o')