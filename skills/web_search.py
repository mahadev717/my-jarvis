"""Skill: open a Google search in the default browser."""

import webbrowser
import urllib.parse


def search(command: str, speaker) -> None:
    query = command
    for prefix in ("search for", "search", "google", "look up", "browse"):
        query = query.replace(prefix, "").strip()

    if not query:
        speaker.say("What should I search for?")
        return

    url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
    webbrowser.open(url)
    speaker.say(f"Here are the search results for {query}.")
