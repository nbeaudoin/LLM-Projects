# Video tutorial: https://www.youtube.com/@Avra_b/videos

#!pip install -r requirements.txt

import openai
import streamlit as st

openai.api_key = st.secrets['pass']

# Setup up Streamlit UI
st.header("Summarizer App using OpenAI + Streamlit")

# Layout box 
article_text = st.text_area("Enter your text you want to summarize")
temp = st.slider("temperature", 0.0, 1.0, 0.5)

if len(article_text) > 100:
    if st.button("Generate Summary"):
        # Use GPT to generate a summary of the article
        reponse = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = "Please summarize this scientific article for me in a few seconds : " + article_text,
            max_token = 516,
            temperature = temp
        )