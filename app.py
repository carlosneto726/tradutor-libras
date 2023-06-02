from tkinter import messagebox
import speech_recognition as sr
from unidecode import unidecode
from db import Conn


def ouvir_microfone():
    microfone = sr.Recognizer()
    
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        messagebox.showinfo(message='Diga alguma coisa')
        audio = microfone.listen(source)
        
    try:
        frase = unidecode(microfone.recognize_google(audio,language='pt-BR'))
        print("Você disse: " + frase)
        link = traduzir_frase(frase.lower())[0][1]
        
    except sr.UnknownValueError:
        messagebox.showinfo(message='Não entendi o você disse, tente novamente.')
        link = None
    except:
        messagebox.showinfo(message='Não achei essa palavra no nosso banco de dados.')
        link = None
        
    return link

def traduzir_frase(word):
    conn = Conn("libras")

    try:
        condicao = f"WHERE titulo = '{word}' OR titulo LIKE '%{word}%'"
    except:
        print("Não achei essa palavra no banco de dados.")

    return conn.select(condicao)


def retornaPalavraByLink(link):
    conn = Conn("libras")

    try:
        condicao = f"WHERE link = '{link}'"
    except:
        print("Não achei essa palavra no banco de dados.")

    return conn.select(condicao)


def retornaLinkByPalavra(word):
    conn = Conn("libras")

    try:
        condicao = f"WHERE titulo = '{word}' OR titulo LIKE '%{word}%'"
    except:
        print("Não achei essa palavra no banco de dados.")

    return conn.select(condicao)

#if __name__ == "__main__":
#    link = ouvir_microfone()
#    if link != None:
#        Gui(link)



