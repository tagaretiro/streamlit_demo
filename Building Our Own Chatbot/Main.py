import streamlit as st

# Title Widget
st.title("Building your first LLM Chat App")

body_text = '''The advent of large language models like GPT has revolutionized the ease of developing chat-based applications. Streamlit offers several Chat elements, enabling you to build Graphical User Interfaces (GUIs) for conversational agents or chatbots. Leveraging session state along with these elements allows you to construct anything from a basic chatbot to a more advanced, ChatGPT-like experience using purely Python code.

In this tutorial, we'll start by walking through Streamlit's chat elements, st.chat_message and st.chat_input. Then we'll proceed to construct three distinct applications, each showcasing an increasing level of complexity and functionality:

First, we'll Build a bot that mirrors your input to get a feel for the chat elements and how they work. We'll also introduce session state and how it can be used to store the chat history. This section will serve as a foundation for the rest of the tutorial.

Next, we'll Build a ChatGPT-like app that leverages session state to remember conversational context, all within less than 50 lines of code.'''

st.markdown(body_text)





