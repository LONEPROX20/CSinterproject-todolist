import tkinter as tk

class ToDoList: 
    def __init__(self, root): 
        self.root = root
        self.root.title("To Do List") 
        self.root.geometry("700x700") 
        self.root.resizable(False, False)





if __name__ == "__main__": 
    root = tk.Tk()
    app = ToDoList(root)
    app.root.mainloop()