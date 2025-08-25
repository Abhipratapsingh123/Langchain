import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Load API key
load_dotenv()

# Initialize model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful AI assistant")
    ]

st.title("💬 AI Chatbot")

# Display chat history
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# Chat input (like console input)
if user_input := st.chat_input("Type your message..."):
    # Append user message
    st.session_state.chat_history.append(HumanMessage(content=user_input))# type: ignore

    # Display immediately
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response
    result = model.invoke(st.session_state.chat_history)

    # Append AI response
    st.session_state.chat_history.append(AIMessage(content=result.content))# type: ignore

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(result.content)
