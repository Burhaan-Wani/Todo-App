from get_todos_write_todos import *
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="Todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=get_todos(),
                      key="Todos",
                      enable_events=True,
                      size=[40, 10])
edit_btn = sg.Button("Edit")
layout = [[label], [input_box, add_button], [list_box, edit_btn]]

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
            window["Todos"].update(values=todo_list)
        case sg.WIN_CLOSED:
            break
        case "Todos":
            window["Todo"].update(value=values["Todos"][0])
        case "Edit":
            todo_to_edit = values["Todos"][0]
            new_todo = values['Todo']

            todo_list = get_todos()
            index = todo_list.index(todo_to_edit)
            todo_list[index] = new_todo
            write_todos(todo_list)
            window["Todos"].update(values=todo_list)
window.close()
