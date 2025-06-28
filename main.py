from assistant.listen import listen_command
from assistant.speak import speak_text
from assistant.intent import detect_intent
from assistant.weather import get_weather
from assistant.wiki import search_wikipedia
from assistant.reminder import add_reminder, get_reminders
from assistant.apps import open_app
from assistant.get_response import get_gpt_reply  # ←✅ move it here
import datetime
import webbrowser
from dotenv import load_dotenv
load_dotenv()

def main():
    speak_text("Hi shashi! I’m your assistant. How can I help you today?")

    while True:
        command = listen_command().lower()
        intent = detect_intent(command)

        # 🔌 Exit Command
        if any(word in command for word in ["stop", "exit", "bye", "quit"]):
            speak_text("Goodbye! Have a great day.")
            break

        # 🌤️ Weather
        elif intent == "weather":
            speak_text("Which city do you want the weather for?")
            city = listen_command()
            report = get_weather(city)
            speak_text(report)

        # 📖 Wikipedia Search
        elif intent == "ask_question":
            speak_text("Let me think...")
            result = get_gpt_reply(command)
            speak_text(result)


        # ⏰ Reminders
        elif intent == "reminder":
            speak_text("What should I remind you about?")
            reminder = listen_command()
            add_reminder(reminder)
            speak_text("Got it. Reminder added.")

        elif "read reminders" in command:
            speak_text(get_reminders())

        # 💻 Open Apps
        elif intent == "open_app":
            speak_text("Which app would you like me to open?")
            app = listen_command()
            result = open_app(app)
            speak_text(result)

        # 🕒 Time
        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak_text(f"The current time is {now}")

        # 🌐 Open Website
        elif intent == "open_website":
            speak_text("Which website should I open?")
            site = listen_command().replace(" ", "")
            webbrowser.open(f"https://{site}")
            speak_text(f"Opening {site}")
            
        elif intent == "chat":
            speak_text("Let me think...")
            reply = get_gpt_reply(command)
            speak_text(reply)


        else:
            speak_text("Sorry, I didn’t understand that. Can you repeat?")

if __name__ == "__main__":
    main()
