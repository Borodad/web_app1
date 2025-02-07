import functions
import FreeSimpleGUI as sgui

label = sgui.Text("Type in a to do")
input_box = sgui.InputText(tooltip="Enter to do", key="todo") # set key value to "todo"
add_button = sgui.Button("Add")
list_box = sgui.Listbox(values=functions.get_to_do_list(), key="list_of_existing_to_dos",
                        enable_events=True, size=[45, 10])
edit_button = sgui.Button("Edit")
complete_button = sgui.Button("Complete")
exit_button = sgui.Button("Exit")

mywindow = sgui.Window("My to do App",
                       layout=[[label],
                               [input_box, add_button],
                               [list_box, edit_button, complete_button],
                               [exit_button]],
                       font = ("Helvetica", 15))                     # create a window called "My to do App"

while True:
    event, values = mywindow.read()
    print(event)     # label of event
    print(values)    # dictionary tuple
    print(values["list_of_existing_to_dos"])
    match event:
        case "Add":
            to_do_list = functions.get_to_do_list()
            new_to_do = values['todo'] + "\n" # ie get the value of the dictionary tuple with key 'todo' ie the input
            to_do_list.append(new_to_do)
            functions.write_to_do_list(to_do_list)
            mywindow["list_of_existing_to_dos"].update(values=to_do_list)
        case "Edit":
            print(values["list_of_existing_to_dos"][0])
            to_do_item_to_edit = values["list_of_existing_to_dos"][0] # 0 is the index value of the chosen item
            new_to_do = values["todo"] # value entered in the add field

            list_of_to_dos = functions.get_to_do_list()
            index = list_of_to_dos.index(to_do_item_to_edit)
            list_of_to_dos[index] = new_to_do
            functions.write_to_do_list(list_of_to_dos)
            mywindow["list_of_existing_to_dos"].update(values=list_of_to_dos)
        case "Complete":
            to_do_to_complete = values["list_of_existing_to_dos"][0]
            list_of_to_dos = functions.get_to_do_list()
            list_of_to_dos.remove(to_do_to_complete)
            functions.write_to_do_list(list_of_to_dos)
            mywindow["list_of_existing_to_dos"].update(values=list_of_to_dos)
            mywindow["todo"].update(value="")
        case "Exit":
            break
        case "list_of_existing_to_dos":
            mywindow["todo"].update(value=values["list_of_existing_to_dos"][0]) # points to input field & puts in item highlighted in the list
        case sgui.WIN_CLOSED:    # WIN_CLOSED is a boolean variable set in FreeSimpleGUI
            break                # finish the programme

print("Bye")
mywindow.close()





