import streamlit as st
import pandas as pd
import plotly.express as px
import textwrap

if 'x_range' not in st.session_state:
    st.session_state.x_range = None
if 'y_range' not in st.session_state:
    st.session_state.y_range = None

def wrap_text(text):
    return '<br>'.join(textwrap.wrap(text, width=40))

def update_view(x,y):
   st.session_state.x_range = [x - 0.5, x + 0.5]
   st.session_state.y_range = [y - 0.5, y + 0.5]

df = pd.read_csv("data.csv").dropna(subset=['title_english', 'synopsis'])
df['synopsis'] = df['synopsis'].apply(lambda x: wrap_text(x))
df_copy = df.copy()

st.title("Anime Visualizer")
st.set_page_config(page_title="Anime Visualizer")

fig = px.scatter(df_copy, x="x", y="y", hover_name="title_english", hover_data={"title_english": True, "x": False, "y": False})
if st.session_state.x_range and st.session_state.y_range:
    fig.update_xaxes(range=st.session_state.x_range)
    fig.update_yaxes(range=st.session_state.y_range)
query = st.text_input("Search for an anime", placeholder="More than A Married Couple, But Not Lovers")
if query:
    results = df_copy[df_copy["title_english"].str.contains(query, case=False)].copy()
    if not results.empty:
        results["Action"] = ""
    
        for index, row in results.iterrows():
            col1, col2 = st.columns([4, 1]) # Adjust column widths as necessary
            col1.write(row['title_english'])
            col2.button(
                "Focus Plot", 
                key=f"btn_{row['title_english']}_{index}", # Unique key required for every button
                on_click=update_view, 
                args=(row['x'], row['y'])
            )
    else:
        st.info("No anime found that matched your search. This database is still relatively small, so not every anime will show up here.")
    #df_copy = df_copy[df_copy["title_english"].str.contains(query, case=False)]
fig.update_traces(
    hovertemplate="<b>%{hovertext}</b><br>%{customdata[0]}<extra></extra>",
    customdata=df_copy[['synopsis']]
)


st.plotly_chart(fig, width="stretch")
