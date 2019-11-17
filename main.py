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
        self.tree.bind("<Double-1>", self.edit_bug)
        self.menu_buttons()
        self.list_bugs()
        self.root.mainloop()

    def menu_buttons(self):
        #Add bug report buttons
        add_button = tk.Button(self.frame, text = "Add Bug Report", command = self.add_bug, width = 20)
        add_button.grid(in_= self.frame, row = 1, column = 0, sticky = tk.W)
        #Exit button
        exit_button = tk.Button(self.frame, text = "Exit", command = self.close, width = 20)
        exit_button.grid(in_= self.frame, row = 1, column = 4, sticky = tk.E)
        #Remove bug report button
        remove_button = tk.Button(self.frame, text = "Remove Bug Report", command = None, width = 20)
        remove_button.grid(in_= self.frame, row = 1, column = 2)

    def list_bugs(self):
        #Populate and refresh data
        self.tree.delete(*self.tree.get_children())
        for bug in self._bug.list_bugs():
            values = (bug.id, bug.types, bug.title, bug.assigned_to, bug.priority, bug.status, bug.description)
            self.tree.insert("", "end", values = values)

    def add_bug(self):
        bug = Data("","","","","","","")
        self.view_bug(bug, self._save_bug)

    def _save_bug(self, bug):
        self._bug.add(bug)
        self.list_bugs()

    def edit_bug(self, event):
        item = self.tree.item(self.tree.focus())
        item_id = item["values"][0]
        item_bug_type = item["values"][1]
        item_title = item["values"][2]
        item_assigned_to = item["values"][3]
        item_priority = item["values"][4]
        item_bug_status = item["values"][5]
        item_description = item["values"][6]
        bug = Data(item_id, item_bug_type, item_title, item_assigned_to, item_priority, item_bug_status, item_description)
        self.view_bug(bug, self._update_bug)

    def _update_bug(self, bug):
        self._bug.update(bug)
        self.list_bugs()

    def view_bug(self, bug, action):
        window = EditWindow(self, bug, action)
        self.root.wait_window(window.root)

    def close(self):
        self.root.destroy()

