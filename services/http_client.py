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
    print(f"Zug {zug} fährt {direction}")
    return response


def set_train_speed(zug, speed):
    response = send_post_request(f"lok/{config.trains[zug]}/speed", data={"speed": speed})
    print(f"Zug {zug} fährt mit {speed / 10}")
    return response


def set_train_function(zug, function):
    response = send_post_request(f"lok/{config.trains[zug]}/function/{config.functions_crossrail[function]}")
    print(f"Zug {zug} {function}")
    return response


def set_accessory_status(accessory, status):
    response = send_post_request(f"accessory/{config.accessories[accessory]}", data={"position": status})
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
        response = send_post_request(f"accessory/{config.accessories[accessory_name]}", data={"position": position})
        responses.append(response)

    return responses


def get_train_speed(zug):
    response = send_get_request(f"lok/{config.trains[zug]}/speed")
    print(f"Zug {zug} fährt mit {response.json()['speed'] / 10}")
    return response


def get_train_direction(zug):
    response = send_get_request(f"lok/{config.trains[zug]}/direction")
    print(f"Zug {zug} fährt {response.json()['direction']}")
    return response


def set_train_direction_with_speed(zug, direction):
    currentSpeed = get_train_speed(zug).json()['speed']
    set_train_direction(zug, direction)
    set_train_speed(zug, currentSpeed)


def add_train_speed(zug, speed):
    currentSpeed = get_train_speed(zug).json()['speed']
    set_train_speed(zug, currentSpeed + speed)


def drive_all():
    for zug in config.trains:
        set_train_speed(zug, 50)


def stop_all():
    for zug in config.trains:
        set_train_speed(zug, 0)


def set_system_mode(mode):
    try:
        url = f"{base_url}/system/status?status={mode}"
        response = requests.post(url, headers={"x-can-hash": config.x_can_hash})
        print(f"System mode set to {mode}")
        return response
    except requests.exceptions.ConnectionError:
        print("Connection to server failed")
        return None