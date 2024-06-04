import streamlit as st

# Title Widget
st.title("This is your title")

# Code widget example in python language
pycode = '''st.title("This is your title")'''
st.code(pycode, language='python')

# Header Widget
st.header("This is your header")
# Code widget example in python language
pycode = '''st.header("This is your header")'''
st.code(pycode, language='python')

# Subheader Widget
st.subheader("This is your subheader")
# Code widget example in python language
pycode = '''st.subheader("This is your subheader")'''
st.code(pycode, language='python')

# Subheader Widget
st.subheader("You can also add dividers!", divider="rainbow")
# Code widget example in python language
pycode = '''st.subheader("You can also add dividers!", divider="rainbow")'''
st.code(pycode, language='python')




