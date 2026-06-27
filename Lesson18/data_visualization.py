import streamlist as st
import pandas as pd
import plotly.ex as px

book_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title("Bestselling Books Analysis")
st.write("This app analyzes