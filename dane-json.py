import requests
import jmespath

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    for member in data.get("members", []):
        print(member.get("name"))

    for i in range(len(data.get("members", []))):
        search_expression = f"members[{i}].name"
        print(jmespath.search(search_expression, data))

except requests.exceptions.RequestException as blad:
    print("wystąpił błąd", blad)
