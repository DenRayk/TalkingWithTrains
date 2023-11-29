import json
import config
import services.http_client as http_client

"""
Initialer Test:
System Start/Alle stop
System Stop
Fahre ZugX vorwärts
Fahre ZugX rückwärts
ZugX fahre Geschwindidkeit y
"""


def extract_activity(prompt_text):
    prompt_text_json = json.loads(prompt_text)

    match prompt_text_json["text"]:

        # System Befehle bisher nicht in der API
        case "system start":
            drive_all()
        case "system stop":
            stop_all()

        # Züge Richtung
        case "fahre zug eins geradeaus" | "fahre zug eins vorwärts" | "zug eins fahre geradeaus" | "zug eins fahre vorwärts":
            http_client.set_train_direction("zug_1", "Forwards")
        case "fahre zug eins rückwärts" | "zug eins fahre rückwärts":
            http_client.set_train_direction("zug_1", "Backwards")
        case "fahre zug zwei geradeaus" | "fahre zug zwei vorwärts" | "zug zwei fahre geradeaus" | "zug zwei fahre vorwärts":
            http_client.set_train_direction("zug_2", "Forwards")
        case "fahre zug zwei rückwärts" | "zug zwei fahre rückwärts":
            http_client.set_train_direction("zug_2", "Backwards")
        case "fahre zug drei geradeaus" | "fahre zug drei vorwärts" | "zug drei fahre geradeaus" | "zug drei fahre vorwärts":
            http_client.set_train_direction("zug_3", "Forwards")
        case "fahre zug drei rückwärts" | "zug drei fahre rückwärts":
            http_client.set_train_direction("zug_3", "Backwards")
        case "fahre zug vier geradeaus" | "fahre zug vier vorwärts" | "zug vier fahre geradeaus" | "zug vier fahre vorwärts":
            http_client.set_train_direction("zug_4", "Forwards")
        case "fahre zug vier rückwärts" | "zug vier fahre rückwärts":
            http_client.set_train_direction("zug_4", "Backwards")

        # Züge anhalten
        case "zug eins stop" | "zug eins halte an":
            http_client.set_train_speed("zug_1", 0)
        case "zug zwei stop" | "zug zwei halte an":
            http_client.set_train_speed("zug_2", 0)
        case "zug drei stop" | "zug drei halte an":
            http_client.set_train_speed("zug_3", 0)
        case "zug vier stop" | "zug vier halte an":
            http_client.set_train_speed("zug_4", 0)

        case _:
            print('Befehl nicht gefunden')


def drive_all():
    print('driving all')


def stop_all():
    print('stopping all')


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
