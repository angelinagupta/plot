import plotly
import pandas as pd
import plotly.express as px

df = pd.read_csv("D:\code\python\data.csv")
fig = px.scatter(df, x = "Population" , y = "Per capita", title= "Internet Users", size="Percentage", color= "Country", size_max= 60)
plotly.offline.plot(fig)