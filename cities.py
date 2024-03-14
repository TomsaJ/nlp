import yaml

# Lese die Liste von Städten aus der Datei ein
with open("cities.txt", "r") as file:
    cities = file.readlines()
cities = [city.strip() for city in cities]

# Erstelle Stories für jede Stadt
stories = []
for city in cities:
    story = f"""
  - story: Weather query with specified city - {city}
    steps:
      - intent: greet
      - action: utter_greet
      - intent: weather_query
      - action: utter_ask_city
      - intent: inform
        entities:
          - city: "{city}"
      - action: action_get_weather
      - intent: goodbye
      - action: utter_goodbye
"""
    stories.append(story)

# Speichere die generierten Stories in einer YAML-Datei
with open("data/stories.yml", "w") as file:
    file.write("version: '2.0'\n\n")
    file.write("stories:\n")
    for story in stories:
        file.write(story)
