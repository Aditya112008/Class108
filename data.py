from numpy import True_
import plotly.figure_factory as ff
import pandas as pd 
import csv

df = pd.read_csv("./data.csv")
fig = ff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist = True)
fig.show()

#we can also drawa distribution using plotly's figure_factory module
#install scipy package 
#use displot() to draw the distribution graph 
# it takes 2 arguments 
#1) data 
#2) the label 
