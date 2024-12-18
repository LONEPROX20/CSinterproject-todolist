import tkinter as tk



class ToDoList: 
    def __init__(self, root): 
        self.root = root
        self.root.title("To Do List") 
        self.root.geometry("700x700") 
        self.root.resizable(False, False)

        # frames buat tempelin buttons kebawah
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=15)

        # buttons appearance dlu
        self.add_task_icon = tk.PhotoImage(file='add_task.png')
        self.add_task_button = tk.Button(root, image=self.add_task_icon, command=self.add_task)
        self.add_task_button.pack(pady=55)

        self.remove_task_icon = tk.PhotoImage(file='remove_tasl.png')
        self.remove_task_button = tk.Button(root, image=self.remove_task_icon,command=self.remove_task)
        self.remove_task_button.pack(pady=15)

        self.start_timer_button = tk.Button(self.buttons_frame, text='start_timer', command=self.start_timer)
        self.start_timer_button.pack(pady=15)

        self.stop_timer_button = tk.Button(self.buttons_frame, text='stop_timer', command=self.stop_timer)
        self.stop_timer_button.pack(pady=15)

        self_task_list = []
        self.task_inputs = tk.Entry(root, width=50)
        self.task_inputs.pack(pady=15)

        self.task_listbox = tk.Listbox(root, width=55, height=20)
        self.task_listbox.pack(pady=40)

        self.timer_status = False
        self.timer = tk.Label(root, text="00:00", font=("Arial", 30))
        self.timer.pack(pady=15)

        

        
    def add_task(self):
        pass

    def remove_task(self):
        pass

    def start_timer(self):
        pass

    def stop_timer(self):
        pass

if __name__ == "__main__": 
    root = tk.Tk()
    app = ToDoList(root)
    app.root.mainloop()