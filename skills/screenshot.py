"""Skill: capture a screenshot and save it to the desktop."""

import os
import datetime
import pyautogui


def take(command: str, speaker) -> None:
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    os.makedirs(desktop, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(desktop, f"screenshot_{timestamp}.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    speaker.say(f"Screenshot saved to your Desktop as screenshot_{timestamp}.png")
