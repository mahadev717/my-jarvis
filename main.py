"""
JARVIS - Just A Rather Very Intelligent System
Entry point
"""

import os
import sys

# Ensure the project root is on the path
sys.path.insert(0, os.path.dirname(__file__))

from core.assistant import Assistant


def main():
    jarvis = Assistant()
    jarvis.run_with_ui()


if __name__ == "__main__":
    main()
