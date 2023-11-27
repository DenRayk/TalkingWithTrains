import requests


class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.hash = None
        self.zug_1: 16391
        self.zug_2: 16389
        self.zug_3: 16392
        self.zug_4: 16390
        self.get_hash()

    def get_hash(self):
        response = self.send_get_request("general/hash")
        print(f"Hash: {response}")
        self.hash = response

    def send_get_request(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"

        if hash is None:
            response = requests.get(url, params=params)
        else:
            response = requests.get(url, params=params, headers={"x-can-hash": self.hash})

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
