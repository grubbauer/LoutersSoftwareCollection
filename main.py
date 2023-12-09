import tkinter as tk
from tkinter import filedialog
from tkinter import font

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        custom_font = font.Font(family="Arial", size=12)
        self.text_area = tk.Text(self.root, wrap="word", undo=True, font=custom_font)
        self.text_area.pack(expand="yes", fill="both")
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.destroy)
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
    def open_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())
    def save_file(self):
        current_file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
        )
        if current_file:
            with open(current_file, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
    def save_as_file(self):
        new_file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
        )
        if new_file:
            with open(new_file, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()