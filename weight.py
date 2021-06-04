from numpy import True_
import plotly.figure_factory as ff
import pandas as pd 
import csv

df = pd.read_csv("./data.csv")
fig = ff.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"],show_hist = True)
fig.show()