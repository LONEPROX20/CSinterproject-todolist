import tkinter as tk
import time
from tkinter import messagebox

class ToDoList: 
    def __init__(self, root): 
        self.root = root
        self.root.title("To Do List") 
        self.root.geometry("700x700") 
        self.root.resizable(False, False)

        # frames buat tempelin buttons kebawah
        self.buttons_frame = tk.Frame(root, width=700)
        self.buttons_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        # buttons appearance dlu
        self.add_task_icon = tk.PhotoImage(file='add_task.png')
        self.add_task_button = tk.Button(root, image=self.add_task_icon, command=self.add_task)
        self.add_task_button.pack(pady=10)

        # self.remove_task_icon = tk.PhotoImage(file='remove_tasl.png')
        # self.remove_task_button = tk.Button(root, image=self.remove_task_icon,command=self.remove_task)
        # self.remove_task_button.pack(pady=15)

        self.start_timer_button = tk.Button(self.buttons_frame, text='start_timer', command=self.start_timer)
        self.start_timer_button.pack(side=tk.LEFT,padx=5)

        self.stop_timer_button = tk.Button(self.buttons_frame, text='stop_timer', command=self.stop_timer)
        self.stop_timer_button.pack(side=tk.LEFT, padx=10)

        self.task_list = []
        self.task_inputs = tk.Entry(root, width=50)
        self.task_inputs.pack(pady=10)

        self.task_listbox = tk.Listbox(root, width=55, height=20)
        self.task_listbox.pack(pady=10)

        self.timer_status = False
        self.timer = tk.Label(root, text="00:00", font=("Arial", 30))
        self.timer.pack(pady=10)

        

        
    def add_task(self):
        task = self.task_inputs.get()
        if task:
            self.task_list.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_inputs.delete(0, tk.END)
        

    def remove_task(self):
        pass

    def start_timer(self):
        if not self.timer_status:
            self.timer_status= True
            self.countdown(30*60)

    def stop_timer(self):
        self.timer_status= False

    def countdown(self, remaining):
        if self.timer_status:
            minutes, seconds = divmod(remaining, 60)
            time_format = '{:02d}:{:02d}'.format(minutes, seconds)
            self.timer.config(text=time_format)
            if remaining > 0:
                self.root.after(1000, self.countdown, remaining -1)
            else:
                self.timer_status = False
                messagebox.showinfo("Timer has elapsed. Hopefully your task is done")

if __name__ == "__main__": 
    root = tk.Tk()
    app = ToDoList(root)
    app.root.mainloop()