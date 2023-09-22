# Initialize an empty to-do list with completion status
todo_list = []

def add_task(task): 
    task = input("Enter a task to add: ")
    todo_list.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    if todo_list:
        print("To-Do List:")
        for index, task in enumerate(todo_list):
            status = "Completed" if task["completed"] else "Incomplete"
            print(f"{index + 1}. {task['task']} - Status: {status}")
    else:
        print("To-Do list is empty!")

def update_task():

    view_tasks()
    task_number = int(input("Enter the number of the task to update: ")) - 1

    if 0 <= task_number < len(todo_list):
        new_task = input("Enter the updated task: ")
        todo_list[task_number]["task"] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task number.")


def mark_task_completed():
    view_tasks()
    task_number = int(input("Enter the number of the task to mark as completed: ")) - 1

    if 0 <= task_number < len(todo_list):
        todo_list[task_number]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_number = int(input("Enter the number of the task to delete: ")) - 1

    if 0 <= task_number < len(todo_list):
        deleted_task = todo_list.pop(task_number)
        print(f"Task '{deleted_task['task']}' deleted successfully!")
    else:
        print("Invalid task number.")




while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Quit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        mark_task_completed()
    elif choice == '5':
        delete_task()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please select a valid option.")