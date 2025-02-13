import streamlit as st
import functions # my back end read & write functions for the todolist.txt

todos = functions.get_to_do_list() # call function to get list

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n" # get value from the key / value pair
    todos.append(new_todo)
    functions.write_to_do_list(todos)

st.title("my To Do app")
st.subheader("This is my to do app")
st.write("This app manages to dos")

for index, todo in enumerate(todos): # enumerate creates an index
    checkbox = st.checkbox(todo, key=todo) # ie key is the value of the to do
    if checkbox:   # ie if checkbox is true
        todos.pop(index) # remove the to do
        functions.write_to_do_list(todos)
        del st.session_state[todo] # remove from session state dictionary
        st.rerun() # re-show

st.text_input(label="Enter a to do:", placeholder="Add a new to do...",
              on_change=add_todo, key="new_todo")

# st.session_state # this will show the session state in the web app
