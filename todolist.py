import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create an entry widget for entering tasks
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)

# Create a button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task, font=("Arial", 12))
add_button.pack()

# Create a listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, font=("Arial", 12))
listbox.pack()

# Create a button to remove tasks
remove_button = tk.Button(root, text="Remove Selected Task", command=remove_task, font=("Arial", 12))
remove_button.pack()

root.mainloop()
