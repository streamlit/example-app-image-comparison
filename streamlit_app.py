import streamlit as st
from streamlit_image_comparison import image_comparison
import cv2

# set page config
st.set_page_config(
    page_title="James Webb Space Telescope vs Hubble Telescope Images",
    layout="centered",
)

st.image(
    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/telescope_1f52d.png",
    width=120,
)

st.header("J. Webb Space Telescope vs Hubble Telescope")

st.write("")
st.write("A simple tool to compare Webb's new images to Hubble!")
st.write("")

st.markdown("### Southern Nebula")

# render image-comparison
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/southern_nebula_700.jpg",
    img2="https://www.webbcompare.com/img/webb/southern_nebula_700.jpg",
    label1="Hubble",
    label2="Webb",
)


st.markdown("### Galaxy Cluster SMACS 0723")

# render image-comparison
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/deep_field_700.jpg",
    img2="https://www.webbcompare.com/img/webb/deep_field_700.jpg",
    label1="Hubble",
    label2="Webb",
)
