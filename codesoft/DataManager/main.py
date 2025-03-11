from todo import ToDoList

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Complete task")
        print("5. Delete task")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            todo_list.view_tasks()
        elif choice == "2":
            task = input("Enter a new task: ")
            todo_list.add_task(task)
        elif choice == "3":
            todo_list.view_tasks()
            task_index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_index, new_task)
        elif choice == "4":
            todo_list.view_tasks()
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            todo_list.complete_task(task_index)
        elif choice == "5":
            todo_list.view_tasks()
            task_index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
