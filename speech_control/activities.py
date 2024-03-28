import json

from fuzzywuzzy import process
import services.http_client as http_client

import train_commands
import accessories_commands
import part_designations

commands = {
    #System commands
    "system start": lambda :http_client.set_system_mode("Go"),
    "system starten": lambda: http_client.set_system_mode("Go"),
    "system aktiviert": lambda: http_client.set_system_mode("Go"),
    "system aktivieren": lambda: http_client.set_system_mode("Go"),
    "start system": lambda: http_client.set_system_mode("Go"),
    "starte system": lambda: http_client.set_system_mode("Go"),
    "aktiviere system": lambda: http_client.set_system_mode("Go"),

    "system stop": lambda :http_client.set_system_mode("Stop"),
    "system stoppen": lambda :http_client.set_system_mode("Stop"),
    "stop system": lambda: http_client.set_system_mode("Stop"),
    "stoppe system": lambda: http_client.set_system_mode("Stop"),
    "beende system": lambda: http_client.set_system_mode("Stop"),

    "system halt": lambda :http_client.set_system_mode("Halt"),
    "system anhalten": lambda: http_client.set_system_mode("Halt"),
    "halt system": lambda: http_client.set_system_mode("Halt"),
    "halte system": lambda: http_client.set_system_mode("Halt"),

    "system reset": lambda :http_client.set_system_mode("Reset"),
    "system zurücksetzen": lambda: http_client.set_system_mode("Reset"),
    "reset system": lambda: http_client.set_system_mode("Reset"),
    "setze system zurück": lambda: http_client.set_system_mode("Reset"),
    "zurücksetzen system": lambda: http_client.set_system_mode("Reset"),
}

#Dynamically create commands for trains
for train_name, train_id in part_designations.trains.items():
    #Commands for train speed
    for action, value in train_commands.train_speed_commands.items():
        command_name = f"{train_name} {action}"
        commands[command_name] = lambda tid=train_id, val=value: http_client.set_train_speed(tid, val)
    #Commands for train direction
    for action, value in train_commands.train_direction_commands.items():
        command_name = f"{train_name} {action}"
        commands[command_name] = lambda tid=train_id, val=value: http_client.set_train_direction(tid, val)
    #Commands for train direction with speed
    for action, value in train_commands.train_direction_speed_commands.items():
        command_name = f"{train_name} {action}"
        commands[command_name] = lambda tid=train_id, val=value: http_client.set_train_direction_with_speed(tid, val)
    #Commands for train adding speed
    for action, value in train_commands.train_add_speed_commands.items():
        command_name = f"{train_name} {action}"
        commands[command_name] = lambda tid=train_id, val=value: http_client.add_train_speed(tid, val)

#Dynamically create commands for accessory signals
for accessory_name, accessory_id in part_designations.accessories_light_signals.items():
    #Commands for accessories light
    for action, value in accessories_commands.accessories_light_commands.items():
        command_name = f"{accessory_name} {action}"
        commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_status(aid, val)

#Dynamically create commands for accessory right turnouts
for accessory_name, accessory_id in part_designations.accessories_right_turnouts.items():
    #Commands for accessories right turnouts
    for action, value in accessories_commands.accessories_general_turnouts_commands.items():
        command_name = f"{accessory_name} {action}"
        commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_status(aid, val)
    for action, value in accessories_commands.accessories_right_turnouts_commands.items():
        command_name = f"{accessory_name} {action}"
        commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_status(aid, val)

#Dynamically create commands for accessory left turnouts
for accessory_name, accessory_id in part_designations.accessories_left_turnouts.items():
    #Commands for accessories left turnouts
    for action, value in accessories_commands.accessories_general_turnouts_commands.items():
        command_name = f"{accessory_name} {action}"
        commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_status(aid, val)
    for action, value in accessories_commands.accessories_left_turnouts_commands.items():
        command_name = f"{accessory_name} {action}"
        commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_status(aid, val)

#Dynamically create commands for accessory uncoupling tracks
for accessory_name, accessory_id in part_designations.accessories_uncoupling_tracks.items():
    #Commands for accessories uncoupling tracks
    for action, value in accessories_commands.accessories_uncoupling_tracks_commands.items():
        command_name = f"{accessory_name} {action}"
        commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_status(aid, val)

#Dynamically create commands for accessory three way turnouts
for accessory_name, accessory_id in part_designations.accessories_three_way_turnouts.items():
    #Commands for accessories three way turnouts
    for action, value in accessories_commands.accessories_three_way_turnouts_commands.items():
        command_name = f"{accessory_name} {action}"
        commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_three_way_turnouts_status(aid, val)

#for command in commands.keys():
#    print(command)
print(f"Total of {len(commands)} commands loaded")


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
