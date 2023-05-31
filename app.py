
import speech_recognition as sr
from db import Conn
from gui import Gui

def ouvir_microfone():
    microfone = sr.Recognizer()
    
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)
        
    try:
        frase = microfone.recognize_google(audio,language='pt-BR')
        
        print("Você disse: " + frase)
        print(traduzir_frase(frase.lower())[0][1])
        
    except sr.UnknownValueError:
        print("Não entendi")
        
    return traduzir_frase(frase.lower())[0][1]

def traduzir_frase(frase):
    conn = Conn("libras")

    condicao = f"WHERE titulo = '{frase}'"

    return conn.select(condicao)

if __name__ == "__main__":
    gui = Gui(ouvir_microfone())



