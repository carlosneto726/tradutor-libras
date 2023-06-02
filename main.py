import tkinter as tk
from tkVideoPlayer import TkinterVideo
import app


def play_pause():
    if videoplayer.is_paused():
        videoplayer.play()
        play_pause_btn["text"] = "Pause"
    else:
        videoplayer.pause()
        play_pause_btn["text"] = "Play"


def replay():
    videoplayer.seek(0)


def vido_ended(event):
    play_pause_btn["text"] = "Replay"
    replay()


def listen():
    url = app.ouvir_microfone()
    label.config(text=f"A palavra {app.retornaPalavraByLink(url)[0][0]} em libras é:")
    videoplayer.load(url)
    
def text_input():
    inp = inputtxt.get(1.0, "end-1c")
    url = app.retornaLinkByPalavra(inp)[0][1]

    label.config(text=f"A palavra {app.retornaPalavraByLink(url)[0][0]} em libras é:")
    videoplayer.load(url)

url = app.ouvir_microfone()
root = tk.Tk()
root.geometry("1000x600")
root.title("Tradutor Libras")

T = tk.Text(root, height = 5, width = 52)
label = tk.Label(root, text=f"A palavra {app.retornaPalavraByLink(url)[0][0]} em libras é:")
label.config(font =("Courier", 14))
label.pack()

videoplayer = TkinterVideo(master=root,  scaled=True)
videoplayer.load(url)
videoplayer.pack(expand=True, fill="both")
videoplayer.set_scaled(False)
play_pause_btn = tk.Button(text="Play", command=play_pause)
play_pause_btn.pack()
listen_btn = tk.Button(text="Listen", command=listen)
listen_btn.pack()

inputtxt = tk.Text(root, height = 1, width = 50)
inputtxt.pack()

input_button = tk.Button(text="Confirmar", command=text_input)
input_button.pack()

videoplayer.play()
videoplayer.pause()
videoplayer.bind("<<Ended>>", vido_ended )
root.mainloop()
