#!/usr/bin/env python
# coding: utf-8

# In[143]:

import pandas as pd
import numpy as np 
import streamlit as st
import datetime
from os import listdir
from os.path import isfile, join
import glob
import re
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt


# In[158]:

@st.cache
def load_data(nrows):
    data =  pd.read_csv(r'C:\Users\nitis\Streamlit\final.csv', nrows=nrows)    
    return data


# In[160]:

df = load_data(100000)
group =  df.country.unique()
print(group)

# In[161]:
#create seaborn

chart3 = alt.Chart(df).mark_circle().encode(x='gni_per_capita', y='life_expectancy', size='population', color='max(gni_per_capita):Q')
st.altair_chart(chart3, use_container_width=True)

st.header('Nitish Gapminder')



checkbox = st.sidebar.checkbox("show country")
#print(checkbox)

if checkbox:
    
 st.sidebar.subheader("Scatter plot setup")

slect_box1=st.sidebar.selectbox(label = 'country', options = group)
slect_box2 =st.sidebar.slider('year',1800,2019)
mask = df['country'] == slect_box1
df1 = df[mask]
mask2 = df1['year'] == slect_box2
df2= df1[mask2]
st.dataframe(data=df2)

#create seaborn
chart = alt.Chart(df2).mark_circle().encode(x='gni_per_capita', y='life_expectancy', size='population', color='max(gni_per_capita):Q')
st.altair_chart(chart, use_container_width=True)