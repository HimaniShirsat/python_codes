todo_list = []

def add_task(task):
    task = input("enter a task you want: ")
    todo_list.append ({"task":task, "completed" : False})
    print("Task added successfully!")


# def view_tasks():
#     if todo_list:
#         print("To-Do List:")
#         for index, task in enumerate(todo_list):
#             status = "Completed" if task["completed"] else "Incomplete"
#             print(f"{index + 1}. {task['task']} - Status: {status}")
#     else:
#         print("To-Do list is empty!")


# def update_task():
#     view_tasks()
#     task_number = int(input("Enter the number of the task to update: ")) - 1

#     if 0 <= task_number < len(todo_list):
#         new_task = input("Enter the updated task: ")
#         todo_list[task_number]["task"] = new_task
#         print("Task updated successfully!")
#     else:
#         print("Invalid task number.")

# def delete_task(index):
#     view_tasks()
#     task_number=int(input("enter the index which u want to delete"))
#     if 1<=index<=len(todo_list):
#          delete=todo_list.pop(index-1)
#          print(f"task{delete} deleted succesfully")    

add_task("book reading")
