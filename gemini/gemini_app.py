import streamlit as st
from groq import Groq

# Initialize the Groq client with the API key from Streamlit secrets
client = Groq(api_key="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")
st.header("Chat with Bot!")
# Set a default model for Groq
if "groq_model" not in st.session_state:
    st.session_state["groq_model"] = "llama3-8b-8192"  # Adjust the model name if needed

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate the assistant response using Groq API
    with st.chat_message("assistant"):
        try:
            # Call the Groq API to get the assistant's response
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                model=st.session_state["groq_model"],
            )

            # Extract the assistant's message content
            response = chat_completion.choices[0].message.content

            # Display the assistant's response in the chat message container
            st.markdown(response)
            
            # Add assistant's response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})

        except Exception as e:
            st.error(f"An error occurred: {e}")
