tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully!\n")

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

def remove_task():
    view_tasks()
    if not tasks:
        return
    task_no = int(input("Enter task number to remove: "))
    if 1 <= task_no <= len(tasks):
        removed = tasks.pop(task_no - 1)
        print(f"Removed task: {removed}\n")
    else:
        print("Invalid task number.\n")

while True:
    print("---- TO-DO LIST ----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
