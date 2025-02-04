import functions
import FreeSimpleGUI as sgui

label = sgui.Text("Type in a to do")
input_box = sgui.InputText(tooltip="Enter to do", key="todo") # set key value to "todo"
add_button = sgui.Button("Add")

mywindow = sgui.Window("My to do App",
                       layout=[[label], [input_box, add_button]],
                       font = ("Helvetica", 15))                     # create a window called "My to do App"

while True:
    event, values = mywindow.read()
    print(event)     # label of add_button
    print(values)    # dictionary tuple
    match event:
        case "Add":
            to_do_list = functions.get_to_do_list()
            new_to_do = values['todo'] + "\n" # ie get the value of the dictionary tuple with key "todo" ie the input
            to_do_list.append(new_to_do)
            functions.write_to_do_list(to_do_list)
        case sgui.WIN_CLOSED:    # WIN_CLOSED is a boolean variable set in FreeSimpleGUI
            break              # finish the programme

mywindow.close()





