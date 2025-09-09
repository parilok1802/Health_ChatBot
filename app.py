# app.py
import streamlit as st
from openai import OpenAI

# OpenRouter Client
client = OpenAI(
    api_key="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",   # <-- apni OpenRouter API key yaha daalo
    base_url="https://openrouter.ai/api/v1"
)

st.set_page_config(page_title="CareAway Chatbot", page_icon="💬")
st.title("🤖 CareAway Healthcare Assistant")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a healthcare assistant AI."}
    ]

# Display old messages
for msg in st.session_state.messages[1:]:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# Input box
if prompt := st.chat_input("Ask about symptoms, services, or care..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324:free",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"⚠️ Error: {str(e)}"

    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
