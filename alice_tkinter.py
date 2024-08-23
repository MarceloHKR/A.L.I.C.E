'''import speech_recognition as sr
import pyttsx3
from tkinter import *

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Initialize the engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='pt-br')
            print(f"User said: {query}\n")
            return query.lower()
        except Exception as e:
            print("Say that again please...")
            return "None"

def on_button_click():
    query = listen()
    if query != "None":
        speak("Você disse: " + query)

# Create tkinter window
root = Tk()
root.title("AI ativada por voz")

# Create button
button = Button(root, text="Fale", command=on_button_click)
button.pack()

# Start tkinter event loop
root.mainloop()'''