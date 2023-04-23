import pandas as pd
import pickle
import streamlit as st
from PIL import Image
imagg = Image.open('Reason_Dismissal_VK.png')
st.title('Reason Dismissal')
if st.button('Display the Graph'):
        st.image(imagg)
        st.text('Conclusion')
        st.text('Most of the time, Virat Kohli gets out by getting caught by the fielder or the keeper.')