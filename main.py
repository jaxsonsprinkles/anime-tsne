import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("data.csv")

fig = px.scatter(df, x="x", y="y", hover_name="title", hover_data={"title": True, "x": False, "y": False})
fig.update_traces(
    hovertemplate=df["title"]
)

st.plotly_chart(fig, use_container_width=True)