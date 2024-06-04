import streamlit as st


st.title("Secrets and Config")

st.header("Secrets Management")

st.write("You can fetch the need key-value from your secrets file and pass it to your app.")
secrets_body='''[demo_key]
secret_value="THIS IS A SECRET KEY"'''
st.code(secrets_body, 'toml')

with st.echo(code_location="below"):
	secret_value = st.secrets.demo_key.secret_value

	# !!! THIS IS FOR DEMO PURPOSES ONLY. DO NOT PRINT SECRET VALUES IN PRODUCTION !!!
	with st.container(border=3):
		st.write(f"Your secret value is: {secret_value}")

st.divider()

st.header("Configuration Management")

config_body='''[server]
maxUploadSize=15'''
st.code(config_body, 'toml')

st.write("Setting the config.toml for maxUploadSize=15 will limit the file_uploader widget.")

with st.echo(code_location="below"):
	st.file_uploader("demo_upload", disabled=True, label_visibility="collapsed")