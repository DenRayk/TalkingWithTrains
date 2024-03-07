import json

from fuzzywuzzy import process
import services.http_client as http_client

commands = {
    "system start": http_client.drive_all,
    "system stop": http_client.stop_all,
}

train_commands = {
    "geradeaus": "forwards",
    "fahre geradeaus": "forwards",
    "vorwärts": "Forwards",
    "fahre vorwärts": "Forwards",
    "rückwärts": "Backwards",
    "fahre rückwärts": "Backwards",
    "stop": 0,
    "halte an": 0,
    "fahre los": 500,
    "fahre so schnell wie möglich": 1000,
}

trains = {
    "zug eins": "zug_1",
    "zug zwei": "zug_2",
    "zug drei": "zug_3",
    "zug vier": "zug_4",
}

for train_name, train_id in trains.items():
    for action, value in train_commands.items():
        command_name = f"{train_name} {action}"
        if isinstance(value, str):
            commands[command_name] = lambda tid=train_id, val=value: http_client.set_train_direction(tid, val)
        else:
            commands[command_name] = lambda tid=train_id, val=value: http_client.set_train_speed(tid, val)


def extract_activity(prompt_text):
    command = json.loads(prompt_text)["text"]

    best_match, score = process.extractOne(command, commands.keys())

    if score > 70:
        print(f'User Input: "{command}"\n'
              f'Execute: "{best_match}" ({score}%)')
        commands[best_match]()
        return True
    else:
        print('Befehl nicht gefunden')
        return False
