import streamlit as st
import time

# Write Widget
st.header("Write Widget")
st.write("This is a normal text")
# Code widget example in python language
pycode = '''st.write("This is a normal text")'''
st.code(pycode, language='python')

st.divider()

with st.container():
	# Stream Widget
	st.header("Stream Text Widget")
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

st.divider()

# Echo Widget
st.header("Echo Widget")
st.write("You can use echo to display both the graphic elements and the code that generated it. Super useful for making tutorials/explanatory visuals")

def get_user_name():
    return 'John'

with st.echo():
    st.write("Everything inside this block will be executed and printed after!")

st.divider()

# Code Widget
st.header("Code Widget")
st.write("You can use st.code() if you just want to display code with syntax-highlights. Unlike st.echo(), the code won't be executed.")
# Code widget example in python language
pycode = '''st.code(st.write("Hello! This is a test python code!"), language='python')'''
st.code(pycode, language='python')

st.divider()

# LaTeX Widget
st.header("LaTeX Widget")
st.write("You can use LaTeX widget to print out mathematical formulas.")
with st.echo():
	st.latex(r'''
		a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
		\sum_{k=0}^{n-1} ar^k =
		a \left(\frac{1-r^{n}}{1-r}\right)
		''')

st.divider()		
		
# Markdown Widget
st.header("Markdown Widget")
markdown_text = ''':red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in] :gray[pretty] :rainbow[colors] and :blue-background[highlight] text by using st.markdown()'''
st.markdown(markdown_text)

pycode = f'''st.markdown(\'\'\'{markdown_text}\'\'\')
st.markdown(markdown_text)'''
st.code(pycode, language='python')



	