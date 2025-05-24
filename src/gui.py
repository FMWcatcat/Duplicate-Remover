from tkinter import filedialog, messagebox
import tkinter as tk
from tkinter import *
import os
import platform
import subprocess
from PIL import Image, ImageTk, ImageFilter




class ImageGallery:
    def __init__(self, master):
        self.path_var=tk.StringVar()

        self.root = master
        self.filepath = ""
        self.filetypes = (".jpg", ".jpeg", ".jpe", ".png")
        self.all_files = ""

        self.row_height = 120
        self.buffer = 10
        self.dr_w_width = 600
        self.dr_w_height = 150
        self.pr_w_width = 1200
        self.pr_w_height = 800

        self.center_window(self.root, self.dr_w_width, self.dr_w_height)
        self.setup_ui()

        self.list_of_images = []
        self.image_frames = {}

        self.loaded_images = set()

        
        
    def setup_ui(self):
        self.select_dir_btn = tk.Button(self.root, text="select Directory", command=self.dir_dialog)
        self.select_dir_btn.pack(pady=10)

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        self.canvas = tk.Canvas(self.main_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        self.scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
    
        self.scroll_frame = tk.Frame(self.canvas)
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
    
        self.canvas.bind('<configure>', self.on_canvas_configure)
        self.scroll_frame.bind('<configure>', self.on_frame_configure)

        self.root.bind_all("<MouseWheel>", self.on_mousewheel)
        self.root.bind_all("<Button-4>", lambda e: self.canvas.yview_scroll(-1, "units"))
        self.root.bind_all("<Button-5>", lambda e: self.canvas.yview_scroll(1, "units"))

        self.canvas.bind("<Configure>", self.load_visible_images)   
        self.canvas.bind("<MouseWheel>", self.load_visible_images)   
        self.canvas.bind("<ButtonRelease-1>", self.load_visible_images)   


    def dir_dialog(self):
  
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

        self.filepath = filedialog.askdirectory(initialdir=initial_dir, title="Select a Folder")

        if self.filepath:
            self.load_image_data()
            self.create_image_frames()
            self.load_visible_images()


    def center_window(self, window, width, height):

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width / 2) - (self.dr_w_width / 2)
        y = (screen_height / 2) - (self.dr_w_height / 2)

        window.geometry(f'{self.dr_w_width}x{self.dr_w_height}+{int(x)}+{int(y)}')


    def load_image_data(self):
        self.list_of_images = []
        all_files = os.listdir(self.filepath)

        for f in all_files:
            if f.endswith(self.filetypes):
                self.list_of_images.append(f)


    def create_process_window(self):
        self.process_window = tk.Toplevel(self.root)
        
        screen_width = self.process_window.winfo_screenwidth()
        screen_height = self.process_window.winfo_screenheight()
        x = (screen_width / 2) - (self.pr_w_width / 2)
        y = (screen_height / 2) - (self.pr_w_height / 2)

        self.process_window.title(f"{self.filepath}")
        self.process_window.geometry(f'{self.pr_w_width}x{self.pr_w_height}+{int(x)}+{int(y)}')

        self.setup_scrollable_frame()


    def setup_scrollable_frame(self):

        main_frame = tk.Frame(self.process_window)
        main_frame.pack(fill=tk.BOTH, expand=1)

        canvas = tk.Canvas(main_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        
        scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.scroll_frame = tk.Frame(canvas)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self.display_images()


    def display_images(self):
        for idx, image_name in enumerate(self.list_of_images):
            image_frame = tk.Frame(self.scroll_frame, borderwidth=2, relief="ridge", padx=5, pady=5)
            image_frame.grid(row=idx, column=0, sticky="ew", padx=10, pady=5)

            try:
                img_path = os.path.join(self.filepath, image_name)
                pil_img = Image.open(img_path)
                pil_img = pil_img.resize((100,100), Image.LANCZOS)

                tk_img = ImageTk.PhotoImage(pil_img)

                image_frame.image = tk_img

                img_label = tk.Label(image_frame, image=tk_img)
                img_label.pack(side=tk.LEFT, padx=5)

                name_label = tk.Label(image_frame, text=image_name, wraplenght=300, anchor="W")
                name_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

                select_btn = tk.Button(image_frame, text="Select", command=lambda img=image_name: self.process_image(img))
                select_btn.pack(side=tk.RIGHT, padx=5)

            except Exception as e:
                error_label = tk.Label(image_frame, text=f"Error loading {image_name}: {str(e)}")         
                error_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")


    def load_visible_images(self, *args):
        visible_top = self.canvas.yview()[0]
        visible_bottom = self.canvas.yview()[1]

        canvas_height = self.canvas.winfo_height()

        total_height = self.scroll_frame.winfo_height()
        if total_height == 0:
            return 
        
        start_idx = int(visible_top * len(self.list_of_images))
        end_idx = int(visible_bottom * len(self.list_of_images)) + 1

        for idx in range(max(0,start_idx-5), min(len(self.list_of_images), end_idx+5)):
            if idx not in self.load_image(idx):
                self.load_image(idx)
                self.loaded_images.add(idx)


    def sample_image_colors(self, image):
        width, height = image.size
      
        image = image.filter(ImageFilter.GaussianBlur(radius=5))

        if image.mode != 'RGB':
            image = image.convert('RGB')

        cell_width = width // 7
        cell_height = height // 7

        color_data = []

        for y in range(1, 6):
            for x in range(1, 6):
                center_x = x * cell_width + cell_width // 2
                center_y = y * cell_height + cell_height // 2

                if 0 <= center_x < width and 0 <= center_y < height:
                    pixel = image.getpixel((center_x, center_y))
                    color_data.append(pixel)

        return color_data



        
    def process_image(self, image_name):
        try:
            img_path = os.path.join(self.filepath, image_name)
            
            pil_img = Image.open(img_path)
            
            file_size = os.path.getsize(img_path)
            file_type = os.path.splitext(image_name)[1].lower()
            shown_size = self.get_shown_size(file_size)
            
            color_data = self.sample_image_colors(pil_img)
            
            data_filename = f"{os.path.splitext(image_name)[0]}_color_data.txt"
            data_path = os.path.join(self.filepath, data_filename)
            self.save_color_data(color_data, data_path)
            
            matches = self.find_similar_images(color_data, image_name)
            
            if matches:
                self.show_comparison_ui(image_name, img_path, pil_img, shown_size, file_type, matches)
            else:
                messagebox.showinfo("No Duplicates", "No similar images found.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error processing image: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Duplicate Remover')
    gallery = ImageGallery(root)
    root.mainloop()