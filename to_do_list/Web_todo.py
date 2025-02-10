import streamlit as st
import functions # my back end read & write functions for the todolist.txt file

todos = functions.get_to_do_list()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n" # get value from the key / value pair
    todos.append(new_todo)
    functions.write_to_do_list(todos)


st.title("my To Do app")
st.subheader("This is my to do app")
st.write("This app manages to dos")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a to do:", placeholder="Add a new to do...",
              on_change=add_todo, key="new_todo")

# st.session_state # this will show the session state in the web app
