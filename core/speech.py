"""
Speech I/O — microphone listening and text-to-speech output.
"""

import pyttsx3
import speech_recognition as sr


class Speaker:
    """Text-to-speech wrapper around pyttsx3."""

    def __init__(self, rate: int = 175, volume: float = 1.0, voice_index: int = 0):
        self._engine = pyttsx3.init()
        self._engine.setProperty("rate", rate)
        self._engine.setProperty("volume", volume)
        voices = self._engine.getProperty("voices")
        if voices:
            idx = min(voice_index, len(voices) - 1)
            self._engine.setProperty("voice", voices[idx].id)

    def say(self, text: str) -> None:
        print(f"JARVIS: {text}")
        self._engine.say(text)
        self._engine.runAndWait()


class Listener:
    """Microphone listener wrapper around SpeechRecognition."""

    def __init__(self, timeout: int = 5, phrase_limit: int = 10):
        self._recognizer = sr.Recognizer()
        self._timeout = timeout
        self._phrase_limit = phrase_limit

    def listen(self) -> str | None:
        """Return transcribed text or None on failure."""
        with sr.Microphone() as source:
            print("Listening...")
            self._recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self._recognizer.listen(
                    source,
                    timeout=self._timeout,
                    phrase_time_limit=self._phrase_limit,
                )
                text = self._recognizer.recognize_google(audio)
                print(f"You: {text}")
                return text.lower()
            except sr.WaitTimeoutError:
                return None
            except sr.UnknownValueError:
                return None
            except sr.RequestError as e:
                print(f"[Speech] Recognition service error: {e}")
                return None
