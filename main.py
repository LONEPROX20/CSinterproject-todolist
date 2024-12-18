import tkinter as tk



class ToDoList: 
    def __init__(self, root): 
        self.root = root
        self.root.title("To Do List") 
        self.root.geometry("700x700") 
        self.root.resizable(False, False)

        # buttons appearance dlu
        self.add_task_icon = tk.PhotoImage(file='add_task.png')
        self.add_task_button = tk.Button(root, image=self.add_task_icon, command=self.add_task)
        self.add_task_button.pack(pady=55)

        self.remove_task_icon = tk.PhotoImage(file='remove_tasl.png')
        self.remove_task_button = tk.Button(root, image=self.remove_task_icon,command=self.remove_task)
        self.remove_task_button.pack(pady=15)

        self_task_list = []
        self.task_inputs = tk.Entry(root, width=50)
        self.task_inputs.pack(pady=15)

        self.task_listbox = tk.Listbox(root, width=55, height=20)
        self.task_listbox.pack(pady=40)

    def add_task(self):
        pass

    def remove_task(self):
        pass


if __name__ == "__main__": 
    root = tk.Tk()
    app = ToDoList(root)
    app.root.mainloop()