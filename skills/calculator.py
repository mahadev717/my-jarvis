"""Skill: evaluate simple arithmetic expressions spoken by the user."""

import re


# Map spoken words to operators / digits
_WORD_MAP = {
    "plus": "+", "add": "+", "added to": "+",
    "minus": "-", "subtract": "-", "subtracted from": "-",
    "times": "*", "multiplied by": "*", "multiply": "*",
    "divided by": "/", "divide": "/", "over": "/",
    "power": "**", "to the power of": "**",
    "zero": "0", "one": "1", "two": "2", "three": "3",
    "four": "4", "five": "5", "six": "6", "seven": "7",
    "eight": "8", "nine": "9", "ten": "10",
}


def _preprocess(command: str) -> str:
    text = command
    for word, symbol in sorted(_WORD_MAP.items(), key=lambda x: -len(x[0])):
        text = re.sub(rf"\b{word}\b", symbol, text)
    return text


def calculate(command: str, speaker) -> None:
    # Strip trigger words
    expr = command
    for prefix in ("calculate", "compute", "what is", "evaluate"):
        expr = expr.replace(prefix, "").strip()

    expr = _preprocess(expr)

    # Keep only safe characters
    safe = re.sub(r"[^0-9+\-*/().%\s\*]", "", expr).strip()

    if not safe:
        speaker.say("I couldn't parse that calculation. Please try again.")
        return

    try:
        result = eval(safe, {"__builtins__": {}})  # noqa: S307 — limited to math ops
        speaker.say(f"The result is {result}.")
    except ZeroDivisionError:
        speaker.say("You can't divide by zero.")
    except Exception:
        speaker.say("I couldn't calculate that. Please rephrase.")
