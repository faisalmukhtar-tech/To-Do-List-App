''' Simple To-Do List App '''

tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            i = 0
            while i < len(tasks):
                print(i + 1, "-", tasks[i])
                i += 1

    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            i = 0
            while i < len(tasks):
                print(i + 1, "-", tasks[i])
                i += 1

            task_number = int(input("Enter task number to delete: "))

            if task_number >= 1 and task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print(deleted_task, "deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")