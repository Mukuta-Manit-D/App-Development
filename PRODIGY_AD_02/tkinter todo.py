import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        # Dictionary to store tasks
        self.tasks = {}
        
        # Task List Display
        self.task_listbox = tk.Listbox(self.root, width=50, height=15, font=("Arial", 12))
        self.task_listbox.pack(pady=10)
        
        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        add_button = tk.Button(button_frame, text="Add Task", command=self.add_task, width=10)
        add_button.grid(row=0, column=0, padx=5)
        
        edit_button = tk.Button(button_frame, text="Edit Task", command=self.edit_task, width=10)
        edit_button.grid(row=0, column=1, padx=5)
        
        delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task, width=10)
        delete_button.grid(row=0, column=2, padx=5)
        
        view_button = tk.Button(button_frame, text="View Task", command=self.view_task, width=10)
        view_button.grid(row=0, column=3, padx=5)
    
    def add_task(self):
        task_description = simpledialog.askstring("Add Task", "Enter task description:")
        if task_description:
            task_id = len(self.tasks) + 1
            self.tasks[task_id] = task_description
            self.task_listbox.insert(tk.END, f"{task_id}. {task_description}")
    
    def edit_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task_index = selected_task[0]
            task_id = list(self.tasks.keys())[task_index]
            new_description = simpledialog.askstring("Edit Task", "Enter new task description:")
            if new_description:
                self.tasks[task_id] = new_description
                self.task_listbox.delete(task_index)
                self.task_listbox.insert(task_index, f"{task_id}. {new_description}")
        else:
            messagebox.showwarning("Edit Task", "Please select a task to edit.")
    
    def delete_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task_index = selected_task[0]
            task_id = list(self.tasks.keys())[task_index]
            del self.tasks[task_id]
            self.task_listbox.delete(task_index)
        else:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")
    
    def view_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task_index = selected_task[0]
            task_id = list(self.tasks.keys())[task_index]
            task_description = self.tasks[task_id]
            messagebox.showinfo("View Task", f"Task {task_id}: {task_description}")
        else:
            messagebox.showwarning("View Task", "Please select a task to view.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
