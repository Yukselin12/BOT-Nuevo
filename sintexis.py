import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate",150)

voices = engine.getProperty("voices")
for index, voice in enumerate(voices):
    print(f"voz {index} - {voice.name} - {voice.languages}")

engine.setProperty("voice", voices[1].id)



def speak(texto):
    engine.say(texto)
    engine.runAndWait()

