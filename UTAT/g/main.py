import numpy as np
import streamlit as st
from PIL import Image

SEEDLING_EMOJI_URL = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/facebook/65/seedling_1f331" \
                      ".png "
page_title = "Weed Detector"


# Set page title and favicon.
st.set_page_config(
    page_title=page_title,
    page_icon=SEEDLING_EMOJI_URL
)


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://get.wallhere.com/photo/sunlight-trees-landscape-hill-nature-grass-sky-field-photography-green-morning-farm-atmosphere-steppe-grassland-pasture-agriculture-meadow-plantation-plain-1920x1080-px-lawn-highland-prairie-crop-rural-area-computer-wallpaper-atmosphere-of-earth-ecosystem-grass-family-ecoregion-789185.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 




st.markdown(f'<h1 style="color:#000000;font-size:35px;">{"Weed Recognizer"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#000000;font-size:24px;">{"Our project helps identify weeds in a farm."}</h1>', unsafe_allow_html=True)


# st.button('Try it out!!')

