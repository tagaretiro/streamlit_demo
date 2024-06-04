import streamlit as st

st.title("ChatGPT-like Clone")

from openai import AzureOpenAI

api_key=st.secrets.openai_info.api_key
endpoint_url=st.secrets.openai_info.endpoint_url
api_version=st.secrets.openai_info.api_version
model_name=st.secrets.openai_info.model_name

client = AzureOpenAI(azure_endpoint=endpoint_url, api_key=api_key, api_version=api_version)

with st.container():
	st.write('''Now that you've understood the basics of Streamlit's chat elements, let's make a few tweaks to it to build our own ChatGPT-like app. You'll need to install the Azure OpenAI Python library and get an API key to follow along.''')
	
	st.code('pip install openai', 'bash')
	
	st.markdown('''We will use the same principles in our previous examples but now we will connect our interactive chat app with Azure AI Services. You can get your keys from the resources assigned to you. 
	Always use :red[SECRETS]  when dealing with credentials.''')
	
	st.code('''[openai_info]
api_key="-- Deployment API Key --"
endpoint_url="-- Deployment Endopoint URL --"
api_version="-- API Version --"
model_name="-- Deployment Model Name --"''', 'toml')


pycode = '''import streamlit
from openai import AzureOpenAI

# Get Azure OpenAI resource keys and information from secrets.toml
api_key=st.secrets.openai_info.api_key
endpoint_url=st.secrets.openai_info.endpoint_url
api_version=st.secrets.openai_info.api_version
model_name=st.secrets.openai_info.model_name

# Initialize Azure OpenAI client
client = AzureOpenAI(azure_endpoint=endpoint_url, api_key=api_key, api_version=api_version)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        # Get response from Completions API
        stream = client.chat.completions.create(
            model=model_name,
            # Get chat history from session state
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        # Write message as stream
        response = st.write_stream(stream)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})'''
with st.container():
	st.code(pycode, language='python')
    
st.divider()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
	
	
