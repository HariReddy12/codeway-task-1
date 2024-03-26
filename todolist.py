class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_index):
        del self.tasks[task_index]

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list!")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

def main():
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added successfully!")
        elif choice == '2':
            todo_list.display_tasks()
            task_index = int(input("Enter the index of the task to remove: ")) - 1
            if 0 <= task_index < len(todo_list.tasks):
                todo_list.remove_task(task_index)
                print("Task removed successfully!")
            else:
                print("Invalid task index!")
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()