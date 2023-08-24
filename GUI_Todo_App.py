from get_todos_write_todos import *
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="Todo")
add_button = sg.Button("Add", size=[7, 1], font=("Helvetica", 11))
list_box = sg.Listbox(values=get_todos(),
                      key="Todos",
                      enable_events=True,
                      size=[37, 10])
edit_btn = sg.Button("Edit", size=[5, 1], font=("Helvetica", 11))
completed_btn = sg.Button("Completed", size=[8, 1], font=("Helvetica", 11))
Exit_btn = sg.Button("Exit", size=[8, 1], font=("Helvetica", 11))

layout = [[label], [input_box, add_button], [list_box, edit_btn, completed_btn], [Exit_btn]]

window = sg.Window("My To-Do App",
                   layout,
                   font=("Helvetica", 12))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todo_list = get_todos()
            new_todo = values["Todo"] + "\n"
            todo_list.append(new_todo)
            write_todos(todo_list)
            window["Todos"].update(values=todo_list)
            window["Todo"].update(value="")
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
        case "Completed":
            completed_todo = values["Todos"][0]
            todo_list = get_todos()
            index = todo_list.index(completed_todo)
            todo_list.pop(index)
            write_todos(todo_list)
            window["Todos"].update(values=todo_list)
            window["Todo"].update(value="")

        case "Exit":
            break

window.close()
