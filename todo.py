# todo.py

def display_tasks(tasks):
    """Display the current list of tasks."""
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def delete_task(tasks):
    """Delete a task from the list."""
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the to-do list application."""
    tasks = []
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()