import json
import os

import services.http_client as http_client

import speech_control.command_generation.train_commands as train_commands
import speech_control.command_generation.accessories_commands as accessories_commands
import speech_control.command_generation.part_designations as part_designations


def generate_commands(commands):
    # Dynamically create commands for trains
    for train_name, train_id in part_designations.trains.items():
        # Commands for train speed
        for action, value in train_commands.train_speed_commands.items():
            command_name = f"{train_name} {action}"
            commands[command_name] = lambda tid=train_id, val=value: http_client.set_train_speed(tid, val)
        # Commands for train direction with speed
        for action, value in train_commands.train_direction_speed_commands.items():
            command_name = f"{train_name} {action}"
            commands[command_name] = lambda tid=train_id, val=value: http_client.set_train_direction_with_speed(tid, val)
        # Commands for train adding speed
        for action, value in train_commands.train_add_speed_commands.items():
            command_name = f"{train_name} {action}"
            commands[command_name] = lambda tid=train_id, val=value: http_client.add_train_speed(tid, val)
        # Commands for train functions
        for action, value in train_commands.train_function_commands.items():
            command_name = f"{train_name} {action}"
            if "hupe" in command_name:
                commands[command_name] = lambda tid=train_id, val=value: http_client.set_train_function_on_off(tid, val, 2)
            elif any(keyword in command_name for keyword in ["aus", "ausschalten", "deaktivieren"]):
                if not(train_id == "zug_1" and "rauch" in command_name):
                    commands[command_name] = lambda tid=train_id, val=value: http_client.set_train_function_off(tid, val)
                else:
                    print("NOT IN: " + command_name)
            else:
                if train_id == "zug_1" and "rauch" in command_name:
                    commands[command_name] = lambda tid=train_id: http_client.set_train_function_on_off(tid, 14, 1)
                    print(command_name)
                else:
                    commands[command_name] = lambda tid=train_id, val=value: http_client.set_train_function_on(tid, val)


    # Dynamically create commands for accessory signals
    for accessory_name, accessory_id in part_designations.accessories_light_signals.items():
        # Commands for accessories light
        for action, value in accessories_commands.accessories_light_commands.items():
            command_name = f"{accessory_name} {action}"
            commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_status(aid, val)

    # Dynamically create commands for accessory right turnouts
    for accessory_name, accessory_id in part_designations.accessories_right_turnouts.items():
        # Commands for accessories right turnouts
        for action, value in accessories_commands.accessories_general_turnouts_commands.items():
            command_name = f"{accessory_name} {action}"
            commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_status(aid, val)
        for action, value in accessories_commands.accessories_right_turnouts_commands.items():
            command_name = f"{accessory_name} {action}"
            commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_status(aid, val)

    # Dynamically create commands for accessory left turnouts
    for accessory_name, accessory_id in part_designations.accessories_left_turnouts.items():
        # Commands for accessories left turnouts
        for action, value in accessories_commands.accessories_general_turnouts_commands.items():
            command_name = f"{accessory_name} {action}"
            commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_status(aid, val)
        for action, value in accessories_commands.accessories_left_turnouts_commands.items():
            command_name = f"{accessory_name} {action}"
            commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_status(aid, val)

    # Dynamically create commands for accessory uncoupling tracks
    for accessory_name, accessory_id in part_designations.accessories_uncoupling_tracks.items():
        # Commands for accessories uncoupling tracks
        for action, value in accessories_commands.accessories_uncoupling_tracks_commands.items():
            command_name = f"{accessory_name} {action}"
            commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_status(aid, val)

    # Dynamically create commands for accessory three-way turnouts
    for accessory_name, accessory_id in part_designations.accessories_three_way_turnouts.items():
        # Commands for accessories three-way turnouts
        for action, value in accessories_commands.accessories_three_way_turnouts_commands.items():
            command_name = f"{accessory_name} {action}"
            commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_three_way_turnouts_status(aid, val)


def generate_grammar(commands):
    words = set()
    for command in commands:
        words.update(command.split())

    words.update(["[unk]", "modellbahn"])
    unique_words = sorted(words)

    # Pfad zur übergeordneten Ebene des aktuellen Skriptverzeichnisses
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    # Konstruiere den Pfad zur grammar.json-Datei im übergeordneten Verzeichnis
    file_path = os.path.join(parent_dir, 'grammar.json')

    if os.path.exists(file_path) and os.access(file_path, os.W_OK):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(unique_words, f, ensure_ascii=False, indent=4)
    else:
        print(f"The file {file_path} does not exist or is not writable.")
