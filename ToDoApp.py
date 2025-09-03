import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List by Shree Varada Vaidya")
        self.root.geometry("400x500")

        # Task list
        self.tasks = []

        # UI
        self.task_entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.listbox = tk.Listbox(root, width=50, height=20, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        self.done_button = tk.Button(root, text="Mark as Done", command=self.mark_done)
        self.done_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter a task!")

    def mark_done(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            task = self.tasks[index] + " ✅"
            self.tasks[index] = task
            self.listbox.delete(index)
            self.listbox.insert(index, task)
        else:
            messagebox.showwarning("Warning", "Select a task!")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.listbox.delete(index)
        else:
            messagebox.showwarning("Warning", "Select a task!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
