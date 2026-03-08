"""Skill: read from or write to the clipboard."""

import pyperclip


def handle(command: str, speaker) -> None:
    if "read" in command or "what is" in command or "paste" in command:
        content = pyperclip.paste()
        if content:
            speaker.say(f"Your clipboard contains: {content[:200]}")
        else:
            speaker.say("The clipboard is empty.")
    else:
        # Extract text after "copy"
        text = command.replace("copy", "").strip()
        if text:
            pyperclip.copy(text)
            speaker.say(f"Copied to clipboard: {text}")
        else:
            speaker.say("What would you like me to copy?")
