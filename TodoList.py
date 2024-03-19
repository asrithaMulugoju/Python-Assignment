tasks = []

while True:
    print("\n1. Add Task")
    print("2. Delete Task")
    print("3. Mark Task as Completed")
    print("4. Display Tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "completed": False})
    elif choice == "2":
        index = int(input("Enter task index to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            print("Task deleted successfully!")
        else:
            print("Invalid task index.")
    elif choice == "3":
        index = int(input("Enter task index to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")
    elif choice == "4":
        print("----- TO-DO LIST -----")
        for index, task in enumerate(tasks):
            status = "✔" if task["completed"] else " "
            print(f"{index + 1}. [{status}] {task['task']}")
        print("----------------------")
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
