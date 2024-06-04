import streamlit as st
import random
import string

st.title("Cache")

with st.echo(code_location="below"):
	if "input_length" not in st.session_state:
		st.session_state["input_length"] = 5

	@st.cache_data()
	def generate_random_string_cache(length=st.session_state["input_length"]):
		return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

	def generate_random_string(length=st.session_state["input_length"]):
		return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
		
	col1, col2 = st.columns(2)
	with col1:
		if st.button("Random String", use_container_width=True):
			random_string = generate_random_string(st.session_state["input_length"])
			st.session_state["output_text"] = random_string

	with col2:
		if st.button("Random String w/ Cache", use_container_width=True):
			random_string = generate_random_string_cache(st.session_state["input_length"])
			st.session_state["output_text"] = random_string
	
	col3, col4 = st.columns(2)
	with col3:
		st.number_input("String Length", min_value=1, max_value=10, value=5, key="input_length", label_visibility="collapsed")
	with col4:
		if st.button("Clear Cache", use_container_width=True): 
			st.cache_data.clear()
			st.session_state["output_text"] = ""
			
	st.text_input(label="String Container", key="output_text")