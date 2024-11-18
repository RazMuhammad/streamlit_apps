import streamlit as st
import google.generativeai as genai

# Streamlit interface
st.set_page_config(page_title="Simple ChatBot", layout="wide")

st.title("✨ Simple ChatBot ✨")
st.write("Powered by Google Generative AI")

# Initialize the Generative Model
api_key = "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"
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get response from the model
def get_chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

# Function to display assistant's response
def display_assistant_response():
    with st.chat_message("assistant"):
        # Get the assistant's response (non-streaming)
        response = get_chatbot_response(st.session_state.messages[-1]["content"])
        st.write(response)  # Display response in the chat
        return response

# Main content area
st.header("Chat with the Bot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []  # Initialize message history

# Display chat history after it's updated
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    
    if role == "user":
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
            <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>You:</b> {content} 😊</p>
        </div>
        """, unsafe_allow_html=True)
    
    if role == "assistant":
        st.markdown(f"""
        <div style="
            background-color: #808080; 
            border-radius: 15px; 
            padding: 10px 15px; 
            margin: 5px 0; 
            max-width: 70%; 
            text-align: left; 
            display: inline-block;
        ">
            <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>Bot:</b> {content} 🤖</p>
        </div>
        """, unsafe_allow_html=True)

# Form for user input
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Enter your message:", max_chars=2000, label_visibility="collapsed")
    submit_button = st.form_submit_button("Send")

if submit_button:
    if user_input:
        # Add user's message to session state
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Display user's message immediately
        st.chat_message("user").write(user_input)
        
        # Get and display assistant's response
        response = display_assistant_response()
        
        # Add assistant's message to session state
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.warning("Please Enter A Prompt")
