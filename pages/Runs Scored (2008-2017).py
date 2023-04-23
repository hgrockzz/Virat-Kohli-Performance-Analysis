import pandas as pd
import pickle
import streamlit as st
from PIL import Image
imagg = Image.open('pages/runs_score_byVK.png')
st.title('Runs scored (2008-2017)')
if st.button('Display the Graph'):
        st.image(imagg)
        st.text('Conclusion')
        st.text('The Maximun number of Runs are Scored in Year 2011.')