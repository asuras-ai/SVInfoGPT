import os, streamlit as st

# Uncomment to specify your OpenAI API key here (local testing only, not in production!), or add corresponding environment variable (recommended)
#os.environ['OPENAI_API_KEY']= ""

from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, PromptHelper, StorageContext, load_index_from_storage
from langchain import OpenAI

#load AZT Info Llama-Index from JSON files
# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="./storage")
# load index
index = load_index_from_storage(storage_context)
index = index.as_query_engine()

# Define a simple Streamlit app
st.title("SV Info Chatbot")
query = st.text_input("Wie kann ich Ihnen helfen?", "")
query_full = 'Answer a question. Add to the response the name of the source document and the page where the response can be verified. Answer in the language of the question. The question: ' + query

if st.button("Submit"):
    response = index.query(query_full)
    st.write(response)
