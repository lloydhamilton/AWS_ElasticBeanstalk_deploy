import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets
import seaborn as sns

iris = datasets.load_iris()

# -- Set page config
apptitle = 'GW Quickview'


# -- Default detector list
detectorlist = ['H1','L1', 'V1']

# Title the app
st.title('Gravitational Wave Quickview')
st.sidebar.markdown("hellow world")
st.markdown("""
 * Use the menu at left to select data and set plot parameters
 * Your plots will appear below
""")
st.sidebar.markdown('# this is a comment that has been edited locally')
data = pd.DataFrame(iris.data, 
                    columns = np.append(iris.target_names, np.array(['class'])))

st.markdown('## Iris Dataset')

st.sidebar.file_uploader('upload your file')
st.sidebar.color_picker('pick pick pick')
st.dataframe(data,400, 500)

col1, col2, col3 = st.columns(3)
with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")