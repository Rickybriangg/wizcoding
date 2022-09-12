import streamlit as st
from PIL import Image

st.title("photo")

image = Image.open("image/pic profile.jpeg")
#st.image(image,caption="The beautiful villas hotel")

image1 =Image.open("image/pic4.jpeg")
#st.image(image1,caption="The fabulous interior")

image2 = Image.open("image/pic3.jpeg")

col1,col2,col3= st.columns(3)
with col1:
    st.image(image1, caption="The fabulous interior")


with col2:
    st.image(image,caption="The beautiful villas hotel")

with col3:
    st.image(image2,caption="The serene interior")
