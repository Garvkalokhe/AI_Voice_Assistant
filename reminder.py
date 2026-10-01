import threading


def set_reminder(amount, unit, message, callback):

    if unit in ["second", "seconds"]:
        seconds = amount
        time_text = f"{amount} second" if amount == 1 else f"{amount} seconds"

    else:
        seconds = amount * 60
        time_text = f"{amount} minute" if amount == 1 else f"{amount} minutes"

    timer = threading.Timer(
        seconds,
        callback,
        args=[message]
    )

    timer.daemon = True
    timer.start()

    return f"Okay, I will remind you in {time_text} to {message}."


if __name__ == "__main__":

    def test_callback(message):
        print("REMINDER:", message)

    print(set_reminder(10, "seconds", "drink water", test_callback))

    print("Waiting for reminder...")

    input("Press Enter to exit...")