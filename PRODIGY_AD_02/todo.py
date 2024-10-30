class ToDoList:
    def __init__(self):
        self.tasks = {}  # Dictionary to store tasks with IDs
    
    def add_task(self, task_description):
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = task_description
        print(f"Task added with ID {task_id}: '{task_description}'")
    
    def edit_task(self, task_id, new_description):
        if task_id in self.tasks:
            self.tasks[task_id] = new_description
            print(f"Task {task_id} updated to: '{new_description}'")
        else:
            print("Task ID not found.")
    
    def delete_task(self, task_id):
        if task_id in self.tasks:
            deleted_task = self.tasks.pop(task_id)
            print(f"Task '{deleted_task}' deleted.")
        else:
            print("Task ID not found.")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Current To-Do List:")
            for task_id, description in self.tasks.items():
                print(f"{task_id}. {description}")
    

# Main program
if __name__ == "__main__":
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List App:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            task_description = input("Enter task description: ")
            todo_list.add_task(task_description)
        
        elif choice == '2':
            task_id = int(input("Enter task ID to edit: "))
            new_description = input("Enter new task description: ")
            todo_list.edit_task(task_id, new_description)
        
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
        
        elif choice == '4':
            todo_list.view_tasks()
        
        elif choice == '5':
            print("Exiting the To-Do List App. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")
