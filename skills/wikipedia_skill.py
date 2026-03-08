"""Skill: Wikipedia summaries."""

import wikipedia


def search(command: str, speaker) -> None:
    # Strip common trigger words to get the actual query
    query = command
    for prefix in ("wikipedia", "who is", "what is", "tell me about"):
        query = query.replace(prefix, "").strip()

    if not query:
        speaker.say("What would you like me to look up?")
        return

    try:
        summary = wikipedia.summary(query, sentences=2, auto_suggest=True)
        speaker.say(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        speaker.say(f"That topic is ambiguous. Did you mean: {e.options[0]}?")
    except wikipedia.exceptions.PageError:
        speaker.say(f"I couldn't find a Wikipedia page for {query}.")
