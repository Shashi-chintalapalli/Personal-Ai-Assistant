import os

def open_app(app_name):
    app_name = app_name.lower()

    app_map = {
        "safari": "Safari",
        "chrome": "Google Chrome",
        "notes": "Notes",
        "mail": "Mail",
        "calendar": "Calendar",
        "messages": "Messages",
        "facetime": "FaceTime",
        "system preferences": "System Settings",
        "terminal": "Terminal"
    }

    if app_name in app_map:
        try:
            os.system(f"open -a '{app_map[app_name]}'")
            return f"Opening {app_map[app_name]}"
        except Exception as e:
            return f"❌ Could not open {app_map[app_name]}: {e}"
    else:
        return f"⚠️ Sorry, I don’t know how to open {app_name}."
