# 🦙 Sv Info Chatbot 🖥️

A simple Streamlit web app for using [LlamaIndex](https://github.com/jerryjliu/llama_index), an interface to connect LLM’s with external data.
The bot was trained with public data from "Allianz Zentrum für Technik" to provide support for german speaking automotive experts.

## 🚀 Context

- LLamaIndex lets you create a custom ChatGPT version especially for your specific data & documents 
- It doesn't provide an user interface so we create one using Steamlit
- The goal is to make it as easy as possible to create a custom ChatGPT clone and deploy it locally or on the web with a simply UI


## 💻 Installation

Clone the repo or download the files to zip 
```
git clone https://github.com/j4nc0r/svinfogpt.git
```
Install the required packages using PIP
```
pip install -r requirements.txt
```
(optional) If you already have created a Llama index somewhere else safe it the to JSON-files and copy them from your `./storage` folder to `./storage` in this repo.
To create JSON files from index use:
```
index.storage_context.persist()
```

## 🔧 Configuration 
### OpenAI API Key
(optional) If you don't have an OpenAI API Key go to [OpenAI](https://platform.openai.com/account/api-keys) and create one. <br><br>

Open `index.py` and insert your API secret key
```
os.environ['OPENAI_API_KEY']= "insert-your-key-here"
```
## 🏠 Test & Deploy locally

1. Run `index.py`
2. Deploy the Streamlit app in terminal:
```
streamlit run index.py
```
A browser should open and you're ready to chat with your personal ChatGPT clone

## 🚆 Deploy to the web with Railway


To deploy on [Railway](https://railway.app/?referralCode=01QhWs), click the button below.




