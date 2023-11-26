import requests


class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.hash = None

    def get_hash(self, name):
        response = self.send_get_request("hash", {"name": name})
        self.hash = response["hash"]

    def send_get_request(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Fehler bei der Anfrage: {response.status_code}")
            return None

    def send_post_request(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data)

        if response.status_code == 201:
            return response.json()
        else:
            print(f"Fehler bei der Anfrage: {response.status_code}")
            return None

