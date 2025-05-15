from tkinter import filedialog
import tkinter as tk
from tkinter import *
import os

root = tk.Tk()

path_var=tk.StringVar()

def select_folder():
    path = path_var.get()
    path_var.set('')


dr_w_width = 600
dr_w_height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (dr_w_width / 2)
y = (screen_height / 2) - (dr_w_height / 2)

root.geometry(f'{dr_w_width}x{dr_w_height}+{int(x)}+{int(y)}')
root.title('Duplicate Remover')


#def save_folder_path():
 #   for s in :
#get([end-1c])
def clear_text():
    input_folder_entry.delete(0, "end-1c")

def enter_path():
    filepath = input_folder_entry.get(0, "end-1c")
    with open("filepath.txt", "w") as f:
        f.write(text)

def file_dialog():
    filepath = filedialog.askdirectory(initialdir, title="Select a Folder")



input_folder_label = tk.Label(root, text = 'file_path', font=('calibri', 16))
input_folder_intructions = tk.Label(root, text = 'Insert target folder filepath.', font=('calibri', 12))
input_folder_entry = tk.Entry(root, textvariable = path_var, width=40, font=('calibri', 12))
input_folder_enter = tk.Button(root, text='Enter', width=10, command=enter_path)
input_folder_clear = tk.Button(root, text='Clear', width=10, command=clear_text)
input_folder_select = tk.Button(root, text='Select Folder', width=10, command=file_dialog)
#command=root.destroy
input_folder_label.place(x=300, y=50, anchor=CENTER)
input_folder_intructions.place(x=300, y=105, anchor=CENTER)
input_folder_entry.place(x=300, y=80, anchor=CENTER)
input_folder_enter.place(x=430, y=135, anchor=CENTER)
input_folder_clear.place(x=170, y=135, anchor=CENTER)
input_folder_select.place(x=300, y=135, anchor=CENTER)





root.mainloop()