"""Skill: tell a random joke via pyjokes."""

import pyjokes


def tell_joke(command: str, speaker) -> None:
    joke = pyjokes.get_joke()
    speaker.say(joke)
