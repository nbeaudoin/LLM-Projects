# Video tutorial: https://www.youtube.com/@Avra_b/videos

#!pip install -r requirements.txt

import openai
import streamlit as st

openai.api_key = st.secrets['pass']

# Setup up Streamlit UI
st.header("Summarizer App using OpenAI + Streamlit")

# Layout box 
article_text = st.text_area("Enter your text you want to summarize")
output_size = st.radio(label="What kind of output do you want?",
                       options=["To-the-point",
                                "Concise",
                                "Detailed"])

if output_size == "To-the-point":
    out_token = 50,
elif output_size == "Concise":
    out_token = 128
else:
    out_token = 516

if len(article_text) > 100:
    if st.button("Generate Summary", type="primary"):
        # Use GPT to generate a summary of the article
        response = openai.Completion.create(
            engine = "text-davinci-002",
            prompt = "Please summarize this scientific article for me in a few seconds : " + article_text,
            max_tokens = out_token,
            temperature = 0.5
        )

        # Print the summary
        res = response["choices"][0]["text"]
        st.info(res)
        st.download_button("Download Result", res)
else:
    st.warning("The sentence is not long enough!")