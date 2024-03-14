from datetime import datetime

# Function to add a task
def add_task(tasks, task, priority, due_date):
    tasks.append({'task': task, 'priority': priority, 'due_date': due_date, 'completed': False})

# Function to remove a task
def remove_task(tasks, index):
    del tasks[index]

# Function to mark a task as completed
def mark_completed(tasks, index):
    tasks[index]['completed'] = True

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{i}. {task['task']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {status}")

def main():
    tasks = []

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            priority = input("Enter priority (high/medium/low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, task, priority, due_date)
            print("Task added successfully.")

        elif choice == '2':
            display_tasks(tasks)
            index = int(input("Enter the index of the task to remove: ")) - 1
            remove_task(tasks, index)
            print("Task removed successfully.")

        elif choice == '3':
            display_tasks(tasks)
            index = int(input("Enter the index of the task to mark as completed: ")) - 1
            mark_completed(tasks, index)
            print("Task marked as completed.")

        elif choice == '4':
            display_tasks(tasks)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()