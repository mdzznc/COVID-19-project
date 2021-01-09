# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 16:10:22 2020

@author: Zheng Xie

@Source: https://towardsdatascience.com
@Title: Learn How to Create Animated Graphs in Python
@Author: Costas Andreou
"""

import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('covid_19_clean_complete.csv', header = 'infer')

df1 = df.loc[
    df['Country/Region'].isin(['US'])
    ]
df2 = df1[['Date', 'Recovered', 'Deaths',  'Active']]
df2.set_index('Date', inplace = True)
df2.index = pd.to_datetime(df2.index)


fig, ax = plt.subplots()
explode=[0.01,0.01,0.01]

def getmepie(i): 
    def absolute_value(val):
        a  = np.round(val/100.*df2.head(i).max().sum(), 0)
        return int(a)
    ax.clear()
    plot = df2.head(i).max().plot.pie(y=df2.columns,autopct=absolute_value, label='', explode = explode, shadow = False)
    plot.set_title('Compostion of Confirmed Cases in USA\n'+                    
                  str(df2.index[min( i, len(df2.index)-1 )].strftime('%y-%m-%d')))

animator = ani.FuncAnimation(fig, getmepie, interval = 100)
#plt.show()

#animator.save(r'path.gif')
