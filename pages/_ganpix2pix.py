import streamlit as st
from PIL import Image

st.title('pix2pix')

st.text('The purpose here is to use pix2pix to generate openstreet image from satellite image like this :')

image = Image.open('satimgganpi2pi.PNG')

#displaying the images on streamlit app

st.image(image, caption='Typical example')