import speech_recognition as sr
import pyttsx3

# Inicializa classe reconhecedora (para reconhecer a fala)
r = sr.Recognizer()

# Inicializa a engine
alice = pyttsx3.init()

def speak(text):
    alice.say(text)
    alice.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Escuta...")
        audio = r.listen(source)
        try:
            print("Reconhecendo...")
            query = r.recognize_google(audio, language='pt-br')
            print(f"Usuário disse: {query}\n")
        except Exception as e:
            print("Diga isso novamente, por favor...")
            return "None"
        return query.lower()

speak("Olá, como posso ajudar?")
listen()