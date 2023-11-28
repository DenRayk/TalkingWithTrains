# TODO: implement activities for the trains
import json

zug_1: 16391
zug_2: 16389
zug_3: 16392
zug_4: 16390


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
        case "system start":
            drive_all()
        case "system stop":
            stop_all()
        case "fahre zug eins geradeaus":
            drive_forward(zug_1)
        case "fahre zug eins zurück":
            drive_backwards(zug_1)
        case "zug eins stop":
            drive_stop(zug_1)
        case _:
            print('Befehl nicht gefunden')


def drive_all():
    print('driving all')


def stop_all():
    print('stopping all')


def drive_forward(train_id):
    print(train_id, 'driving forward')


def drive_backwards(train_id):
    print(train_id, ' driving backwards')


def drive_stop(train_id):
    print(train_id, ' Stop')



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
