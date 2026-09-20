import json
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read tasks.json. Starting with an empty list.")
        return []


def save_tasks(tasks):
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    except OSError as error:
        print(f"Error saving tasks: {error}")


def display_tasks(tasks):
    print("\n========== MY TO-DO LIST ==========")

    if not tasks:
        print("No tasks found.")
        print("===================================\n")
        return

    for index, task in enumerate(tasks, start=1):
        status = "✓ Completed" if task["completed"] else "○ Pending"
        print(f"{index}. {task['task']} [{status}]")

    print("===================================\n")


def add_task(tasks):
    task_name = input("Enter a new task: ").strip()

    if not task_name:
        print("Task cannot be empty.")
        return

    tasks.append({
        "id": len(tasks) + 1,
        "task": task_name,
        "completed": False
    })

    save_tasks(tasks)
    print("Task added successfully.")


def mark_completed(tasks):
    if not tasks:
        print("No tasks available.")
        return

    display_tasks(tasks)

    try:
        task_number = int(input("Enter task number to mark completed: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    if not tasks:
        print("No tasks available.")
        return

    display_tasks(tasks)

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)

            # Rebuild IDs after deletion.
            for index, task in enumerate(tasks, start=1):
                task["id"] = index

            save_tasks(tasks)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    my_tasks = load_tasks()

    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        print("================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(my_tasks)
        elif choice == "2":
            display_tasks(my_tasks)
        elif choice == "3":
            mark_completed(my_tasks)
        elif choice == "4":
            delete_task(my_tasks)
        elif choice == "5":
            print("Thank you for using the To-Do List!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
