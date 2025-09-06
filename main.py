# To- Do list console app


# The main menu 
def show_menu():
    print("\n ===== TO-DO Lists App")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as done")
    print("4. Delete Task")
    print("5. Exit")

# Viewing Task
def view_tasks(tasks):
    if not tasks:
        print("\n No tasks available!")
    else:
        print("\n Your Tasks: ")
        for i, task in enumerate(tasks, start=1):
            status = "✅ Done" if task['done'] else "❌ Not Done"
            print(f"{i}.{task['title']}[{status}]")

# Adding a task
def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("Tasks added!")

# Marking a task as done
def mark_task_done(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to mark as done: "))
            tasks[task_num-1]["done"] = True
            print("Task marked as done")
        except(ValueError, IndexError):
            print("Invalid task number")

# Deleting a Task
def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: "))
            tasks.pop(task_num-1)
            print("Task Deleted")
        except(ValueError, IndexError):
            print("Invalid task number!")

# The main loop (app's engine)
def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print ("Exiting..... GoodBye!")
            break
        else:
            print("Invalid choice ! Please try again")

# Program entry point
if __name__== "__main__":
    main()





















