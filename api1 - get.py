import requests

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"

try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    print("dane:", data)

except requests.exceptions.RequestException as blad:
    print("wystąpił błąd", blad)
