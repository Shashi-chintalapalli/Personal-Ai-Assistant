# assistant/speak.py

import pyttsx3
import platform

# Initialize text-to-speech engine
try:
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)  # Speed
    engine.setProperty('volume', 1.0)  # Max volume
except Exception as e:
    print(f"❌ Text-to-Speech engine initialization failed: {e}")
    engine = None

def speak_text(text):
    print(f"🗣️ Assistant: {text}")
    try:
        if engine:
            engine.say(text)
            engine.runAndWait()
    except RuntimeError as e:
        print(f"⚠️ Speak failed (possibly due to GUI conflict): {e}")
