import pandas as pd
import pickle
import streamlit as st
from PIL import Image
imagg = Image.open('pages/runs_score_byVK')
st.title('Runs per Innings')
if st.button('Display the Graph'):
        st.image(imagg)
        st.text('Conclusion')
        st.text('- There is a linear relationship between Runs and 4s, which means the more he scores in the innings, the more 4s he hits.')