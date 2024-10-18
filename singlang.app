#File: main.py
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Sign Language Translator",
    page_icon="👐")  #only set once in front page, the other 2 pages nonid


st.sidebar.markdown("""
    <h1 style='font-size: 36px;'>Signify</h1>
    <p style='font-size: 14px; color: grey;'>Bridging Signs, Connecting Worlds</p>
    <h5 style='font-size: 20px;'>Select a page: </h5
    """,
                    unsafe_allow_html=True)
page = st.sidebar.radio("",
                        ("Home", "Upload or Capture", "Real-time Detection"))

if page == "Home":
    st.write("# Welcome to the Sign Language Translator! 👐")

    st.markdown("""
        This application helps translate sign language to text and then to other languages.

        **👈 Select a page from the sidebar** to get started:

        ### How it works
        1. Upload or capture an image of sign language
        2. Our AI will interpret the signs and convert them to text
        3. You can then translate the text to your chosen language

        ### About
        This app uses OpenAI's GPT model for sign language interpretation and translation.
        """)

elif page == "Upload or Capture":
    import upload  # 1 and 2 infront will caused error

elif page == "Real-time Detection":
    import real

