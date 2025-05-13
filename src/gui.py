from tkinter import *
import tkinter as tk

root = tk.Tk()

path_var=tk.StringVar()

def select_folder():
    path = path_var.get()
    path_var.set('')


dr_w_width = 800
dr_w_height = 500

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
    input_folder_entry.delete(0, "end")

def enter_path():
    input_folder_entry.

input_folder_label = tk.Label(root, text = 'file_path', font=('calibri', 16))
input_folder_intructions = tk.Label(root, text = 'Insert target folder filepath.', font=('calibri', 12))
input_folder_entry = tk.Entry(root, textvariable = path_var, width=40, font=('calibri', 12))
input_folder_enter = tk.Button(root, text='Enter', width=15, command=enter_path)
input_folder_clear = tk.Button(root, text='Clear', width=15, command=clear_text)
#command=root.destroy
input_folder_label.place(x=400, y=100, anchor=CENTER)
input_folder_intructions.place(x=400, y=190, anchor=CENTER)
input_folder_entry.place(x=400, y=130, anchor=CENTER)
input_folder_enter.place(x=500, y=160, anchor=CENTER)
input_folder_clear.place(x=300, y=160, anchor=CENTER)




root.mainloop()