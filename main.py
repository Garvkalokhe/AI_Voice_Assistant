import re
import speech_recognition as sr

from assistant import VoiceAssistant
from commands import get_current_time, get_current_date
from websites import open_website
from weather import get_weather
from news import get_news
from reminder import set_reminder


recognizer = sr.Recognizer()
assistant = VoiceAssistant()

def reminder_callback(message):

    assistant.speak("Reminder: " + message)


def listen():

    with sr.Microphone() as source:

        print("Listening...")

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio)

        print("You:", text)

        return text.lower()

    except sr.UnknownValueError:

        assistant.speak("Sorry, I couldn't understand that.")

        return ""

    except sr.RequestError:

        assistant.speak("Speech recognition service is unavailable.")

        return ""


def process_command(command):

    if "hello" in command or "hi" in command:

        assistant.speak("Hello! How can I help you?")

    elif "your name" in command:

        assistant.speak("I am your personal voice assistant.")

    elif "time" in command:

        response = get_current_time()

        assistant.speak(response)

    elif "date" in command:

        response = get_current_date()

        assistant.speak(response)


    elif "remind me" in command:

        pattern = r"remind me in (\d+) (second|seconds|minute|minutes) to (.+)"

        match = re.search(pattern, command)

        if match:

            amount = int(match.group(1))
            unit = match.group(2)
            message = match.group(3).strip()

            response = set_reminder(
                amount,
                unit,
                message,
                reminder_callback
            )

            assistant.speak(response)

        else:

            assistant.speak(
                "Please say the reminder like: "
                "remind me in 1 minute to drink water."
            )

    elif "weather" in command:

        if " in " in command:

            city = command.split(" in ", 1)[1].strip()

            response = get_weather(city)

            assistant.speak(response)

        else:

            assistant.speak("Which city would you like the weather for?")

            city = listen()

            if city:

                response = get_weather(city)

                assistant.speak(response)

            else:

                assistant.speak("Sorry, I could not understand the city.")

    elif "news" in command:

        headlines = get_news()

        assistant.speak("Here are the latest news headlines.")

        for headline in headlines:

            assistant.speak(headline)

    elif "open" in command:

        response = open_website(command)

        if response:

            assistant.speak(response)

        else:

            assistant.speak("Sorry, I don't know that website.")

    elif "exit" in command or "quit" in command or "stop" in command:

        assistant.speak("Goodbye!")

        return False

    else:

        assistant.speak("I heard you say " + command)

    return True


# Start the assistant

assistant.speak("Hello! I am your personal voice assistant.")

assistant.speak("How can I help you?")


running = True


while running:

    command = listen()

    if command:

        running = process_command(command)