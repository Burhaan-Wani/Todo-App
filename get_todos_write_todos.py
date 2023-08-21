FILEPATH = "todos.txt"


def get_todos(file_path=FILEPATH):
    with open(file_path, "r") as file_local:
        todo_local = file_local.readlines()
        return todo_local


def write_todos(todo_arg, file_path=FILEPATH):
    with open(file_path, "w") as files_local:
        files_local.writelines(todo_arg)
