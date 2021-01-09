# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:31:10 2020

@author: Zheng Xie

@Source: https://towardsdatascience.com
@Title: Learn How to Create Animated Graphs in Python
@Author: Costas Andreou

@Data Link: https://www.kaggle.com/imdevskp/corona-virus-report?select=day_wise.csv
"""

import pandas as pd
import matplotlib.animation as ani
import matplotlib.pyplot as plt


# Data cleaning
df = pd.read_csv('day_wise.csv', header = 'infer')
df1 = df[['Date', 'Confirmed', 'Deaths', 'Recovered', 'Active']]
df1.set_index('Date', inplace = True)

# Chart configuration 
color = ['red', 'green', 'blue', 'orange']
fig = plt.figure()
plt.xticks(rotation = 45) 
plt.subplots_adjust(bottom = 0.2, top = 0.9) 
plt.ylabel('No of Cases')
plt.xlabel('Date')
ax = plt.gca()
ax.xaxis.set_major_locator(plt.MaxNLocator(7))

# Set up curve function.
def biuld_chart(i = int):
    plt.legend(df1.columns)
    p = plt.plot(df1[:i].index, df1[:i].values)
    for i in range(4):
        p[i].set_color(color[i])
        
animator = ani.FuncAnimation(fig, biuld_chart, interval = 200)
#plt.show()

#animator.save(r'path.gif')

