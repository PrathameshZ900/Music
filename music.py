import os
import pygame
from tkinter import Tk, Label, Button, filedialog

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        self.master.geometry("400x200")

        self.current_song_label = Label(master, text="Current Song: None", font=("Helvetica", 12))
        self.current_song_label.pack(pady=10)

        self.play_button = Button(master, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)

        self.pause_button = Button(master, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=10)

        self.stop_button = Button(master, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)

        self.choose_button = Button(master, text="Choose Song", command=self.choose_song)
        self.choose_button.pack(pady=10)

        pygame.mixer.init()

    def play_music(self):
        if hasattr(self, 'current_song'):
            pygame.mixer.music.load(self.current_song)
            pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def choose_song(self):
    # Replace 'dummy_song.mp3' with the actual path to your MP3 file
    song_path = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")], initialdir=os.path.dirname(__file__), initialfile="dummy_song.mp3")

    if song_path:
        self.current_song = song_path
        self.current_song_label.config(text="Current Song: " + os.path.basename(song_path))


        if song_path:
            self.current_song = song_path
            self.current_song_label.config(text="Current Song: " + os.path.basename(song_path))

if __name__ == "__main__":
    root = Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
