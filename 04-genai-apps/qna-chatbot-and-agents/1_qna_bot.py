from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm= ChatGoogleGenerativeAI(model="gemini-3.6-flash")
st.title("AskBuddy - AI QnA Bot")
st.markdown("My QnA Bot with Langchain and Google Gemini !")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    role=message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)

query=st.chat_input("Ask anything?")
if query:
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("user").markdown(query)
    res=llm.invoke(query)
    if isinstance(res.content, list):
        answer = res.content[0]["text"]
    else:
        answer = res.content
    st.chat_message("ai").markdown(answer)
    st.session_state.messages.append({"role":"ai","content":answer})
