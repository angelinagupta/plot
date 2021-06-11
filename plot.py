import plotly
import pandas as pd
import plotly.express as px

df = pd.read_csv("D:\code\python\line_chart.csv")
fig = px.line(df, x = "Year" , y = "Per capita income", color= "Country", title= "Per Capita Income")
plotly.offline.plot(fig)