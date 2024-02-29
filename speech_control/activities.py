import json

from fuzzywuzzy import process
import services.http_client as http_client

commands = {
    # System control commands
    "system start": lambda: http_client.drive_all(),
    "system stop": lambda: http_client.stop_all(),

    # Train direction commands
    # Zug 1
    "fahre zug eins geradeaus": lambda: http_client.set_train_direction_forwards("zug_1"),
    "fahre zug eins vorwärts": lambda: http_client.set_train_direction_forwards("zug_1"),
    "zug eins fahre geradeaus": lambda: http_client.set_train_direction_forwards("zug_1"),
    "zug eins fahre vorwärts": lambda: http_client.set_train_direction_forwards("zug_1"),
    "fahre zug eins rückwärts": lambda: http_client.set_train_direction_backwards("zug_1"),
    "zug eins fahre rückwärts": lambda: http_client.set_train_direction_backwards("zug_1"),

    # Zug 2
    "fahre zug zwei geradeaus": lambda: http_client.set_train_direction_forwards("zug_2"),
    "fahre zug zwei vorwärts": lambda: http_client.set_train_direction_forwards("zug_2"),
    "zug zwei fahre geradeaus": lambda: http_client.set_train_direction_forwards("zug_2"),
    "zug zwei fahre vorwärts": lambda: http_client.set_train_direction_forwards("zug_2"),
    "fahre zug zwei rückwärts": lambda: http_client.set_train_direction_backwards("zug_2"),
    "zug zwei fahre rückwärts": lambda: http_client.set_train_direction_backwards("zug_2"),

    # Zug 3
    "fahre zug drei geradeaus": lambda: http_client.set_train_direction_forwards("zug_3"),
    "fahre zug drei vorwärts": lambda: http_client.set_train_direction_forwards("zug_3"),
    "zug drei fahre geradeaus": lambda: http_client.set_train_direction_forwards("zug_3"),
    "zug drei fahre vorwärts": lambda: http_client.set_train_direction_forwards("zug_3"),
    "fahre zug drei rückwärts": lambda: http_client.set_train_direction_backwards("zug_3"),
    "zug drei fahre rückwärts": lambda: http_client.set_train_direction_backwards("zug_3"),

    # Zug 4
    "fahre zug vier geradeaus": lambda: http_client.set_train_direction_forwards("zug_4"),
    "fahre zug vier vorwärts": lambda: http_client.set_train_direction_forwards("zug_4"),
    "zug vier fahre geradeaus": lambda: http_client.set_train_direction_forwards("zug_4"),
    "zug vier fahre vorwärts": lambda: http_client.set_train_direction_forwards("zug_4"),
    "fahre zug vier rückwärts": lambda: http_client.set_train_direction_backwards("zug_4"),
    "zug vier fahre rückwärts": lambda: http_client.set_train_direction_backwards("zug_4"),

    # Train speed commands
    # Zug 1
    "zug eins stop": lambda: http_client.set_train_speed("zug_1", 0),
    "zug eins halte an": lambda: http_client.set_train_speed("zug_1", 0),
    "zug eins fahre los": lambda: http_client.set_train_speed("zug_1", 500),
    "zug eins fahre so schnell wie möglich": lambda: http_client.set_train_speed("zug_1", 1000),

    # Zug 2
    "zug zwei stop": lambda: http_client.set_train_speed("zug_2", 0),
    "zug zwei halte an": lambda: http_client.set_train_speed("zug_2", 0),
    "zug zwei fahre los": lambda: http_client.set_train_speed("zug_2", 500),
    "zug zwei fahre so schnell wie möglich": lambda: http_client.set_train_speed("zug_2", 1000),

    # Zug 3
    "zug drei stop": lambda: http_client.set_train_speed("zug_3", 0),
    "zug drei halte an": lambda: http_client.set_train_speed("zug_3", 0),
    "zug drei fahre los": lambda: http_client.set_train_speed("zug_3", 500),
    "zug drei fahre so schnell wie möglich": lambda: http_client.set_train_speed("zug_3", 1000),

    # Zug 4
    "zug vier stop": lambda: http_client.set_train_speed("zug_4", 0),
    "zug vier halte an": lambda: http_client.set_train_speed("zug_4", 0),
    "zug vier fahre los": lambda: http_client.set_train_speed("zug_4", 50),
    "zug vier fahre so schnell wie möglich": lambda: http_client.set_train_speed("zug_4", 1000),
}


def extract_activity(prompt_text):
    command = json.loads(prompt_text)["text"]

    best_match, score = process.extractOne(command, commands.keys())

    if score > 70:
        commands[command]()
    else:
        print('Befehl nicht gefunden')


"""
Mögliche Befehle
ZugX fahre
ZugX vorwärts
ZugX rückwärts
ZugX fahre geradeaus
ZugX fahre vorwärts
ZugX fahre rückwärts
ZugX stop
ZugX halte an
ZugX Geschwindidkeit x
ZugX fahre Geschwindigkeit x
ZugX fahre vorwärts mit Geschwindigkeit x
ZugX fahre gerade aus mit Geschwindigkeit x
ZugX fahre rückwärts mit Geschwindigkeit x
ZugX fahre vorwärts nach Bahnhof x
ZugX fahre rückwärts nach Bahnhof x
ZugX fahre vorwärts zu Gleis X
ZugX fahre rückwärts zu Gleis X
ZugX fahre vorwärts zu abschnitt X
ZugX fahre rückwärts zu abschnitt X
Stelle Weiche x
Toggle Weiche x
Alle stop
stop
Weiter
Alle fahren
....
"""
