import streamlit as st
import time

st.title("Chat Widgets")

st.write("Streamlit provides a few commands to help you build conversational apps. These chat elements are designed to be used in conjunction with each other, but you can also use them separately.")

# Chat Message Widget	
st.header("Chat Message")
chatm_api = '''st.chat_message(name, avatar=None)'''
st.code(chatm_api, 'python')
st.write("Insert a chat message container.")
with st.echo():
	with st.container(border=1):
		with st.chat_message("user"):
			st.write("Hello 👋")
		with st.chat_message("assistant"):
			st.write("Hi 👋")

st.divider()	
		

# Chat Input Widget	
st.header("Chat Input")
chati_api = '''st.chat_input(placeholder="Your message", *, key=None, max_chars=None, disabled=False, on_submit=None, args=None, kwargs=None)'''
st.code(chati_api, 'python')
st.write("Display a chat input widget.")
with st.echo():
	with st.container(border=1):
		prompt = st.chat_input("Say something")
		if prompt:
			st.write(f"User has sent the following prompt: {prompt}")

st.divider()


with st.container():
	# Stream Widget
	st.header("Write Stream")
	_LOREM_IPSUM = """
	Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
	incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
	nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
	"""
	st.write("This is a streamed text: ")

	# !!! THIS IS JUST A SAMPLE FUNCTION TO OUTPUT A STREAM !!!
	def stream_data():
		for word in _LOREM_IPSUM.split(" "):
			yield word + " "
			time.sleep(0.1)
	# !!! FOR ACTUAL USE CASES PLEASE USE A PROPER STREAM PARAMETER (Callable, Generator, Iterable, OpenAI Stream, or LangChain Stream) !!!

	st.write_stream(stream_data)

	# Code widget example in python language
	pycode = '''st.write_stream(stream_data)'''
	st.code(pycode, language='python')

	st.write("Stream data must be a generator, iterable, or an OpenAI/Langchain Stream")

		
# Status Widget
st.header("Status Container")
st.write("Insert a status container to display output from long-running tasks.")
with st.echo():
	with st.container(border=1):
		with st.status("Downloading data..."):
			st.write("Searching for data...")
			time.sleep(2)
			st.write("Found URL.")
			time.sleep(1)
			st.write("Downloading data...")
			time.sleep(1)

		st.button("Rerun")
		
st.divider()