from get_todos_write_todos import *
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo",key="Todo")
add_button = sg.Button("Add")
layout = [[label], [input_box, add_button]]

window = sg.Window("My To-Do App",
                   layout,
                   font=("Helvetica", 12))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todo_list = get_todos()
            new_todo = values["Todo"] + "\n"
            todo_list.append(new_todo)
            write_todos(todo_list)
        case sg.WIN_CLOSED:
            break

window.close()
