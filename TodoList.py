class TodoList:
    def __init__(self):
        self.todos = []

    def add_todo(self, todo):
        self.todos.append({"task": todo, "completed": False})

    def delete_todo(self, index):
        if 0 <= index < len(self.todos):
            del self.todos[index]
            print("Todo deleted successfully!")
        else:
            print("Invalid todo index.")

    def complete_todo(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index]["completed"] = True
            print("Todo marked as completed.")
        else:
            print("Invalid todo index.")

    def show_remaining_todos(self):
        print("Remaining Todos:")
        for index, todo in enumerate(self.todos):
            if not todo["completed"]:
                print(f"{index + 1}. {todo['task']}")
        print()

    def show_statistics(self):
        total_todos = len(self.todos)
        completed_todos = sum(1 for todo in self.todos if todo["completed"])
        remaining_todos = total_todos - completed_todos
        print("----- Todo List Statistics -----")
        print(f"Total Todos: {total_todos}")
        print(f"Completed Todos: {completed_todos}")
        print(f"Remaining Todos: {remaining_todos}")
        print("---------------------------------")


def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Todo")
        print("2. Delete Todo")
        print("3. Complete Todo")
        print("4. Show Remaining Todos")
        print("5. Show Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            todo = input("Enter todo: ")
            todo_list.add_todo(todo)
        elif choice == "2":
            index = int(input("Enter todo index to delete: ")) - 1
            todo_list.delete_todo(index)
        elif choice == "3":
            index = int(input("Enter todo index to mark as completed: ")) - 1
            todo_list.complete_todo(index)
        elif choice == "4":
            todo_list.show_remaining_todos()
        elif choice == "5":
            todo_list.show_statistics()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
