import functions
import FreeSimpleGUI as sgui

label = sgui.Text("Type in a to do")
input_box = sgui.InputText(tooltip="Enter to do")
add_button = sgui.Button("Add")

mywindow = sgui.Window("My to do App", layout=[[label], [input_box, add_button]]) # create a window called "My to do App"
mywindow.read()
mywindow.close()





