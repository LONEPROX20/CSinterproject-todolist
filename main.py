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
        self.add_task_button.pack(padx=100,pady=100)

        self.remove_task_icon = tk.PhotoImage(file='remove_tasl.png')
        self.remove_task_button = tk.Button(root, image=self.remove_task_icon,command=self.remove_task)
        self.remove_task_button.pack(padx=100, pady=10)

    def add_task(self):
        pass

    def remove_task(self):
        pass


if __name__ == "__main__": 
    root = tk.Tk()
    app = ToDoList(root)
    app.root.mainloop()