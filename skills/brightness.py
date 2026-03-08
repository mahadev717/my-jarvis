"""Skill: get or set screen brightness."""

import screen_brightness_control as sbc


def handle(command: str, speaker) -> None:
    # Detect a number in the command
    words = command.split()
    level = None
    for word in words:
        if word.isdigit():
            level = int(word)
            break

    if level is not None:
        level = max(0, min(100, level))
        sbc.set_brightness(level)
        speaker.say(f"Screen brightness set to {level} percent.")
    else:
        try:
            current = sbc.get_brightness(display=0)
            if isinstance(current, list):
                current = current[0]
            speaker.say(f"Current screen brightness is {current} percent.")
        except Exception:
            speaker.say("I couldn't read the screen brightness.")
