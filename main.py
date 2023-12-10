import tkinter as tk
from tkinter import filedialog
import pygame
import os

class AudioPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Player")
        self.root.geometry("300x150")

        self.playlist = []

        self.create_gui()
        self.init_player()

    def create_gui(self):
        # Buttons
        self.play_button = tk.Button(self.root, text="Play", command=self.play)
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Files", command=self.add_files)
        self.add_button.pack(pady=10)

        # Playlist
        self.playlist_label = tk.Label(self.root, text="Playlist:")
        self.playlist_label.pack()

        self.playlist_box = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.playlist_box.pack()

    def init_player(self):
        pygame.init()
        pygame.mixer.init()

    def add_files(self):
        files = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if files:
            self.playlist.extend(files)
            self.update_playlist_box()

    def update_playlist_box(self):
        self.playlist_box.delete(0, tk.END)
        for file_path in self.playlist:
            self.playlist_box.insert(tk.END, os.path.basename(file_path))

    def play(self):
        selected_index = self.playlist_box.curselection()
        if selected_index:
            selected_file = self.playlist[selected_index[0]]
            pygame.mixer.music.load(selected_file)
            pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    audio_player = AudioPlayer(root)
    root.mainloop()
