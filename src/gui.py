from tkinter import filedialog
import tkinter as tk
from tkinter import *
import os
import platform
import subprocess

start_up_window = tk.Tk()

path_var=tk.StringVar()

def select_folder():
    path = path_var.get()
    path_var.set('')


dr_w_width = 600
dr_w_height = 150
pr_w_width = 1200
pr_w_height = 800

screen_width = start_up_window.winfo_screenwidth()
screen_height = start_up_window.winfo_screenheight()

x = (screen_width / 2) - (dr_w_width / 2)
y = (screen_height / 2) - (dr_w_height / 2)

start_up_window.geometry(f'{dr_w_width}x{dr_w_height}+{int(x)}+{int(y)}')
start_up_window.title('Duplicate Remover')


#def save_folder_path():
 #   for s in :
#get([end-1c])
def clear_text():
    input_folder_entry.delete(0, "end-1c")

def enter_path():
    filepath = input_folder_entry.get(0, "end-1c")
    with open("filepath.txt", "w") as f:
        f.write(text)

filepath = ""
filetypes = (".jpg", ".jpeg", ".jpe", ".png")
all_files = ""

def file_dialog():
    global filepath
    try:
        if platform.system() == "Windows":
            initial_dir = os.path.join(os.path.expanduser("~"), "Desktop")
        elif "microsoft" in platform.uname().release.lower():
            initial_dir = "/mnt/c/Users"
        else:
            initial_dir = os.path.expanduser("~")
    except Exception as e:
        print(f"Error finding initial directory: {e}")
        initial_dir = "/"

    filepath = filedialog.askdirectory(initialdir=initial_dir, title="Select a Folder")
    file_list()

    return filepath, start_up_window.destroy()


def file_list():
    global filepath, filetypes
    all_files = os.listdir(filepath)
    list_of_images = []
    
    for f in all_files:
        if f.endswith(filetypes):
            list_of_images.append(f)

    process_window = tk.Tk()

    screen_width = process_window.winfo_screenwidth()
    screen_height = process_window.winfo_screenheight()
    
    x = (screen_width / 2) - (pr_w_width / 2)
    y = (screen_height / 2) - (pr_w_height / 2)

    process_window.title(f"{filepath}")
    process_window.geometry(f'{pr_w_width}x{pr_w_height}+{int(x)}+{int(y)}')

    listbox = tk.Listbox(process_window, width=70)
        


#Initial window
input_folder_label = tk.Label(start_up_window, text = 'Select a folder to be processed', font=('calibri', 16))
#input_folder_intructions = tk.Label(root, text = 'Select a Folder.', font=('calibri', 12))
#input_folder_entry = tk.Entry(root, textvariable = path_var, width=40, font=('calibri', 12))
#input_folder_enter = tk.Button(root, text='Enter', width=10, command=enter_path)
#input_folder_clear = tk.Button(root, text='Clear', width=10, command=clear_text)
input_folder_select = tk.Button(start_up_window, text='Select a folder', width=10, command=file_dialog)
#command=root.destroy
input_folder_label.place(x=300, y=50, anchor=CENTER)
#input_folder_intructions.place(x=300, y=105, anchor=CENTER)
#input_folder_entry.place(x=300, y=80, anchor=CENTER)
#input_folder_enter.place(x=430, y=135, anchor=CENTER)
#input_folder_clear.place(x=170, y=135, anchor=CENTER)
input_folder_select.place(x=300, y=90, anchor=CENTER)








start_up_window.mainloop()