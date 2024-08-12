import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
secret_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=secret_key)

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get response from the model
def get_chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit interface
# st.set_page_config(page_title="Enter API kry", layout="left")
st.set_page_config(page_title="Simple ChatBot", layout="centered")


st.title("✨ Simple ChatBot ✨")
st.write("Powered by Google Generative AI")

if "history" not in st.session_state:
    st.session_state["history"] = []
# Display chat history after it's updated
for user_message, bot_message in st.session_state.history:
    st.markdown(f"""
    <div style="
        background-color: #800080; 
        border-radius: 15px; 
        padding: 10px 15px; 
        margin: 5px 0; 
        max-width: 70%; 
        text-align: left; 
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>You:</b> {user_message} 😊</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="
        background-color:  #808080; 
        border-radius: 15px; 
        padding: 10px 15px; 
        margin: 5px 0; 
        max-width: 70%; 
        text-align: left; 
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>Bot:</b> {bot_message} 🤖</p>
    </div>
    """, unsafe_allow_html=True)


# Form for user input
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("", max_chars=2000)
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input:
            response = get_chatbot_response(user_input)
            st.session_state.history.append((user_input, response))
            
        else:
            st.warning("Please Enter A Prompt")

