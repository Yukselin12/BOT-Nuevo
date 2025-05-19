import pyttsx3
import requests

engine = pyttsx3.init()
engine.setProperty("rate",150)

voices = engine.getProperty("voices")
for index, voice in enumerate(voices):
    print(f"voz {index} - {voice.name} - {voice.languages}")

len = int(input("Elije una voz, Ingles = 0 Español = 1 "))
engine.setProperty("voice", voices[len].id)



def speak(texto):
    engine.say(texto)
    engine.runAndWait()

