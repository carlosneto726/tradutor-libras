import tkinter as tk
from tkVideoPlayer import TkinterVideo

class Gui:
    def __init__(self, url):
        self.url = url
        self.root = tk.Tk()
        self.videoplayer = TkinterVideo(master=self.root,  scaled=True)
        self.videoplayer.load(url)
        self.videoplayer.pack(expand=True, fill="both")
        self.videoplayer.set_scaled(False)
        self.play_pause_btn = tk.Button(text="Play", command=self.play_pause)
        self.play_pause_btn.pack()
        self.videoplayer.play()
        self.videoplayer.pause()
        self.videoplayer.bind("<<Ended>>", self.vido_ended )
        self.root.mainloop()

    def play_pause(self):
        if self.videoplayer.is_paused():
            self.videoplayer.play()
            self.play_pause_btn["text"] = "Pause"
        else:
            self.videoplayer.pause()
            self.play_pause_btn["text"] = "Play"


    def replay(self):
        self.videoplayer.seek(0)


    def vido_ended(self, event):
        self.play_pause_btn["text"] = "Replay"
        self.replay()

