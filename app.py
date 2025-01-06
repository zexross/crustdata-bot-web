import streamlit as st
from business_logic import make_request

# Set the title of the app
st.title("Crustdata Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

# React to user input
if prompt := st.chat_input("Ask a question"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "text": prompt})

    # Generate response from backend
    history = st.session_state.messages

    # Show a loading spinner while waiting for the response
    with st.spinner("Generating response..."):
        response = make_request(query=prompt, history=history)

    if response['status'] == 'success':
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response['response'])
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "text": response['response']})
    else:
        # Display an error message if the request fails
        st.error(response['error'])