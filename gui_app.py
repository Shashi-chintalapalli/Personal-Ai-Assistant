# gui_app.py

import tkinter as tk
from tkinter import scrolledtext
from assistant.listen import listen_command
from assistant.get_response import get_gpt_reply

import platform
import threading

# Use browser-based speech only if on macOS to avoid pyttsx3 issues
IS_MAC = platform.system() == "Darwin"

# Optional: Replace pyttsx3 with native Mac speak command (safe on GUI threads)
def speak_text(text):
    print(f"🗣️ Assistant: {text}")
    if IS_MAC:
        import os
        os.system(f"say '{text}'")  # macOS native speech
    else:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate', 170)
        engine.say(text)
        engine.runAndWait()

# GUI setup
root = tk.Tk()
root.title("AI Assistant")
root.geometry("500x600")
root.configure(bg="#1e1e1e")

# Chat display
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#1e1e1e", fg="white", font=("Helvetica", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.insert(tk.END, "🗣️ Assistant: Hi Shashi! I'm your AI Assistant.\n")
chat_area.config(state=tk.DISABLED)

# Entry field
input_text = tk.StringVar()
entry = tk.Entry(root, textvariable=input_text, font=("Helvetica", 14), bg="#333", fg="white", insertbackground="white")
entry.pack(padx=10, pady=(0, 10), fill=tk.X)

# --- Main Logic ---

def respond(text):
    def threaded_response():
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"🧑 You: {text}\n")
        chat_area.yview(tk.END)
        speak_text("Let me think...")

        reply = get_gpt_reply(text)

        chat_area.insert(tk.END, f"🤖 Assistant: {reply}\n")
        chat_area.config(state=tk.DISABLED)
        chat_area.yview(tk.END)
        speak_text(reply)

    threading.Thread(target=threaded_response).start()  # Avoid GUI freeze

def on_enter(event=None):
    user_input = input_text.get().strip()
    if user_input:
        input_text.set("")
        respond(user_input)

def on_mic():
    def mic_listen():
        speak_text("🎙️ Listening...")
        command = listen_command()
        if command:
            input_text.set(command)
            respond(command)

    threading.Thread(target=mic_listen).start()

# Buttons
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(padx=10, pady=(0, 10), fill=tk.X)

mic_btn = tk.Button(button_frame, text="🎤", command=on_mic, bg="#555", fg="white", font=("Helvetica", 12))
mic_btn.pack(side=tk.LEFT)

submit_btn = tk.Button(button_frame, text="Send", command=on_enter, bg="#4caf50", fg="white", font=("Helvetica", 12))
submit_btn.pack(side=tk.RIGHT)

entry.bind("<Return>", on_enter)

# Run app
root.mainloop()
