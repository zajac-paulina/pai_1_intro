import requests
from requests.exceptions import RequestException, ReadTimeout
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

url = "https://httpbin.org/delay/2"
data = {"name": "natalia"}
timeout = 1
max_retries = 3
backoff_factor = 0.5

try:
    headers = {"Content-Type": "application/json"}
    session = requests.Session()
    retries = Retry(total=max_retries, backoff_factor=backoff_factor)
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    response = session.post(url, json=data, headers=headers, timeout=timeout)
    response.raise_for_status()

    response_data = response.json()
    print("odpowiedź http:", response.status_code)
    print("odpowiedź json:")
    print(response_data)

except ReadTimeout:
    print("przekroczono limit czasowy")

except RequestException as blad:
    print("wystąpił błąd", blad)
