"""Skill: current time and date."""

import datetime


def tell_time(command: str, speaker) -> None:
    now = datetime.datetime.now().strftime("%I:%M %p")
    speaker.say(f"The current time is {now}.")


def tell_date(command: str, speaker) -> None:
    today = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speaker.say(f"Today is {today}.")
