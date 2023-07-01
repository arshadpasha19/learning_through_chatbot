import streamlit as st
import pyttsx3
from streamlit_chat import message as st_message
import bot_code

if "history" not in st.session_state:
    st.session_state.history = []

st.title("How can I help you?")

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()

def answer():
    user_message = st.session_state.input_text
    if not user_message:
        return  # Exit early if no valid input

    if user_message.lower() == "quit":
        st.stop()

    message_bot = bot_code.generate_answer(user_message)
    st.session_state.history.append({"message": user_message, "is_user": True})
    st.session_state.history.append({"message": message_bot, "is_user": False})

    # Text output
    st_message(message=message_bot, is_user=False, key='unique_key')

    # Speech output
    speak_text(message_bot)

st.text_input("Talk to the bot", key="input_text", on_change=answer)

if st.button("Clear conversation history"):
    st.session_state.history = []

# Display the conversation history in reverse order
for i, chat in enumerate(reversed(st.session_state.history)):
    st_message(message=chat['message'], is_user=chat['is_user'], key=i)





