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


if __name__ == "__main__":

    root = tk.Tk()
    root.geometry("1000x600")
    root.title("Tradutor Libras")

    T = tk.Text(root, height = 5, width = 52)
    label = tk.Label(root, text=f"Bem vindo ao tradutor de libras, você pode falar ou digitar \numa palavra, e ela será traduzida em Libras.")
    label.config(font =("Courier", 14))
    videoplayer = TkinterVideo(master=root,  scaled=True)
    videoplayer.bind("<<Ended>>", vido_ended )
    play_pause_btn = tk.Button(text="Play", command=play_pause)
    listen_btn = tk.Button(text="Ouvir", command=listen)
    inputtxt = tk.Text(root, height = 1, width = 50)
    input_button = tk.Button(text="Confirmar", command=text_input)

    label.pack()
    videoplayer.pack(expand=True, fill="both")
    play_pause_btn.pack()
    listen_btn.pack()
    inputtxt.pack()
    input_button.pack()

    root.mainloop()