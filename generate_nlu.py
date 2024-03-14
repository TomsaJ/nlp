import random

# Lese Städte aus der cities.txt-Datei
with open("cities.txt", "r", encoding="utf-8") as file:
    cities = [city.strip() for city in file.readlines()]



# Lese Sätze aus der sentences.txt.txt-Datei
with open("sentences.txt", "r", encoding="utf-8") as file:
    sentences = [sentence.strip() for sentence in file.readlines()]

# Begrüßungs- und Abschiedsabschnitte
greet_examples = ["Hallo", "Hi", "Guten Tag"]
goodbye_examples = ["Tschüss", "Auf Wiedersehen", "Bis später"]
weather_query_examples = ["Wie ist das Wetter?", "Kannst du mir das Wetter sagen?", "Was ist das Wetter heute?"]

# Zufällige Auswahl von Sätzen und Städten
random_sentences = [random.choice(sentences) for _ in range(len(cities))]
random_cities = random.sample(cities, len(cities))

# Generiere Trainingsdaten mit zufällig ausgewählten Sätzen und Städten
examples = []
for sentence, city in zip(random_sentences, random_cities):
    example = f"{sentence} [{city}](city)?"
    examples.append(example)

# Füge Begrüßungs- und Abschiedsbeispiele hinzu

# Speichere die generierten Beispiele in einer NLU-Datei
with open("data/nlu.yml", "w") as file:
    file.write("version: '2.0'\n\n")
    file.write("nlu:\n")
    # Begrüßungsbeispiele
    file.write("  - intent: greet\n")
    file.write("    examples: |\n")
    for example in greet_examples:
        file.write(f"      - {example}\n")
    file.write("\n")
    # Abschiedsbeispiele
    file.write("  - intent: goodbye\n")
    file.write("    examples: |\n")
    for example in goodbye_examples:
        file.write(f"      - {example}\n")
    file.write("\n")
    # Wetternachfrage-Beispiele
    file.write("  - intent: weather_query\n")
    file.write("    examples: |\n")
    for example in weather_query_examples:
        file.write(f"      - {example}\n")
    file.write("\n")
    file.write("  - intent: inform\n")
    file.write("    examples: |\n")
    for example in examples:
        file.write(f"      - {example}\n")
    file.write("\n")
