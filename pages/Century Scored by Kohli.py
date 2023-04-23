import pandas as pd
import pickle
import streamlit as st
from PIL import Image
imagg = Image.open('pages/nooftimevk_scoredcentury.png')
st.title('Century Scored by Kohli')
if st.button('Display the Graph'):
        st.image(imagg)
        st.text('Conclusion')
        st.text('He has scored five times century against Australia.')