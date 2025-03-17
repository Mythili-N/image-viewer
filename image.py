
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("800x600")  # Increased size for better display

        self.image_list = []
        self.current_image_index = -1

        self.canvas = tk.Canvas(self.root, bg="black")  # Set background color
        self.canvas.pack(fill="both", expand=True)

        # Buttons for navigation
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side="bottom", fill="x", padx=5, pady=5)

        self.prev_button = tk.Button(self.button_frame, text="Previous", command=self.show_previous_image)
        self.prev_button.pack(side="left", padx=5)

        self.next_button = tk.Button(self.button_frame, text="Next", command=self.show_next_image)
        self.next_button.pack(side="left", padx=5)

        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.root.quit)
        self.exit_button.pack(side="right", padx=5)

        # Load images
        self.load_images()

        # Resize event
        self.root.bind("<Configure>", self.on_resize)

    def load_images(self):
        folder = filedialog.askdirectory(title="Select Folder with Images")
        
        if folder:
            self.image_list = [
                os.path.join(folder, f) for f in os.listdir(folder)
                if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))
            ]
            
            if self.image_list:
                self.show_image(0)

    def show_image(self, index):
        if 0 <= index < len(self.image_list):
            image_path = self.image_list[index]
            image = Image.open(image_path)

            # Resize image to fit the canvas while maintaining aspect ratio
            canvas_width = self.canvas.winfo_width() or 800  # Default width if not set
            canvas_height = self.canvas.winfo_height() or 600  # Default height if not set
            image.thumbnail((canvas_width, canvas_height), Image.Resampling.LANCZOS)

            image_tk = ImageTk.PhotoImage(image)
            self.canvas.delete("all")  # Clear previous images
            self.canvas.create_image(canvas_width // 2, canvas_height // 2, image=image_tk, anchor="center")
            self.canvas.image = image_tk  # Keep a reference

            self.current_image_index = index

    def show_next_image(self):
        if self.current_image_index + 1 < len(self.image_list):
            self.show_image(self.current_image_index + 1)

    def show_previous_image(self):
        if self.current_image_index - 1 >= 0:
            self.show_image(self.current_image_index - 1)

    def on_resize(self, event):
        if self.current_image_index != -1:
            self.show_image(self.current_image_index)

if __name__ == "__main__":
    root = tk.Tk()
    viewer = ImageViewer(root)
    root.mainloop()
