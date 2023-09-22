#importing the tkinter module
import tkinter
import tkinter as tk
from tkcalendar import Calendar
import tkinter.messagebox


root = tkinter.Tk()
root.title("To-Do List")

#Function to add a tasks
def add_Task():
    task = entry_task.get()
    priority = priority_var.get()
    due_date = calendar.get_date()
    if task!= "" and priority and due_date:
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
        listbox_tasks.insert(tk.END, f"Priority: {priority}, Task: {task}, Due Date: {due_date}")
        entry_task.delete(0, tk.END)
        priority_var.set("")
        calendar.set_date("")
    else:
        tkinter.messagebox.showwarning(title="WARNING!", message="Please enter a task.") 

#Function to remove a tasks
def remove_Task():
        try:     
            task_index = listbox_tasks.curselection()[0]
            listbox_tasks.delete(task_index)
        except:
            tkinter.messagebox.showwarning(title="WARNING!", message="Please select a task.")    

#Function to mark the tasks
def mark_Task():
        try:
            task_index = listbox_tasks.curselection()[0]
            listbox_tasks.itemconfig(task_index, {'bg': 'green', 'fg': 'white'})
        except:
            tkinter.messagebox.showwarning(title="WARNING!", message="Please mark a task.")

#Function to save the tasks
def save_Task():
    with open("tasks.txt", "w") as file:
        tasks = listbox_tasks.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

#Function to  load the tasks
def load_Task():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox_tasks.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

#Creating a GUI tp view the list of tasks as well as enter the tasks
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=15, width=70)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

# Create a calendar widget for selecting due dates
calendar = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
calendar.pack()

# Create a radio button group for selecting priority
priority_var = tk.StringVar()
priority_label = tk.Label(root, text="Priority:")
priority_label.pack()
priority_high = tk.Radiobutton(root, text="High", variable=priority_var, value="High")
priority_medium = tk.Radiobutton(root, text="Medium", variable=priority_var, value="Medium")
priority_low = tk.Radiobutton(root, text="Low", variable=priority_var, value="Low")
priority_high.pack()
priority_medium.pack()
priority_low.pack()


button_add_task = tkinter.Button(root, text="ADD TASK", width=50, command = add_Task)
button_add_task.pack()

button_remove_task = tkinter.Button(root, text="REMOVE TASK", width=50, command = remove_Task)
button_remove_task.pack()

button_mark_task = tkinter.Button(root, text="MARK TASK", width=50, command = mark_Task)
button_mark_task.pack()

button_save_task = tkinter.Button(root, text="SAVE TASK", width=50, command = save_Task)
button_save_task.pack()

button_load_task = tkinter.Button(root, text="LOAD TASK", width=50, command = load_Task)
button_load_task.pack()

# Load tasks from the file at the start of the application
load_Task()

root.mainloop()