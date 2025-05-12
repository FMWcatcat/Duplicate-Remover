from tkinter import *
import tkinter as tk

root = tk.Tk()

path_var=tk.StringVar()

def select_folder():
    path = path_var.get()
    path_var.set("")

root.geometry("800x500")
root.title("Duplicate Remover")
button = tk.Button(root, text="Select input folder", width=15, command=root.destroy)



input_folder_label = tk.Label(root, text = "file_path", font=("calibri", 12))
input_folder_entry = tk.Entry(root,textvariable = path_var, font=("calibri", 12))

input_folder_label.grid(row=0,column=0)
input_folder_entry.grid(row=1,column=0)
button.grid(row=1,column=1)

root.mainloop()