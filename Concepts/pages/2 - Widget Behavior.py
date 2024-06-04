import streamlit as st

st.title("Widget Behavior")

with st.echo(code_location="below"):
	x = st.slider('x', key='demo_slider')  # 👈 this is a widget

	st.write(f"This is the value of my slider widget: {x}")
	st.write(f"I can also recall this value from memory! Look: {st.session_state['demo_slider']}")