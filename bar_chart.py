# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:17:56 2020

@author: Zheng Xie

@Source: https://towardsdatascience.com
@Title: Learn How to Create Animated Graphs in Python
@Author: Costas Andreou
"""

import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('time_series_covid19_deaths_global.csv', header = 'infer')

df_interest = df.loc[
    df['Country/Region'].isin(['Brazil', 'US', 'Italy', 'India'])]
df_interest.rename(
    index=lambda x: df_interest.at[x, 'Country/Region'], inplace=True)
df1 = df_interest.transpose()
df1 = df1.drop(['Province/State', 'Country/Region', 'Lat', 'Long'])
df1 = df1.loc[(df1 != 0).any(1)]
df1.index = pd.to_datetime(df1.index)

fig = plt.figure()

def buildmybarchart(i=int):
    iv = min(i, len(df1.index)-1)
    objects = df1.max().index
    y_pos = np.arange(len(objects))
    performance = df1.iloc[[iv]].values.tolist()[0]
    
    plt.bar(y_pos, performance, align='center', color=['red', 'green', 'blue', 'orange'])
    plt.xticks(y_pos, objects)
    plt.ylabel('Deaths')
    plt.xlabel('Countries')
    plt.title('Deaths per Country \n' + str(df1.index[iv].strftime('%y-%m-%d')))
        
animator = ani.FuncAnimation(fig, buildmybarchart, interval=100)
        
plt.show()

#animator.save(r'path.gif')
