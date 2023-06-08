#!pip install -r requirements.txt

import openai
import streamlit as st

openai.api_key = st.secrets['pass']

# Setup up Streamlit UI
st.header("Summarizer App using OpenAI + Streamlit")

# Layout box 
article_text = st.text_area("Enter your text you want to summarize")