class EditWindow(object):
    def __init__(self, parent, bug, saveAction):
        self._parent = parent.root
        self.root = tk.Toplevel(parent.root)
        self.root.title("Bug report")
        self.root.transient(parent.root)
        self.root.grab_set()
        self.saveAction = saveAction
        self._bug = bug

        self.frame = tk.Frame(self.root)
        self.frame.pack(side = tk.TOP, fill = tk.BOTH, expand = tk.Y, padx= 10, pady = 10)

        last_row = self.add_widgets(bug)
        self._save_button = tk.Button(self.frame, text = "Save", command = self.save_bugs, width = 20, padx = 5, pady = 5)
        self._save_button.grid(in_ = self.frame, row = last_row + 7, column = 1, sticky = tk.E)

        exit_button = tk.Button(self.frame, text = "Close", command = self.close, width = 20, padx = 5, pady = 5)
        exit_button.grid(in_ = self.frame, row = last_row + 8, column = 1, sticky = tk.E)
    
    def close(self):
        self.root.destroy()

    def add_widgets(self, bug):
        #Assign Labels
        bug_type = tk.Label(self.frame, text = "Type:", width = 10, padx = 10, pady = 10)
        bug_type.grid(in_= self.frame, row = 0, column = 0, sticky = tk.E)

        title = tk.Label(self.frame, text = "Title:", width = 10, padx = 10, pady = 10)
        title.grid(in_ = self.frame, row = 1, column = 0, sticky = tk.E)

        assigned_to = tk.Label(self.frame, text = "Assigned to:", width  = 10 , padx = 10, pady = 10)
        assigned_to.grid(in_ = self.frame, row = 2, column = 0, sticky = tk.E)

        priority = tk.Label(self.frame, text = "Priority:", width = 10, padx = 10, pady = 10)
        priority.grid(in_ = self.frame, row = 3, column = 0, sticky = tk.E)

        bug_status = tk.Label(self.frame, text = "Status:", width = 10, padx = 10, pady= 10)
        bug_status.grid(in_ = self.frame, row = 4, column = 0, sticky = tk.E)

        description = tk.Label(self.frame, text = "Description:", width = 10, padx = 10, pady = 10)
        description.grid(in_ = self.frame, row = 5, column = 0, sticky = tk.E)
        

        #Assign components
        self.tkvar1 = tk.StringVar()
        choices = {"Defect", "Enchancement", "Task"}
        if self._bug.types == "Defect":
            self.tkvar1.set("Defect")
        elif self._bug.types == "Enchancement":
            self.tkvar1.set("Enchancement")
        elif self._bug.types == "Task":
            self._tkvar1.set("Task")
        else:
            self.tkvar1.set("<Select an option>")
        self.type_option = tk.OptionMenu(self.frame, self.tkvar1, *choices)
        self.type_option.grid(in_ = self.frame, row = 0, column = 1, sticky = tk.W)

        self.title_entry = tk.Entry(self.frame, width = 30)
        self.title_entry.grid(in_ = self.frame, row = 1, column = 1, sticky = tk.W)
        if self._bug.title != "":
            self.title_entry.insert(tk.END, self._bug.title)
    

        self.assigned_to_entry = tk.Entry(self.frame, width = 30)
        self.assigned_to_entry.grid(in_ = self.frame, row = 2, column = 1, sticky = tk.W)
        if self._bug.assigned_to != "":
            self.assigned_to_entry.insert(tk.END, self._bug.assigned_to)

        self.tkvar2 = tk.StringVar()
        selection = {"Low", "Medium", "High"}
        if self._bug.priority == "Low":
            self.tkvar2.set("Low")
        elif self._bug.priority == "Medium":
            self.tkvar2.set("Medium")
        elif self._bug.priority == "High":
            self.tkvar2.set("High")
        else:
            self.tkvar2.set("<Select an option>")
        self.priority_option = tk.OptionMenu(self.frame, self.tkvar2, *selection)
        self.priority_option.grid(in_ = self.frame, row = 3, column = 1, sticky = tk.W)

        self.tkvar3 = tk.StringVar()
        options = {"New", "Assigned", "Closed", "Reopened", "Fixed", "Invalid", "Duplicate", "Won't fix"}
        if self._bug.status == "New":
            self.tkvar3.set("New")
        elif self._bug.status == "Assigned":
            self.tkvar3.set("Assigned")
        elif self._bug.status == "Closed":
            self.tkvar3.set("Closed")
        elif self._bug.status == "Reopened":
            self.tkvar3.set("Reopened")
        elif self._bug.status == "Fixed":
            self.tkvar3.set("Fixed")
        elif self._bug.status == "Invalid":
            self.tkvar3.set("Invalid")
        elif self._bug.status == "Duplicate":
            self.tkvar3.set("Duplicate")
        elif self._bug.status == "Won't fix":
            self.tkvar3.set("Won't fix")
        else:
            self.tkvar3.set("<Select an option>")
        self.bug_status_option = tk.OptionMenu(self.frame, self.tkvar3, *options)
        self.bug_status_option.grid(in_ = self.frame, row = 4, column = 1, sticky = tk.W)

        self.description_text = tk.Text(self.frame, width = 30, height = 5)
        self.description_text.grid(in_ = self.frame, row = 5, column = 1, sticky = tk.W)
        if self._bug.description != "":
            self.description_text.insert(tk.END, self._bug.description)
        return -1

    def save_bugs(self):
        self._bug.types = self.tkvar1.get()

        if self.title_entry.get() != "":
            self._bug.title = self.title_entry.get()
        else:
            self._bug.title = "<None>"

        if self.assigned_to_entry.get() != "":
            self._bug.assigned_to = self.assigned_to_entry.get()
        else:
            self._bug.assigned_to = "<None>"

        self._bug.priority = self.tkvar2.get()
        self._bug.status = self.tkvar3.get()

        if self.description_text.get("1.0", "end-1c") != "":
            self._bug.description = self.description_text.get("1.0", "end-1c")
        else:
            self._bug.description = "<No Description>"

        self.saveAction(self._bug)
        self.close()

if __name__ == '__main__':
    print("Intialising application")
    connection = mysql.connector.connect(user='root', database='bug_tracker', charset='utf8')
    print("Application connected")
    Menu(connection)
    connection.close()


