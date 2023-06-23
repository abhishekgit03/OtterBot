import openai
import streamlit as st
from streamlit_chat import message
import pymongo
import os
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('api_secret')
print("openai.api_key=",openai.api_key)
client = pymongo.MongoClient(os.getenv('mongo_secret'))
db=client.myapp
userdb=db.userdb

def add_chat_log(agent,response, chat_log=None):
    if chat_log is None:
        chat_log = ""
    return f"{chat_log}{agent}: {response}\n"

def generate_response(prompt,unique_id):
    try:
        cust_info = userdb.find_one({"_id":unique_id})
        chat = cust_info['chat']
    except:
        userdb.insert_one({"_id":unique_id,"chat":""})
        cust_info = userdb.find_one({"_id":unique_id})
        chat = cust_info['chat']
    chat = add_chat_log("user", prompt, chat)
    userdb.update_one({"_id":unique_id},{"$set":{"chat":chat}})
    Chat_History = "\n".join(chat.splitlines()[-5:])
    print("Reached here")
    m=[{"role": "system", "content":"You are a helpful AI agent that can answer to any questions of the user. Your name is OtterBot"},
     {"role": "assistant", "content": str(Chat_History)},
    {"role": "user", "content": prompt}]
    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        max_tokens = 500,
        temperature = 0.3,
        messages=m)
    output=result["choices"][0]['message']['content']
    print("Reached here 1")
    chat = add_chat_log("assistant", output, chat)
    userdb.update_one({"_id":unique_id}, {"$set":{"chat":chat}})
    return output


st.title("👾 OtterBot : OpenAI GPT-3.5-Turbo-16k + Streamlit + MongoDB powered Chatbot")
unique_id=st.text_input("Enter your email-id:","", key="email")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.text_input("You: ","", key="input")
    print(input_text)
    return input_text 


user_input = get_text()

if user_input:
    output = generate_response(user_input,unique_id)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')