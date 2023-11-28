import requests


class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.hash = None

        self.trains = {
            "zug_1": 16391,
            "zug_2": 16389,
            "zug_3": 16392,
            "zug_4": 16390,
        }

        self.functionsCrossrail = {
            "Licht": 1,
            "Rauch": 2,
            "Betriebsgeräusche": 3,
            "Hupe 1": 4,
            "Gewicht": 5,
            "Anfahrgeräusche": 6,
            "Innenlicht": 7,
            "Hupe 2": 8,
            "Innenlicht / Vorne": 9,
            "Lüftungsgeräusche": 10,
            "Kück - Sound": 11,
            "Kompressor": 12,
            "Licht unten": 13,
            "Licht unten 2": 14,
            "Fake Anfahrgeräusche": 15,
            "Hupe 3": 16,
            "Hupe 4": 17,
            "Turtle": 18,
            "Kleines Licht": 19,
            "Großes Licht": 20,
            "Luft ablassen": 21,
            "Motorgeräusche": 22,
            "Abkoppelsound 1": 23,
            "FULL Sound": 24,
            "Abkoppelsound 2": 25,
            "ALARM 1": 26,
            "ALARM 2": 27,
            "Türen": 28
        }

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
        response = requests.post(url, json=data, headers={"x-can-hash": self.hash})

        if response.status_code == 201:
            return response.json()
        else:
            print(f"Fehler bei der Anfrage: {response.status_code}")
            return None

    def set_direction(self, zug, direction):
        response = self.send_post_request(f"lok/{self.trains[zug]}/direction", data={"direction": direction})
        print(f"Zug {zug} fährt {direction}")

    def set_speed(self, zug, speed):
        response = self.send_post_request(f"lok/{self.trains[zug]}/speed", data={"speed": speed})
        print(f"Zug {zug} fährt mit {speed / 10}")

    def set_function(self, zug, function):
        response = self.send_post_request(f"lok/{self.trains[zug]}/function/{self.functionsCrossrail[function]}")
        print(f"Zug {zug} {function}")
