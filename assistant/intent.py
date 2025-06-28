def detect_intent(command: str) -> str:
    command = command.lower()

    if any(word in command for word in ["weather", "temperature", "forecast", "climate"]):
        return "weather"
    elif any(word in command for word in ["reminder", "remind", "note this down", "remember"]):
        return "reminder"
    elif any(phrase in command for phrase in ["wikipedia", "who is", "what is", "tell me about"]):
        return "ask_question"
    elif any(word in command for word in ["open", "launch", "start", "run"]):
        return "open_app"
    elif any(phrase in command for phrase in ["website", "browse", "go to", "open site"]):
        return "open_website"
    elif any(phrase in command for phrase in ["time", "current time", "what time"]):
        return "get_time"
    elif any(phrase in command for phrase in ["exit", "quit", "stop", "goodbye"]):
        return "exit"
    else:
        return "chat"
