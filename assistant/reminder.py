import os

REMINDER_FILE = "reminders.txt"

def add_reminder(text):
    with open(REMINDER_FILE, "a") as f:
        f.write(f"{text}\n")

def get_reminders():
    if not os.path.exists(REMINDER_FILE):
        return "You have no reminders."

    with open(REMINDER_FILE, "r") as f:
        lines = f.readlines()
        return "Here are your reminders:\n" + "".join(lines)
