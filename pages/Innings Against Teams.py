import pandas as pd
import pickle
import streamlit as st
from PIL import Image
imagg = Image.open('pages/no_innings_against_teams.png')
st.title('Innings Against Teams')
if st.button('Display the Graph'):
        st.image(imagg)
        st.text('Conclusion')
        st.text('Virat has played highest Innings against Sri Lanka, followed by England.')