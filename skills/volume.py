"""Skill: system volume control via pycaw (Windows)."""

from __future__ import annotations

try:
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    import math

    def _get_volume_interface():
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        return cast(interface, POINTER(IAudioEndpointVolume))

    _PYCAW_AVAILABLE = True
except Exception:
    _PYCAW_AVAILABLE = False


def handle(command: str, speaker) -> None:
    if not _PYCAW_AVAILABLE:
        speaker.say("Volume control is not available on this system.")
        return

    words = command.split()
    level = None
    for word in words:
        if word.isdigit():
            level = int(word)
            break

    vol = _get_volume_interface()

    if level is not None:
        level = max(0, min(100, level))
        # pycaw uses scalar 0.0–1.0
        vol.SetMasterVolumeLevelScalar(level / 100.0, None)
        speaker.say(f"Volume set to {level} percent.")
    else:
        current = round(vol.GetMasterVolumeLevelScalar() * 100)
        speaker.say(f"Current volume is {current} percent.")


def mute(command: str, speaker) -> None:
    if not _PYCAW_AVAILABLE:
        speaker.say("Volume control is not available on this system.")
        return

    vol = _get_volume_interface()
    is_muted = vol.GetMute()
    vol.SetMute(not is_muted, None)
    state = "muted" if not is_muted else "unmuted"
    speaker.say(f"Audio {state}.")
