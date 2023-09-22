# Initialize an empty to-do list
todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks():
    if not todo_list:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def update_task(index, new_task):
    if 1 <= index <= len(todo_list):
        todo_list[index - 1] = new_task
        print(f"Task {index} updated successfully!")
    else:
        print("Invalid task index.")

def delete_task(index):
    if 1 <= index <= len(todo_list):
        deleted_task = todo_list.pop(index - 1)
        print(f"Task {index} ('{deleted_task}') deleted successfully!")
    else:
        print("Invalid task index.")

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        index = int(input("Enter the task index to update: "))
        new_task = input("Enter the updated task: ")
        update_task(index, new_task)
    elif choice == "4":
        index = int(input("Enter the task index to delete: "))
        delete_task(index)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")