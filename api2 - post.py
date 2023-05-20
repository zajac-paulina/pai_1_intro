import requests

url = "https://httpbin.org/post"
data = {"name": "natalia"}

try:
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()

    response_data = response.json()
    print("odpowiedź http:", response.status_code)
    print("odpowiedź json:")
    print(response_data)

except requests.exceptions.RequestException as blad:
    print("wystąpił błąd", blad)
