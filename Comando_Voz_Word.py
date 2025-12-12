
import speech_recognition as sr
import subprocess
import os

def ouvir_comando():
    meu_microfone = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga o comando...")
        meu_microfone.adjust_for_ambient_noise(source)
        audio = meu_microfone.listen(source)

    try:
        comando = meu_microfone.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        return None
    except sr.RequestError:
        print("Erro ao conectar ao serviço de reconhecimento.")
        return None

def executar_comando(comando):
    if "abrir word" in comando:
        print("Abrindo Microsoft Word...")
        subprocess.Popen(["start", "winword"], shell=True)
    else:
        print("Comando não reconhecido.")



if __name__ == "__main__":
    comando = ouvir_comando()
    if comando:
        executar_comando(comando)

    
