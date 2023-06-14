# From tutorial: https://medium.com/databutton/getting-started-with-langchain-a-powerful-tool-for-working-with-large-language-models-286419ba0842

#!pip install -r requirements.txt

import streamlit as st 
from langchain.chains import LLMChain, SimpleSequentialChain 
from langchain.llms import OpenAI 
from langchain.prompts import PromptTemplate 

# Set the title of the Streamlit app
st.title("✅ What's TRUE  : Using LangChain `SimpleSequentialChain`")

# Add a link to the Github repository that inspired this app
st.markdown("Inspired from [fact-checker](https://github.com/jagilley/fact-checker) by Jagiley")

# Set the GPT-3 API key
API = st.secrets["pass"]

# If an API key has been provided, create an OpenAI language model instance
if API:
    llm = OpenAI(temperature=0.7, openai_api_key=API)
else:
    # If an API key hasn't been provided, display a warning message
    st.warning("Enter your OPENAI API-KEY. Get your OpenAI API key from [here](https://platform.openai.com/account/api-keys).\n")

# Add a text input box for the user's question
user_question = st.text_input(
    "Enter Your Question : ",
    placeholder = "Cyanobacteria can perform photosynthetsis , are they considered as plants?",
)