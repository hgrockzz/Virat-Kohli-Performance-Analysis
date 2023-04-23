import pandas as pd
import pickle
import streamlit as st
from PIL import Image
imagg = Image.open('Monthly_perf_yeartoyear.png')
st.title('YearWise Performance')
if st.button('Display the Graph'):
        st.image(imagg)