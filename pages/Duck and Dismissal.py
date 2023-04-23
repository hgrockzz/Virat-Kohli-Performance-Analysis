import pandas as pd
import pickle
import streamlit as st
from PIL import Image
imagg = Image.open('pages/no_times_scored0.png')
st.title('Duck and Dismissal')
if st.button('Display the Graph'):
        st.image(imagg)