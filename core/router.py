"""
Command Router — maps spoken commands to skill handlers.
"""

from __future__ import annotations

from core.speech import Speaker
import skills.time_date as time_date
import skills.web_search as web_search
import skills.wikipedia_skill as wiki
import skills.jokes as jokes
import skills.system_info as system_info
import skills.apps as apps
import skills.clipboard as clipboard
import skills.screenshot as screenshot
import skills.brightness as brightness
import skills.volume as volume
import skills.calculator as calculator
import skills.weather as weather


class Router:
    def __init__(self, speaker: Speaker):
        self.speaker = speaker

        # Ordered list of (keywords, handler_function)
        self._routes: list[tuple[tuple[str, ...], callable]] = [
            # Time / Date
            (("what time", "current time", "tell me the time"), time_date.tell_time),
            (("what date", "today's date", "what day"), time_date.tell_date),

            # Wikipedia
            (("wikipedia", "who is", "what is", "tell me about"), wiki.search),

            # Web search
            (("search", "google", "look up", "browse"), web_search.search),

            # Jokes
            (("joke", "make me laugh", "tell me a joke", "funny"), jokes.tell_joke),

            # System info
            (("cpu", "processor usage"), system_info.cpu_usage),
            (("memory", "ram usage"), system_info.memory_usage),
            (("battery", "battery status"), system_info.battery_status),
            (("disk", "storage"), system_info.disk_usage),

            # Apps
            (("open notepad",), lambda cmd, spk: apps.open_app("notepad", spk)),
            (("open calculator",), lambda cmd, spk: apps.open_app("calc", spk)),
            (("open browser", "open chrome", "open edge"), lambda cmd, spk: apps.open_browser(spk)),
            (("open file explorer",), lambda cmd, spk: apps.open_app("explorer", spk)),

            # Clipboard
            (("copy", "clipboard"), clipboard.handle),

            # Screenshot
            (("screenshot", "take a screenshot", "capture screen"), screenshot.take),

            # Brightness
            (("brightness",), brightness.handle),

            # Volume
            (("volume",), volume.handle),
            (("mute",), volume.mute),

            # Calculator
            (("calculate", "what is", "compute"), calculator.calculate),

            # Weather
            (("weather", "temperature", "climate"), weather.get_weather),
        ]

    def handle(self, command: str) -> None:
        for keywords, handler in self._routes:
            if any(kw in command for kw in keywords):
                try:
                    handler(command, self.speaker)
                except Exception as e:
                    self.speaker.say("Sorry, something went wrong with that skill.")
                    print(f"[Router] Error in handler: {e}")
                return

        self.speaker.say("I'm not sure how to help with that. Try asking differently.")
