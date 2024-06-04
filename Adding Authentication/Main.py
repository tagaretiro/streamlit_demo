import streamlit as st
from streamlit_msal import Msal

st.title("ChatGPT-like Clone")

from openai import AzureOpenAI

api_key=st.secrets.openai_info.api_key
endpoint_url=st.secrets.openai_info.endpoint_url
api_version=st.secrets.openai_info.api_version
model_name=st.secrets.openai_info.model_name

msal_client_id=st.secrets.azure_info.a_client_id
msal_authority=st.secrets.azure_info.a_authority

client = AzureOpenAI(azure_endpoint=endpoint_url, api_key=api_key, api_version=api_version)

with st.sidebar:
	auth_data = Msal.initialize_ui(
		client_id=msal_client_id,
		authority=msal_authority,
		scopes=[], # Optional
		# Customize (Default values):
		connecting_label="Connecting",
		disconnected_label="Disconnected",
		sign_in_label="Sign in",
		sign_out_label="Sign out"
    )

if auth_data:
	with st.sidebar:
		st.json(auth_data)

	with st.container(border=1):
		if "messages" not in st.session_state:
			st.session_state.messages = []

		for message in st.session_state.messages:
			with st.chat_message(message["role"]):
				st.markdown(message["content"])

		if prompt := st.chat_input("What is up?"):
			st.session_state.messages.append({"role": "user", "content": prompt})
			with st.chat_message("user"):
				st.markdown(prompt)

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
			st.session_state.messages.append({"role": "assistant", "content": response})
		
		
	pycode = '''msal_client_id=st.secrets.azure_info.a_client_id
msal_authority=st.secrets.azure_info.a_authority

client = AzureOpenAI(azure_endpoint=endpoint_url, api_key=api_key, api_version=api_version)

with st.sidebar:
	auth_data = Msal.initialize_ui(
		client_id=msal_client_id,
		authority=msal_authority,
		scopes=[], # Optional
		# Customize (Default values):
		connecting_label="Connecting",
		disconnected_label="Disconnected",
		sign_in_label="Sign in",
		sign_out_label="Sign out"
    )

if auth_data:
	with st.sidebar:
		st.json(auth_data)
		#... continue code...'''
	st.code(pycode, language='python')