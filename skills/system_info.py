"""Skill: CPU, RAM, battery and disk information via psutil."""

import psutil


def cpu_usage(command: str, speaker) -> None:
    usage = psutil.cpu_percent(interval=1)
    speaker.say(f"CPU usage is currently at {usage} percent.")


def memory_usage(command: str, speaker) -> None:
    mem = psutil.virtual_memory()
    used = round(mem.used / (1024 ** 3), 2)
    total = round(mem.total / (1024 ** 3), 2)
    speaker.say(f"RAM usage is {used} GB out of {total} GB, that's {mem.percent} percent.")


def battery_status(command: str, speaker) -> None:
    battery = psutil.sensors_battery()
    if battery is None:
        speaker.say("No battery detected — this might be a desktop computer.")
        return
    plugged = "plugged in" if battery.power_plugged else "not plugged in"
    speaker.say(
        f"Battery is at {round(battery.percent)} percent and is {plugged}."
    )


def disk_usage(command: str, speaker) -> None:
    disk = psutil.disk_usage("/")
    used = round(disk.used / (1024 ** 3), 2)
    total = round(disk.total / (1024 ** 3), 2)
    speaker.say(
        f"Disk usage is {used} GB used out of {total} GB, that's {disk.percent} percent."
    )
