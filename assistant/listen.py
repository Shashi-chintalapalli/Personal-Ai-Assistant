import speech_recognition as sr

def listen_command(timeout=5, phrase_time_limit=10):
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎙️ Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

        text = recognizer.recognize_google(audio)
        print(f"✅ You said: {text}")
        return text

    except sr.WaitTimeoutError:
        print("⏰ Listening timed out while waiting for phrase.")
        return "Listening timed out."

    except sr.UnknownValueError:
        print("😕 Could not understand audio.")
        return "Sorry, I didn't catch that."

    except sr.RequestError as e:
        print(f"🔌 Could not request results; {e}")
        return "Speech service error."

    except Exception as e:
        print(f"⚠️ Error: {e}")
        return "There was an error capturing audio."
