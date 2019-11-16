import mysql.connector
import tkinter as tk
import tkinter.ttk
from report import *

class Menu(object):
    def __init__(self, connection):
        self._bug = Bug(connection)
        #Setup menu
        self.root = tk.Tk()
        self.root.title("Bug Tracker")
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx = 50, pady = 50)
        #Create grid headings
        columns = ["ID", "Type", "Title", "Assigned to", "Priority", "Status", "Description"]
        self.tree = tkinter.ttk.Treeview(self.frame, columns = columns, show = "headings")
        self.tree.grid(in_=self.frame, row = 0, column = 0, columnspan = 5, sticky = tk.NSEW)
        for column in columns:
            self.tree.heading(column, text = column.title())
        self.menu_buttons()

    def menu_buttons(self):
        #Add bug report button
        add_button = tk.Button(self.frame, text = "Add Bug Report", command = None, width = 20)
        add_button.grid(in_= self.frame, row = 1, column = 0, sticky = tk.W)
        #Exit button
        exit_button = tk.Button(self.frame, text = "Exit", command = self.close, width = 20)
        exit_button.grid(in_= self.frame, row = 1, column = 4, sticky = tk.E)
        #Remove bug report button
        remove_button = tk.Button(self.frame, text = "Remove Bug Report", command = None, width = 20)
        remove_button.grid(in_= self.frame, row = 1, column = 2)
        self.list_bugs()
        self.root.mainloop()

    def list_bugs(self):
        #Populate and refresh data
        self.tree.delete(*self.tree.get_children())
        for bug in self._bug.list_bugs():
            values = (bug.id, bug.types, bug.title, bug.assigned_to, bug.priority, bug.status, bug.description)
            self.tree.insert("", "end", values = values)

    def add_bug(self):
        pass

    def edit_bug(self):
        pass

    def view_bug(self):
        pass

    def update_bug(self):
        pass

    def close(self):
        self.root.destroy()

class EditWindow(object):
    def __init__(self):
        pass

    def add_widgets(self):
        pass

    def save_bugs(self):
        pass

    def close(self):
        pass


if __name__ == '__main__':
    print('Connecting to database...')
    connection = mysql.connector.connect(user='root',
                                   database='bug_tracker',
                                   charset='utf8')
    print('Database connected')
    application = Menu(connection)
    application.start()
    conn.close()