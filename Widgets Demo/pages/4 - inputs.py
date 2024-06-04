import streamlit as st
import datetime

st.write("With widgets, Streamlit allows you to bake interactivity directly into your apps with buttons, sliders, text inputs, and more.")

# Text Input Widget	
st.header("Text Input Widget")
st.write("A single-line text input widget.")
with st.echo():
	with st.container(border=1):
		title = st.text_input("Movie title", "Life of Brian")
		st.write("The current movie title is", title)

st.divider()	

# Multi-Text Input Widget
st.header("Multi-Line Text Input Widget")	
st.write("A multi-line  text input widget.")
with st.echo():
	with st.container(border=1):
		txt = st.text_area(
			"Text to analyze",
			"It was the best of times, it was the worst of times, it was the age of "
			"wisdom, it was the age of foolishness, it was the epoch of belief, it "
			"was the epoch of incredulity, it was the season of Light, it was the "
			"season of Darkness, it was the spring of hope, it was the winter of "
			"despair, (...)",
		)
		st.write(f"You wrote {len(txt)} characters.")

st.divider()	

# Number Widget	
st.header("Numeric Input Widget")
st.write("A numeric input widget")
with st.echo():
	with st.container(border=1):
		number = st.number_input("Insert a number")
		st.write("The current number is ", number)

st.divider()	

# Date Input Widget	
st.header("Date Input Widget")
st.write("A date input widget")
with st.echo():
	with st.container(border=1):
		d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
		st.write("Your birthday is:", d)

st.divider()	


# Button Widget	
st.header("Button Widget")
st.write("A simple button.")
with st.echo():
	with st.container(border=1):
		if st.button("Button", type="primary"):
			st.write("Button was clicked!")

st.divider()	
	
# Download Widget
st.header("Download Widget")	
st.write("Allow users to download a file directly from your app.")
with st.echo():
	text_contents = '''This is some text'''
	st.download_button("Download", text_contents)

st.divider()

# Link Button Widget	
st.header("Page Link Widget")
st.write("For linking external URLs, you can use st.link_button().")	
with st.echo():
	st.link_button("Go to gallery", "https://streamlit.io/gallery")

st.divider()	

# Selectbox Widget	
st.header("Selectbox Widget")
st.write("The st.selectbox() function facilitates dropdown menus implementation.")	
with st.echo():
	with st.container(border=1):
		agree = st.checkbox("I agree")
		if agree:
			st.write("Great!")

st.divider()	

# Multiselect Widget	
st.header("Multiselect Widget")
st.write("The st.multiselect() function is designed to meet multi-selection dropdown requirements.")	
with st.echo():
	with st.container(border=1):
		options = st.multiselect(
		"What are your favorite colors",
		["Green", "Yellow", "Red", "Blue"],
		["Yellow", "Red"])

		st.write("You selected:", options)
	
st.divider()

# Radio Widget	
st.header("Radio Widget")
st.write("The st.radio() function displays a radio button widget.")	
with st.echo():
	with st.container(border=1):
		genre = st.radio(
			"What's your favorite movie genre",
			["Comedy", "Drama", "Documentary"],
			index=None,
		)

		st.write("You selected:", genre)

st.divider()	
	
# Slider Widget	
st.header("Slider Widget")
st.write("Display a slider widget. It supports int, float, date, time, and datetime types.")	
with st.echo():
	with st.container(border=1):
		age = st.slider("How old are you?", 0, 130, 25)
		st.write("I'm ", age, "years old")

st.write("The difference between st.slider and st.select_slider is that slider only accepts numerical or date/time data and takes a range as input, while select_slider accepts any datatype and takes an iterable set of options.")

st.divider()

# Toggle Widget	
st.header("Toggle Widget")
st.write("The st.toggle() also allows you to render a toggle widget.")	
with st.echo():
	with st.container(border=1):
		on = st.toggle("Activate feature")
		if on:
			st.write("Feature activated!")
	
st.divider()

# Upload Widget
st.header("Upload Widget")
st.write("The st.file_uploader() function is used for handling file uploads.")	
with st.echo():
	with st.container(border=1):
		uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
		for uploaded_file in uploaded_files:
			bytes_data = uploaded_file.read()
			st.write("filename:", uploaded_file.name)
			st.write(bytes_data)
