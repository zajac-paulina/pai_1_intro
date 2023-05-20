import requests
import jmespath

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"
response = requests.get(url)
json_data = response.json()

members = json_data["members"]
for member in members:
    print(member["name"])

for i in range(len(members)):
    search_query = f"members[{i}].name"
    print(jmespath.search(search_query, json_data))
