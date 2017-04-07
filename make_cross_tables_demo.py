from pylab import *
from pandas import date_range,Series,DataFrame,read_csv, qcut, read_excel
from pandas.tools.plotting import radviz,scatter_matrix,bootstrap_plot,parallel_coordinates
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as colors
import brewer2mpl
from matplotlib import rcParams

dark2_colors = brewer2mpl.get_map('Dark2', 'Qualitative', 7).mpl_colors

rcParams['figure.figsize'] = (10, 6)
rcParams['figure.dpi'] = 150
#rcParams['axes.color_cycle'] = dark2_colors #gives an error
rcParams['lines.linewidth'] = 2
rcParams['axes.facecolor'] = 'white'
rcParams['font.size'] = 14
rcParams['patch.edgecolor'] = 'white'
rcParams['patch.facecolor'] = dark2_colors[0]
rcParams['font.family'] = 'StixGeneral'

def remove_border(axes=None, top=False, right=False, left=True, bottom=True):
    ax = axes or plt.gca()
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)
    
    #turn off all ticks
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')
    
    #now re-enable visibles
    if top:
        ax.xaxis.tick_top()
    if bottom:
        ax.xaxis.tick_bottom()
    if left:
        ax.yaxis.tick_left()
    if right:
        ax.yaxis.tick_right()

df=pd.read_csv("E:\Anna\Desktop\жесты\cleaned.csv") #read files with the help of pandas
print(df.head()) # print first 5 rows of csv file
print(df.columns)
#print(df.head())
print(df.shape)
df.info()
z = df.describe(include=['object'])
#print(z)
#print(df.iloc[0:5, 0:4])
data = pd.crosstab(df['expression pattern / phonetics(?)'], df['languages'], normalize=True)
data.to_excel('expression_lang_norm.xlsx')

