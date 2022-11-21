# import numpy as np
import streamlit as st
import streamlit.components.v1 as components
# from PIL import Image
# import utils as utl
from pages import patient

# st.set_page_config(layout="wide", page_title='Navbar sample')
# st.set_option('deprecation.showPyplotGlobalUse', False)
# utl.inject_custom_css()
# utl.navbar_component()
#
#
# def navigation():
#     route = utl.get_current_route()
#     if route == "home":
#         home.load_view()
#     elif route == "about":
#         about.load_view()
#     elif route == "analysis":
#         analysis.load_view()
#     elif route == "options":
#         options.load_view()
#     elif route == "configuration":
#         configuration.load_view()
#     elif route == None:
#         home.load_view()
#
#
# navigation()

u = "https://cdn.discordapp.com/attachments/1043363043947581533/1043716871876268132/DYGNOS__2_-removebg-preview.png"
page_title = "Welcome to DygnosTech"

# Set page title and favicon.
st.set_page_config(page_title=page_title, page_icon=u)

def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.discordapp.com/attachments/1043363043947581533/1043480856150409257/marcel-strauss-iCR53oVMqcs-unsplash.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True,
    )


add_bg_from_url()


path_to_html = "/Users/shiveshprakash/PycharmProjects/Pratham-Varshiya-Kaand/Nov-19/pages/tr.html"

# Read file and keep in variable
with open(path_to_html, 'r') as f:
    html_data = f.read()

# Show in webpage
components.html(html_data, width=2000, height=1000)