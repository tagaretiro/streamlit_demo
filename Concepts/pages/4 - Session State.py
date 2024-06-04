import streamlit as st

st.title("Session State")

with st.echo(code_location="below"):
	if "counter" not in st.session_state:
		st.session_state.counter = 0

	st.session_state.counter += 1

	st.header(f"This page has run {st.session_state.counter} times.")
	st.button("Run it again")