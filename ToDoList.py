# Simple To-Do List using functions

tasks = []

def show_menu():
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added.")

def view_tasks():
    if not tasks:
        print("No tasks added.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(str(i + 1) + ". " + tasks[i])

def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1] = tasks[num - 1] + "-Completed."
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        print("Exiting To-Do List. Bye!")
        break
    else:
        print("Invalid choice. Try again.")
