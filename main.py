import streamlit as st
import pandas as pd
import plotly.express as px
import textwrap

def wrap_text(text):
    return '<br>'.join(textwrap.wrap(text, width=40))


df = pd.read_csv("data.csv").dropna(subset=['title_english', 'synopsis'])
df['synopsis'] = df['synopsis'].apply(lambda x: wrap_text(x))

fig = px.scatter(df, x="x", y="y", hover_name="title_english", hover_data={"title_english": True, "x": False, "y": False})
fig.update_traces(
    hovertemplate="<b>%{hovertext}</b><br>%{customdata[0]}<extra></extra>",
    customdata=df[['synopsis']]
)

st.plotly_chart(fig, width="stretch")