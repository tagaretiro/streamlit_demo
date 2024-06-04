import streamlit as st
import datetime
import time

st.write("Streamlit provides several options for controlling how different elements are laid out on the screen.")

# Columns Widget	
st.header("Columns Widget")
st.write("Insert containers laid out as side-by-side columns.")
with st.echo():
	with st.container(border=1):
		col1, col2, col3 = st.columns(3)
		with col1:
		   st.header("A cat")
		   st.image("https://static.streamlit.io/examples/cat.jpg")

		with col2:
		   st.header("A dog")
		   st.image("https://static.streamlit.io/examples/dog.jpg")

		with col3:
		   st.header("An owl")
		   st.image("https://static.streamlit.io/examples/owl.jpg")

st.divider()
		
# Container Widget	
st.header("Container Widget")
st.write("Inserts an invisible container into your app that can be used to hold multiple elements.")
with st.echo():
	with st.container(border=1):
		st.write("This is inside the container.")
		
st.divider()
		

# Empty Widget	
st.header("Empty Widget")
st.write("Inserts a empty container into your app that can be used to hold a single element. This allows you to, for example, remove elements at any point, or replace several elements at once (using a child multi-element container).")
with st.echo():
	with st.container(border=1):
		placeholder = st.empty()
		if st.button("Replace Placeholder"):
			# Replace the placeholder with a chart:
			placeholder.line_chart({"data": [1, 5, 2, 6]})
	
st.divider()
	
# Expander Widget	
st.header("Expander Widget")
st.write("Inserts a container into your app that can be used to hold multiple elements and can be expanded or collapsed by the user. When collapsed, all that is visible is the provided label.")
with st.echo():
	with st.container(border=1):
		with st.expander("Open for a surpise!"):
			st.write("""pls send help""")
		
st.divider()		
		
# Popover Widget
st.header("Popover Widget")	
st.write("Inserts a multi-element container as a popover. It consists of a button-like element and a container that opens when the button is clicked. Opening and closing the popover will not trigger a rerun.")
with st.echo():
	with st.container(border=1):
		popover = st.popover("Filter items")
		red = popover.checkbox("Show red items.", True)
		blue = popover.checkbox("Show blue items.", True)

		if red:
			st.write(":red[This is a red item.]")
		if blue:
			st.write(":blue[This is a blue item.]")
		
st.divider()
		
# Form Widget	
st.header("Forms Widget")
st.write("Create a form that batches elements together with a \"Submit\" button. Every form must contain a st.form_submit_button and it cannot contain st.button & st.download_button.")
with st.echo():
	with st.container(border=1):
		with st.form("my_form"):
			st.write("Inside the form")
			slider_val = st.slider("Form slider")
			checkbox_val = st.checkbox("Form checkbox")

			# Every form must have a submit button.
			submitted = st.form_submit_button("Submit")
			if submitted:
				st.write("slider", slider_val, "checkbox", checkbox_val)

st.divider()

# Form Widget	
st.header("Tabs Widget")
st.write("Insert containers separated into tabs. Inserts a number of multi-element containers as tabs. Tabs are a navigational element that allows users to easily move between groups of related content.")
with st.echo():
	with st.container(border=1):
		tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
		with tab1:
		   st.header("A cat")
		   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

		with tab2:
		   st.header("A dog")
		   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

		with tab3:
		   st.header("An owl")
		   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


st.warning("All the content of every tab is always sent to and rendered on the frontend. Conditional rendering is currently not supported.")

st.divider()

		
# Sidebar Widget	
st.header("Sidebar Widget")
st.write("Add widgets to sidebar.")
with st.echo():
	if st.button("Add Sidebar Widget"):
		with st.sidebar:
			st.header("This is a new sidebar element!")
