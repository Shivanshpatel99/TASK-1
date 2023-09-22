# TASK-1
To-Do List Application
This is a simple to-do list application created in Python using the tkinter library. It allows users to manage tasks, set task priorities, and specify due dates for tasks. Tasks and their associated information (priority and due date) are stored in a text file for data persistence across sessions.

Features
Add tasks with priority and due date
Remove selected tasks
Store tasks in a text file for data persistence
Load tasks from the text file when the application starts
Requirements
Python 3.x
tkinter library (for GUI)
tkcalendar library (for date picker)
Installation
Install the required libraries:

Copy code

pip install tkcalendar

Download or clone the repository to your local machine.

Run the to_do_list.py file to start the application:

Copy code

python todolist.py

How to Use
Enter a task in the input field.

Select a priority level (High, Medium, Low) using the radio buttons.

Choose a due date using the date picker.

Click the "Add Task" button to add the task to the list.

To remove a task, select it in the list and click the "Remove Task" button.

Tasks are saved automatically and loaded when you reopen the application.

Data Persistence
Tasks and their associated information are saved in a file named tasks.txt in the same directory as the application. This allows tasks to be persisted across sessions, ensuring that you don't lose your to-do list when you close the application.

Contributing
If you'd like to contribute to this project or have suggestions for improvements, please feel free to open an issue or submit a pull request.

Acknowledgments
Special thanks to the tkinter and tkcalendar libraries for providing the tools to create the GUI and date picker components.
Happy task management! 📝📅
