import streamlit as st

st.title("Advanced Streamlit Concepts")

if st.button("Widget Behavior"):
    st.switch_page("pages/2- Widget Behavior.py")
if st.button("Execution Flow"):
    st.switch_page("pages/3- Execution Flow.py")
if st.button("Session State"):
    st.switch_page("pages/4- Session State.py")
if st.button("Cache"):
    st.switch_page("pages/5- Cache.py")
if st.button("Secrets and Config"):
    st.switch_page("pages/6- Secrets and Config.py")

st.page_link("https://docs.streamlit.io/", label="Streamlit Documentation Page", icon="🌎")

