from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionGetWeather(Action):
    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot("city")
        if not city:
            dispatcher.utter_message("Bitte geben Sie einen Stadtnamen an.")
            return []

        api_key = 'ae58b9e382aef8f16fc5b5b2e7155d43'  # Ihr OpenWeatherMap API-Schlüssel
        base_url = 'http://api.openweathermap.org/data/2.5/forecast'
        city_id = '524901'  # ID für Moscow als Beispielstadt
        params = {
            'id': city_id,
            'appid': api_key,
            'units': 'metric'  # Einheit: Celsius
        }

        try:
            response = requests.get(base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                weather_description = data['list'][0]['weather'][0]['description']
                temperature = data['list'][0]['main']['temp']
                dispatcher.utter_message(f"Das Wetter in {city} ist {weather_description} mit einer Temperatur von {temperature}°C.")
            else:
                dispatcher.utter_message("Entschuldigung, ich konnte die Wetterinformationen momentan nicht abrufen.")
        except Exception as e:
            dispatcher.utter_message("Fehler beim Abrufen der Wetterinformationen. Bitte versuchen Sie es später erneut.")

        return []

class ActionFrageWetter(Action):
    def name(self) -> Text:
        return "action_frage_wetter"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Führen Sie hier den Code aus, um das Wetter abzurufen und die Antwort zu senden

        return []
