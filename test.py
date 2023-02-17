import time
import requests

url = "http://localhost"  # replace with the URL of your server
interval = 0.01  # request interval in seconds

while True:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Successful request at {time.time()}")
    else:
        print(
            f"Request failed with status code {response.status_code} at {time.time()}"
        )
    time.sleep(interval)
