"""
Central Assistant — wires speech I/O with skill routing.
"""

import datetime
import threading
import time

from core.speech import Speaker, Listener
from core.router import Router
from core.ui import JarvisUI


class Assistant:
    WAKE_WORDS = {"jarvis", "hey jarvis", "ok jarvis"}
    EXIT_WORDS = {"exit", "quit", "goodbye", "bye", "stop", "shutdown"}

    def __init__(self):
        self.speaker = Speaker()
        self.listener = Listener()
        self.router = Router(self.speaker)
        self.ui = None

    # ------------------------------------------------------------------
    def greet(self) -> None:
        hour = datetime.datetime.now().hour
        if hour < 12:
            period = "morning"
        elif hour < 18:
            period = "afternoon"
        else:
            period = "evening"
        
        msg = f"Good {period}! I am JARVIS. How can I assist you today?"
        if self.ui:
            self.ui.update_status("Greeting...")
        self.speaker.say(msg)

    # ------------------------------------------------------------------
    def run_with_ui(self) -> None:
        """Starts UI in main thread and logic in background."""
        self.ui = JarvisUI()
        
        # Start logic thread
        logic_thread = threading.Thread(target=self._logic_loop, daemon=True)
        logic_thread.start()
        
        self.ui.start()

    def _logic_loop(self) -> None:
        """Main event loop running in background."""
        self.greet()
        
        while True:
            self.ui.update_status("Listening...")
            command = self.listener.listen()
            
            if command is None:
                continue

            # Check exit intent
            if any(word in command for word in self.EXIT_WORDS):
                self.ui.update_status("Shutting down...")
                self.speaker.say("Goodbye! Have a great day.")
                time.sleep(1)
                self.ui.stop()
                break

            # Strip wake word if present
            found_wake = False
            for wake in self.WAKE_WORDS:
                if command.startswith(wake):
                    command = command[len(wake):].strip()
                    found_wake = True
                    break
            
            # If no wake word and we didn't hear anything useful, wait
            if not command:
                continue

            self.ui.update_status("Thinking...")
            self.router.handle(command)
