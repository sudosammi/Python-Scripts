import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Mera Digital Clock")

def update_time():
    current_time = strftime('%H:%M:%S %p')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

clock_label = tk.Label(root, font=('calibri', 50, 'bold'), background='black', foreground='cyan')
clock_label.pack(anchor='center')

update_time()
root.mainloop()