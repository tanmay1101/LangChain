## Integrate our code with OpenAI API

import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

import streamlit as st 

os.environ['OPENAI_API_KEY'] = openai_key

# Streamlit framework

st.title('Celebrity Search Results')
input_text= st.text_input('Search the topic you want to search')

# Prompt Template

first_input_prompt= PromptTemplate(
    input_variables=['name'],
    template= "Tell me about celebrity {name}"
)




## OPENAI LLMS
llm= OpenAI(temperature=0.8)
chain= LLMChain(llm = llm , prompt= first_input_prompt, verbose= True)

if input_text:
    st.write(chain.run(input_text))