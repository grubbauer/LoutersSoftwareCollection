import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("LoutersWatch 1.0")

        self.video_frame = tk.Frame(self.root)
        self.video_frame.pack(pady=10)

        self.canvas = tk.Canvas(self.video_frame)
        self.canvas.pack()

        self.play_button = tk.Button(self.root, text="Play", command=self.play_video)
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_video)
        self.stop_button.pack(pady=5)

        self.video_path = None
        self.cap = None
        self.is_playing = False

    def play_video(self):
        if not self.is_playing:
            self.video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])
            if self.video_path:
                self.cap = cv2.VideoCapture(self.video_path)
                self.is_playing = True
                self.show_frame()

    def show_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image=image)

            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.photo = photo

            if self.is_playing:
                self.root.after(10, self.show_frame)
        else:
            self.cap.release()
            self.is_playing = False

    def stop_video(self):
        if self.is_playing:
            self.cap.release()
            self.is_playing = False

if __name__ == "__main__":
    root = tk.Tk()
    player = VideoPlayer(root)
    root.mainloop()
