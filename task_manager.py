tasks = []

while True:
    print("\nStudent Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

            number = int(input("Enter task number to delete: "))
            tasks.pop(number - 1)
            print("Task deleted successfully.")

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
