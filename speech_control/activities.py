import json

from fuzzywuzzy import process
import services.http_client as http_client


import speech_control.command_generation.generation as generation

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

# Dynamically create commands
generation.generate_commands(commands)

# Generate grammar with all unique words
#generation.generate_grammar(commands.keys())

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



