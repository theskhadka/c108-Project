import pandas as pd
import csv
import plotly.figure_factory as ff
df = pd.read_csv("bellcurve.csv")
fig = ff.create_distplot([df["Height(Inches)"].tolist()], ["Height"], show_hist = False)
fig.show()