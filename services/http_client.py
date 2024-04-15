import time

import requests
import config

base_url = config.base_url


def get_hash():
    response = send_get_request("general/hash")
    if response is None:
        return
    print(f"Hash: {response.json()}")
    config.x_can_hash = str(response.json())


def send_get_request(endpoint, params=None):
    url = f"{base_url}/{endpoint}"

    try:
        if hash is None:
            response = requests.get(url, params=params)
        else:
            response = requests.get(url, params=params, headers={"x-can-hash": config.x_can_hash})

        if response.status_code in [200, 201, 202, 203, 204]:
            return response
        else:
            print(f"Fehler bei der Anfrage: {response.status_code}")
            return None
    except requests.exceptions.ConnectionError:
        print("Connection to server failed")
        return None


def send_post_request(endpoint, data=None):
    url = f"{base_url}/{endpoint}"

    try:
        response = requests.post(url, json=data, headers={"x-can-hash": config.x_can_hash})

        if response.status_code in [200, 201, 202, 203, 204]:
            return response
        else:
            print(f"Fehler bei der Anfrage: {response.status_code}")
            return None
    except requests.exceptions.ConnectionError:
        print("Connection to server failed")
        return None


def set_train_direction(zug, direction):
    response = send_post_request(f"lok/{config.trains[zug]}/direction", data={"direction": direction})
    if response:
        print(f"Zug {zug} fährt {direction}")
    return response


def set_train_speed(zug, speed):
    response = send_post_request(f"lok/{config.trains[zug]}/speed", data={"speed": speed})
    if response:
        print(f"Zug {zug} fährt mit {speed / 10}")
    return response


def set_train_function_on(zug, function):
    response = send_post_request(f"lok/{config.trains[zug]}/function/{function}", data={"value": 1})
    if response:
        print(f"Zug {zug} {function}")
    return response


def set_train_function_off(zug, function):
    response = send_post_request(f"lok/{config.trains[zug]}/function/{function}", data={"value": 0})
    if response:
        print(f"Zug {zug} {function}")
    return response


def set_train_function_on_off(zug, function, sleep_time):
    responses = []
    responses.append(set_train_function_on(zug, function))

    time.sleep(sleep_time)
    responses.append(set_train_function_off(zug, function))

    return responses or None


def train_function_decouple(sleep_time):
    #Hartkodiert für zug_1 entkoppeln
    responses = []
    responses.append(set_train_function_on("zug_1", 1))
    responses.append(set_train_function_on("zug_1", 4))

    time.sleep(sleep_time)
    responses.append(set_train_function_off("zug_1", 1))
    responses.append(set_train_function_off("zug_1", 4))

    return responses or None


def set_accessory_status(accessory, status):
    response = send_post_request(f"accessory/{config.accessories[accessory]}",
                                 data={"position": int(status), "power": 1, "value": 1})
    if response:
        print(f"Accessory {accessory} set to {status}")
    return response


def set_accessory_three_way_turnouts_status(accessory, direction):
    actions = {
        ("W 1", "Links"): [("W 1 DREI LI/MI", False)],
        ("W 1", "Mitte"): [("W 1 DREI LI/MI", True), ("W 1 DREI RE/MI", True)],
        ("W 1", "Rechts"): [("W 1 DREI LI/MI", True), ("W 1 DREI RE/MI", False)],
        ("W 5", "Links"): [("W 5 DREI LI/MI", False)],
        ("W 5", "Mitte"): [("W 5 DREI LI/MI", True), ("W 5 DREI RE/MI", True)],
        ("W 5", "Rechts"): [("W 5 DREI LI/MI", True), ("W 5 DREI RE/MI", False)]
    }

    accessory_actions = actions.get((accessory, direction))

    if not accessory_actions:
        return None

    responses = []
    for accessory_action in accessory_actions:
        accessory_name, position = accessory_action
        response = send_post_request(f"accessory/{config.accessories[accessory_name]}",
                                     data={"position": int(position), "power": 1, "value": 1})
        if response is None:
            return None
        responses.append(response)

    return responses


def get_train_speed(zug):
    response = send_get_request(f"lok/{config.trains[zug]}/speed")
    if response:
        print(f"Zug {zug} fährt mit {response.json()['speed'] / 10}")
    return response


def get_train_direction(zug):
    response = send_get_request(f"lok/{config.trains[zug]}/direction")
    if response:
        print(f"Zug {zug} fährt {response.json()['direction']}")
    return response


def set_train_direction_with_speed(zug, direction):
    current_speed_response = get_train_speed(zug)
    if current_speed_response is not None:
        current_speed = current_speed_response.json()['speed']
        return set_train_direction(zug, direction), set_train_speed(zug, current_speed)
    return None


def add_train_speed(zug, speed):
    current_speed_response = get_train_speed(zug)
    if current_speed_response is not None:
        current_speed = current_speed_response.json()['speed']
        new_speed = max(0, min(1000, current_speed + speed))
        return set_train_speed(zug, new_speed)
    return None


def drive_all():
    responses = []
    for zug in config.trains:
        response = set_train_speed(zug, 500)
        if response is not None:
            responses.append(response)
    return responses or None


def stop_all():
    responses = []
    for zug in config.trains:
        response = set_train_speed(zug, 0)
        if response is not None:
            responses.append(response)
    return responses or None


def set_system_mode(mode):
    try:
        url = f"{base_url}/system/status?status={mode}"
        response = requests.post(url, headers={"x-can-hash": config.x_can_hash})
        if response.status_code in [200, 201, 202, 203, 204]:
            print(f"System mode set to {mode}")
            return response
        return None
    except requests.exceptions.ConnectionError:
        print("Connection to server failed")
        return None
