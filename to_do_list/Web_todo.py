import streamlit as st # streamlit is a set of 3rd party web functions
import functions # my back end read & write functions for the todolist.txt file

todos = functions.get_to_do_list()

st.title("my To Do app")
st.subheader("This is my to do app")
st.write("This app manages to dos")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a to do:", placeholder="Add a new to do...")
