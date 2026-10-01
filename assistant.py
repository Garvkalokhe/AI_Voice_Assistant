import pyttsx3


class VoiceAssistant:

    def __init__(self):
        pass

    def speak(self, text):
        print("Assistant:", text)

        # Create a fresh SAPI5 engine for every response
        engine = pyttsx3.init("sapi5")

        voices = engine.getProperty("voices")

        if voices:
            engine.setProperty("voice", voices[0].id)

        engine.setProperty("rate", 150)
        engine.setProperty("volume", 1.0)

        engine.say(text)
        engine.runAndWait()

        engine.stop()