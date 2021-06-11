import plotly
import pandas as pd
import plotly.express as px

df = pd.read_csv("D:\code\python\data.csv")
fig = px.bar(df, x = "Country" , y = "InternetUsers", title= "Internet Users")
plotly.offline.plot(fig)