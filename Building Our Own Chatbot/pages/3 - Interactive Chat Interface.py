import streamlit as st

st.title("Interactive Chat Interface")

with st.container():
	st.write('''In this section, we'll build a bot that echoes our input. We'll use st.chat_message to display the user's input and st.chat_input to accept user input. We'll also use session state to store the chat history so we can display it in the chat message container.

First, let's think about the different components we'll need to build our bot:

- A way to store the chat history so we can display it in the chat message containers. We can use a list to store the messages, and append to it every time the user or bot sends a message. Each entry in the list will be a dictionary with the following keys: role (the author of the message), and content (the message content).
- A chat input widget so the user can type in a message.
- A message container to display messages from the user and the bot, respectively.

We used the :red[:=] operator to assign the user's input to the prompt variable and checked if it's not :red[None] in the same line. If the user has sent a message, we display the message in the chat message container and append it to the chat history.''')
	
    
pycode = '''# Initialize chat history
if "messages_demo" not in st.session_state:
    st.session_state.messages_demo = []

# Display chat messages from history on app rerun
for message in st.session_state.messages_demo:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages_demo.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history	
    st.session_state.messages_demo.append({"role": "assistant", "content": response})
'''
with st.container():
	st.code(pycode, language='python')
    
st.divider()
    
# Initialize chat history
if "messages_demo" not in st.session_state:
    st.session_state.messages_demo = []

# Display chat messages from history on app rerun
for message in st.session_state.messages_demo:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages_demo.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history	
    st.session_state.messages_demo.append({"role": "assistant", "content": response})


