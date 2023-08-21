# TODO LIST
# from get_todos_write_todos import get_todos, write_todos
from get_todos_write_todos import *
import time
date_time = time.strftime("%b %d, %Y %H:%M:%S")
print("Today is", date_time)
while True:
    user_action = input("Add, Show, Edit, Completed or Exit: ").capitalize()
    user_action = user_action.strip()

    if user_action == "Add":
        todo = input("Enter a Todo: ") + "\n"

        todo_list = get_todos()

        todo_list.append(todo)
        write_todos(todo_list)

    elif user_action == "Show":
        todo_list = get_todos()

        # Method to remove breaks from list items
        # list comprehension method
        # new_list = [item.strip("\n") for item in todo_list]

        for index, item in enumerate(todo_list):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")

    elif user_action == "Edit":
        try:
            todo_list = get_todos("todos.txt")

            user_number = int(input("Number of Todo to Edit: "))
            user_number -= 1
            todo_list[user_number] = input("Enter a new todo: ") + "\n"
            write_todos(todo_list)
        except ValueError:
            print("number takes only integer type value")

    elif user_action == "Completed":
        try:
            todo_list = get_todos()

            remove_todo = int(input("Number of Completed Todo: "))
            index = remove_todo - 1
            todo_to_remove = todo_list[index].strip("\n")
            todo_list.pop(index)

            write_todos(todo_list)
            print(f"Todo \"{todo_to_remove}\" was removed from Todo List")
        except ValueError:
            print("number takes only integer type value")

    elif user_action == "Exit":
        break
    else:
        print("Invalid Command")

print("Bye!")
