from tkinter import Tk, Canvas, Button, filedialog
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("LoutersView 1.0")
        self.master.geometry("500x500")

        self.canvas = Canvas(self.master)
        self.canvas.pack(fill="both", expand=True)

        self.image = None

        self.load_button = Button(self.master, text="Load Image", command=self.load_image)
        self.load_button.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            self.image = Image.open(file_path)
            self.display_image()

    def display_image(self):
        if self.image:
            self.image.thumbnail((400, 400))
            img = ImageTk.PhotoImage(self.image)
            self.canvas.config(width=img.width(), height=img.height())
            self.canvas.create_image(0, 0, anchor="nw", image=img)
            self.canvas.image = img

if __name__ == "__main__":
    root = Tk()
    app = ImageViewer(root)
    root.mainloop()
