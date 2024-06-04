import streamlit as st
import datetime
import time

st.write("Streamlit provides a few methods that allow you to add animation to your apps. These animations include progress bars, status messages (like warnings), and celebratory balloons.")

st.header("Success Widget")
st.write("Display a success message.")
with st.echo():
	st.success('This is a success message!', icon="✅")
	
st.divider()
	
st.header("Information Widget")
st.write("Display a informational message.")
with st.echo():
	st.info('This is a purely informational message', icon="ℹ️")
	
st.divider()
	
st.header("Warning Widget")
st.write("Display a warning message.")
with st.echo():
	st.warning('This is a warning', icon="⚠️")
	
st.divider()

st.header("Error Widget")
st.write("Display a error message.")
with st.echo():
	st.error('This is an error', icon="🚨")
	
st.divider()

st.header("Exception Widget")
st.write("Display a exception message.")
with st.echo():
	e = RuntimeError('This is an exception of type RuntimeError')
	st.exception(e)
	
st.divider()

st.header("Progress Bar Widget")
st.write("Display a progress bar.")
with st.echo():
	with st.container(border=1):
		progress_text = "Operation in progress. Please wait."
		my_bar = st.progress(0, text=progress_text)

		for percent_complete in range(100):
			time.sleep(0.01)
			my_bar.progress(percent_complete + 1, text=progress_text)
		time.sleep(1)
		my_bar.empty()

		st.button("Rerun")
		
st.divider()

st.header("Toast Widget")
st.write("Display a short message, known as a notification \"toast\".")
with st.echo():
	if st.button("Show Toast"):
		st.toast("Hello GenAI forum!")
	
st.header("Balloons Widget")
st.write("Draw celebratory balloons.")
with st.echo():
	if st.button("Balloon Me"):
		st.balloons()
	
st.divider()