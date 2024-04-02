import json

import services.http_client as http_client

import speech_control.train_commands as train_commands
import speech_control.accessories_commands as accessories_commands
import speech_control.part_designations as part_designations


def generate_commands(commands):
    # Dynamically create commands for trains
    for train_name, train_id in part_designations.trains.items():
        # Commands for train speed
        for action, value in train_commands.train_speed_commands.items():
            command_name = f"{train_name} {action}"
            commands[command_name] = lambda tid=train_id, val=value: http_client.set_train_speed(tid, val)
        # Commands for train direction
        for action, value in train_commands.train_direction_commands.items():
            command_name = f"{train_name} {action}"
            commands[command_name] = lambda tid=train_id, val=value: http_client.set_train_direction(tid, val)
        # Commands for train direction with speed
        for action, value in train_commands.train_direction_speed_commands.items():
            command_name = f"{train_name} {action}"
            commands[command_name] = lambda tid=train_id, val=value: http_client.set_train_direction_with_speed(tid,
                                                                                                                val)
        # Commands for train adding speed
        for action, value in train_commands.train_add_speed_commands.items():
            command_name = f"{train_name} {action}"
            commands[command_name] = lambda tid=train_id, val=value: http_client.add_train_speed(tid, val)

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

    # Dynamically create commands for accessory three way turnouts
    for accessory_name, accessory_id in part_designations.accessories_three_way_turnouts.items():
        # Commands for accessories three way turnouts
        for action, value in accessories_commands.accessories_three_way_turnouts_commands.items():
            command_name = f"{accessory_name} {action}"
            commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_three_way_turnouts_status(aid, val)


def generate_grammar(commands):
    words = []
    for command in commands:
        words.extend(command.split())

    unique_words = list(set(words))
    unique_words.append("[unk]")
    unique_words.append("modellbahn")

    unique_words.sort()

    with open('grammar.json', 'w', encoding='utf-8') as f:
        json.dump(unique_words, f, ensure_ascii=False, indent=0)