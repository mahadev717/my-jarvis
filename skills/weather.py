import requests
from core.speech import Speaker

def get_weather(command: str, speaker: Speaker):
    """
    Fetches weather info for a city or default.
    Uses wttr.in/City?format=j1
    """
    city = ""
    # Extract city if "in [city]" is mentioned
    if " in " in command:
        city = command.split(" in ")[-1].strip()
    
    # Alternatively "weather of [city]"
    elif " of " in command:
        city = command.split(" of ")[-1].strip()

    url = f"https://wttr.in/{city}?format=%C+and+%t"
    
    speaker.say(f"Checking the weather {f'in {city}' if city else ''}...")
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            weather_data = response.text.strip()
            # Clean up output
            if "Unknown location" in weather_data:
                speaker.say("I couldn't find that location. Please try specifying a city.")
            else:
                speaker.say(f"The current weather is {weather_data}.")
        else:
            speaker.say("I am unable to reach the weather service at the moment.")
    except Exception as e:
        print(f"[Weather] Error: {e}")
        speaker.say("Sorry, I encountered an error while fetching the weather.")
