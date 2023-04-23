import pandas as pd
import pickle
import streamlit as st
from PIL import Image
imagg = Image.open('matches_different_position.png')
st.title('Batting Order')
if st.button('Display the Graph'):
        st.image(imagg)
        st.text('Conclusion')
        st.text('From above we can say that, Virat Score highest Score at Batting Positon 3..')