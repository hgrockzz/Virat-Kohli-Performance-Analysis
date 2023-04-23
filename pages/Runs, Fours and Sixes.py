import pandas as pd
import pickle
import streamlit as st
from PIL import Image
imagg = Image.open('relationbetween_run_fours.png')
st.title('Runs,Fours and Sixes')
if st.button('Display the Graph'):
        st.image(imagg)
        st.text('Conclusion')
        st.text('- There is a linear relationship between Runs and 4s, which means the more he scores in the innings, the more 4s he hits.')
        st.text('- However, there is no strong linear relationship between Runs and 6s.')