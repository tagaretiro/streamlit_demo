import streamlit as st
import pandas as pd
import numpy as np


# Dataframe Widget
st.header("Dataframe Widget")
st.write("This command works with dataframes from Pandas, PyArrow, Snowpark, and PySpark. It can also display several other types that can be converted to dataframes, e.g. numpy arrays, lists, sets and dictionaries.")
with st.echo():
	df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
	st.dataframe(df) 
st.write("Dataframes displayed with st.dataframe are interactive. End users can sort, resize, search, and copy data to their clipboard.")

st.write("st.table() is also able if you just want to display static data without any interactivity")

st.divider()

# DataEditor Widget
st.header("DataEditor Widget")
st.write("The data editor widget allows you to edit dataframes and many other data structures in a table-like UI.")
with st.echo():
	df = pd.DataFrame(
		[
		   {"command": "st.selectbox", "rating": 4, "is_widget": True},
		   {"command": "st.balloons", "rating": 5, "is_widget": False},
		   {"command": "st.time_input", "rating": 3, "is_widget": True},
		]
	)
	# You can also allow the user to add and delete rows by setting num_rows to "dynamic"
	edited_df = st.data_editor(df, num_rows="dynamic")

	favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
	st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
	
st.divider()	

st.header("Metric Widget")
st.write("The metric widget allows you to display a metric in big bold font, with an optional indicator of how the metric changed.")
with st.echo():
	st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
	
st.divider()

st.header("JSON Widget")
st.write("Streamlit also has a JSON widget to pretty-print JSON string.")	
with st.echo():
	st.json({
		'foo': 'bar',
		'baz': 'boz',
		'stuff': [
			'stuff 1',
			'stuff 2',
			'stuff 3',
			'stuff 5',
		],
	})
	