from tkinter import *
import tkinter as tk

root = tk.Tk()

path_var=tk.StringVar()

def select_folder():
    path = path_var.get()
    path_var.set('')


#--     --      --      --      --
dr_sw_width = 800
dr_sw_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (dr_sw_width / 2)
y = (screen_height / 2) - (dr_sw_height / 2)

root.geometry(f'{dr_sw_width}x{dr_sw_height}+{int(x)}+{int(y)}')
root.title('Duplicate Remover')
#--     --      --      --      --


#def save_folder_path():
 #   for s in :


input_folder_label = tk.Label(root, text = 'file_path', font=('calibri', 16))
input_folder_intructions = tk.Label(root, text = 'Insert target folder filepath for it to be processed.', font=('calibri', 12))
input_folder_entry = tk.Entry(root, textvariable = path_var, font=('calibri', 12))
input_folder = tk.Button(root, text='Select folder path', width=15, command=root.destroy)

input_folder_label.place(x=400, y=100, anchor=CENTER)
input_folder_intructions.place(x=400, y=190, anchor=CENTER)
input_folder_entry.place(x=400, y=130, anchor=CENTER)
input_folder.place(x=400, y=160, anchor=CENTER)

root.mainloop()