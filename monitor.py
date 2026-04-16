import requests
import datetime

try:
    with(open('urls.txt', 'r')) as f:
        urls = f.read().splitlines()
except FileNotFoundError:
    print("Error: urls.txt file not found.")
    exit(1)

for url in urls:
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, timeout=10, headers=headers)
        if response.status_code == 200:
            print(f"{datetime.datetime.now()}: {url} is up.")
        else:
            print(f"{datetime.datetime.now()}: {url} is down. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{datetime.datetime.now()}: {url} is down. Error: {e}\n")
        with open('errores.log', 'a') as log_file:
            log_file.write(f"{datetime.datetime.now()}: {url} is down. Error: {e}\n")
