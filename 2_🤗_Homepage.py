import pandas as pd
import streamlit as st
from PIL import Image

EMAIL = "rickybriangg@gmail.com"
SOCIAL_MEDIA = {
    "Facebook": "https://www.facebook.com/profile.php?id=100077698713869",
    "Instagram": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}

st.set_page_config(page_title="silent villa plams",page_icon=':hotel:',layout="wide")

st.sidebar.success("Select the page above")


logo = Image.open("image/logo.png")
logo2 =Image.open("image/logo2.png")


col5,col6 = st.columns(2)
with col5:
    st.image(logo)

with col6:
    st.image(logo2)


st.write("----")
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


st.title("SILENT VILLA PLAMS")
st.markdown("Affordable ,reliable,explict and comfortability")

st.caption("A place where everyone desires")
st.markdown("The silent villas plams in silent environment ")



