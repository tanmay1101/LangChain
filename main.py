## Integrate our code with OpenAI API

import os
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st 

os.environ['OPENAI_API_KEY'] = openai_key

# Streamlit framework

st.title('Langchain Demo with OpenAI API')
input_text= st.text_input('Search the topic you want to search')

## OPENAI LLMS
llm= OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))