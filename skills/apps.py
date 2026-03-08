"""Skill: launch applications and the browser."""

import subprocess
import webbrowser


def open_app(app_name: str, speaker) -> None:
    try:
        subprocess.Popen(app_name, shell=True)
        speaker.say(f"Opening {app_name}.")
    except Exception as e:
        speaker.say(f"Could not open {app_name}.")
        print(f"[apps] {e}")


def open_browser(speaker) -> None:
    webbrowser.open("https://www.google.com")
    speaker.say("Opening your web browser.")
