import requests
from googletrans import Translator


def fetch_joke_from_api(category="Any"):
    url = f"https://v2.jokeapi.dev/joke/{category}?lang=en"
    response = requests.get(url)
    joke_data = response.json()

    if joke_data["type"] == "single":
        joke_text = joke_data.get("joke")
    else:
        joke_text = f"{joke_data.get('setup')} - {joke_data.get('delivery')}"

    return joke_text


def translate_joke_to_korean(joke_text, lang='ko'):
    translator = Translator()
    translated_text = translator.translate(joke_text, dest=lang).text
    return translated_text

joke_in_english = fetch_joke_from_api()
print("영어 유머:", joke_in_english)
joke_in_korean = translate_joke_to_korean(joke_in_english)
print("유머 (한국어 번역):", joke_in_korean)

joke_in_english = fetch_joke_from_api(category="Programming")
print("영어 유머:", joke_in_english)
joke_in_korean = translate_joke_to_korean(joke_in_english)
print("유머 (한국어 번역):", joke_in_korean)
joke_in_korean = translate_joke_to_korean(joke_in_english, lang="ja")
print("유머 (일본어 번역):", joke_in_korean)