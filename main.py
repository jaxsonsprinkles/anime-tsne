import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("data.csv")

fig = px.scatter(df, x="x", y="y", hover_name="x", hover_data={"x": True, "y": False})
fig.update_traces(
    hovertemplate=df["x"]
)

st.plotly_chart(fig, use_container_width=True)