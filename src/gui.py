from tkinter import filedialog
import tkinter as tk
from tkinter import *
import os
import platform
import subprocess
from PIL import Image, ImageTk



path_var=tk.StringVar()

class ImageGallery:
    def __init__(self):
        self.start_up_window = start_up_window
        self.filepath = ""
        self.filetypes = (".jpg", ".jpeg", ".jpe", ".png")
        self.all_files = ""

        self.row_height = 120
        self.buffer = 10

        self.setup_ui()
        self.list_of_images = []
        self.image_frames = {}

dr_w_width = 600
dr_w_height = 150
pr_w_width = 1200
pr_w_height = 800

screen_width = start_up_window.winfo_screenwidth()
screen_height = start_up_window.winfo_screenheight()

x = (screen_width / 2) - (dr_w_width / 2)
y = (screen_height / 2) - (dr_w_height / 2)

def setup_ui(self):
    self.select_dir_btn = tk.Button(self.root, text="select Directory", command=self.select_directory)
    self.select_dir_btn.pakc(pady=10)

    self.main_frame = tk.Frame(self.start_up_window)
    self.main_frame.pack(fill=tk.BOTH, expand=1)

    self.canvas = tk.Canvas(self.main_frame)
    self.canvas.pack(fill=tk.LEFT, fill=tk.BOTH, expand=1)

    self.scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
    self.scrollbar.pack(side=tk.RIGHT, fil=tk.Y)

    self.canvas.configure(yscrollcommand=self.scrollbar.set)
    
    self.scroll_frame = tk.Frame(self.canvas)
    self.canvas_window = self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
    
    self.canvas.bind('<configure>', self.on_canvas_configure)
    self.scroll_frame.bind('<configure>', self.on_frame_configure)

    self.root.bind_all()
    self.root.bind_all("<Button-4>", lambda e:self.canvas.yview_scroll(1, "units"))
    self.root.bind_all("<Button-5>")
    


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

    main_frame = tk.Frame(process_window)
    main_frame.pack(fill=tk.BOTH, expand=1)

    canvas = tk.Canvas(main_frame)
    canvas.pack(side=tk.RIGHT, fill=tk.Y)
    
    scrollbar = tk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scrollbar.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    scroll_frame =  tk.Frame(canvas)
    canvas.create_window((0,0), window= scroll_frame, anchor="nw")

    for idx, image_name in enumerate(list_of_images):
        image_frame = tk.Frame(scroll_frame, borderwidth=2, relief="ridge", padx=5, pady=5)
        image_frame.grid(row=idx, column=0, sticky="ew", padx=10, pady=5)

        try:
            img_path = os.path.join(filepath, image_name)
            pil_img = Image.open(img_path)
            pil_img = pil_img.resize((100,100), Image.LANCZOS)

            tk_img = ImageTk.PhotoImage(pil_img)

            image_frame.image = tk_img

            img_label = tk.label(image_frame, image=tk_img)
            img_label.pack(side=tk.LEFT, padx=5)

            name_label = tk.label(image_frame, text=image_name, wraplenght=300, anchor="W")
            name_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

            select_btn = tk.Button(image_frame, text="Select", command=lambda img=image_name: process_image(img))
            select_btn.pack(side=tk.RIGHT, padx=5)

        except Exception as e:
            error_label = tk.Label(image_frame, text=f"Error loading {image_name}: {str(e)}")         
            error_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)




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







if __name__ == "__main__":
    start_up_window = tk.Tk()
    start_up_window.geometry(f'{dr_w_width}x{dr_w_height}+{int(x)}+{int(y)}')
    start_up_window.title('Duplicate Remover')

    gallery = ImageGallery(start_up_window)

    start_up_window.mainloop()