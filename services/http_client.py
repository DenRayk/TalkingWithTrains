import requests
import config

base_url = config.base_url


def get_hash():
    response = send_get_request("general/hash")
    print(f"Hash: {response}")
    config.x_can_hash = str(response)


def send_get_request(endpoint, params=None):
    url = f"{base_url}/{endpoint}"

    if hash is None:
        response = requests.get(url, params=params)
    else:
        response = requests.get(url, params=params, headers={"x-can-hash": config.x_can_hash})

    if response.status_code in [200, 201, 202, 203, 204]:
        return response.json()
    else:
        print(f"Fehler bei der Anfrage: {response.status_code}")
        return None


def send_post_request(endpoint, data=None):
    url = f"{base_url}/{endpoint}"
    response = requests.post(url, json=data, headers={"x-can-hash": config.x_can_hash})

    if response.status_code in [200, 201, 202, 203, 204]:
        return response.json()
    else:
        print(f"Fehler bei der Anfrage: {response.status_code}")
        return None


def set_train_direction(zug, direction):
    response = send_post_request(f"lok/{config.trains[zug]}/direction", data={"direction": direction})
    print(f"Zug {zug} fährt {direction}")


def set_train_speed(zug, speed):
    response = send_post_request(f"lok/{config.trains[zug]}/speed", data={"speed": speed})
    print(f"Zug {zug} fährt mit {speed / 10}")


def set_train_function(zug, function):
    response = send_post_request(f"lok/{config.trains[zug]}/function/{config.functions_crossrail[function]}")
    print(f"Zug {zug} {function}")


def get_train_speed(zug):
    response = send_get_request(f"lok/{config.trains[zug]}/speed")
    print(f"Zug {zug} fährt mit {response['speed'] / 10}")
    return response


def get_train_direction(zug):
    response = send_get_request(f"lok/{config.trains[zug]}/direction")
    print(f"Zug {zug} fährt {response['direction']}")
    return response
