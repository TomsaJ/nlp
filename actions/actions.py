import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGetWeather(Action):
    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Stadt extrahieren
        city = tracker.get_slot("city")

        if city:
            # API-Anfrage für das Wetter der angegebenen Stadt
            weather_api_key = "ae58b9e382aef8f16fc5b5b2e7155d43"  # Hier sollte dein API-Schlüssel sein
            weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
            response = requests.get(weather_api_url)
            weather_data = response.json()

            if weather_data["cod"] == 200:
                # Wetterdaten extrahieren
                description = weather_data["weather"][0]["description"]
                temperature = weather_data["main"]["temp"]
                message = f"In {city} ist das Wetter {description} mit einer Temperatur von {temperature}°C."
            else:
                message = "Entschuldigung, ich konnte das Wetter für diese Stadt nicht abrufen."
        else:
            message = "Entschuldigung, ich habe die Stadt nicht verstanden."

        # Nachricht an den Benutzer senden
        dispatcher.utter_message(message)

        return []
