import webbrowser


def open_website(command):

    if "google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    elif "github" in command:
        webbrowser.open("https://github.com")
        return "Opening GitHub."

    elif "gmail" in command:
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail."

    return 