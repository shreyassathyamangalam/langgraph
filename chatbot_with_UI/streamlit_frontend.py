import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

CONFIG = {'configurable': {'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


# load the message history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# {'role': 'user', 'content': 'Hi'}
# {'role': 'assistant', 'content': 'Hello, how can I assist you today?'}


# Create a chat input box
user_input = st.chat_input(placeholder="Type you message here...")

# Display the user input in the chat area
if user_input:
    
    # Add the user input to the message history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message("user"):
        st.text(user_input)
        
    
    response = chatbot.invoke({"messages": [HumanMessage(content=user_input)]}, config=CONFIG)
    ai_message = response['messages'][-1].content
    # Add the assistant input to the message history
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})    
    with st.chat_message("assistant"):
        st.text(ai_message)

