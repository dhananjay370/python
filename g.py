import tkinter as tk
from PIL import ImageTk, Image

class ImageViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Viewer")
        self.master.geometry("500x500")

        self.image_path = "path/to/image.jpg"
        self.image = Image.open(self.image_path)
        self.image.thumbnail((400, 400), Image.ANTIALIAS)
        self.image_tk = ImageTk.PhotoImage(self.image)

        self.label_image = tk.Label(self.master, image=self.image_tk)
        self.label_image.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()
