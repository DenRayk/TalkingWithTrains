import json

from fuzzywuzzy import process
import services.http_client as http_client

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

    #Decoupling
    "entkuppeln": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "entkupplung": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "entkoppel den wagen": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "entkopple wagen": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "wagen entkoppeln": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "wagen aushängen": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "anhänger entkoppeln": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "anhänger aushängen": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "güterwagen entkoppeln": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "güterwagen aushängen": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "entkuppel den anhänger": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "entkuppel den güterwagen": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "entkuppel den wagen": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "hänge den anhänger aus": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "hänge den güterwagen aus": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "hänge den wagen aus": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "trenne den anhänger": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "trenne den güterwagen": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "trenne den wagen": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "anhänger losmachen": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "güterwagen losmachen": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "wagen losmachen": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "kuppel den anhänger ab": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "kuppel den güterwagen ab": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "kuppel den wagen ab": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "kuppel ab": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "trennung durchführen": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "löse den wagen vom Zug": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "löse den wagen von der bahn": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "wagen von zug abkoppeln": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
    "löse verbindung zwischen wagen und zug": lambda: http_client.set_uncoupling_track("entkupplungsgleis_1"),
}

custom_switch_commands = {
    "schalte",
    "schalten",
    "wechseln",
    "wechsel",
    "stellen",
    "stelle",
    "bewegen",
    "bewege",
}

increaseTrainSpeed = 200
reduceTrainSpeed = -200
train_custom_speed_commands = {
    "schneller": increaseTrainSpeed,
    "fahre schneller": increaseTrainSpeed,
    "laufe schneller": increaseTrainSpeed,
    "bewege dich schneller": increaseTrainSpeed,
    "geschwindigkeit erhöhe": increaseTrainSpeed,
    "schneller fahren": increaseTrainSpeed,
    "schneller bewegen": increaseTrainSpeed,
    "schneller voran": increaseTrainSpeed,
    "schneller nach vorne": increaseTrainSpeed,
    "erhöhe geschwindigkeit": increaseTrainSpeed,
    "beschleunige": increaseTrainSpeed,
    "tempo erhöhen": increaseTrainSpeed,
    "erhöhe tempo": increaseTrainSpeed,

    "langsamer": reduceTrainSpeed,
    "fahre langsamer": reduceTrainSpeed,
    "laufe langsamer": reduceTrainSpeed,
    "bewege dich langsamer": reduceTrainSpeed,
    "geschwindigkeit verringere": reduceTrainSpeed,
    "langsamer fahren": reduceTrainSpeed,
    "langsamer bewegen": reduceTrainSpeed,
    "langsamer voran": reduceTrainSpeed,
    "langsamer nach vorne": reduceTrainSpeed,
    "verringere geschwindigkeit": reduceTrainSpeed,
    "verlangsamen": reduceTrainSpeed,
    "tempo verringern": reduceTrainSpeed,
    "verringere tempo": reduceTrainSpeed,
}

train_standard_commands = {
    #Direction forwards
    "geradeaus": "Forwards",
    "fahre geradeaus": "Forwards",
    "richtig geradeaus": "Forwards",
    "in richtung geradeaus": "Forwards",
    "fahre in richtung geradeaus": "Forwards",
    "fahre in die richtung geradeaus": "Forwards",
    "in richtung geradeaus fahren": "Forwards",
    "in richtung geradeaus bewegen": "Forwards",
    "bewege dich geradeaus": "Forwards",
    "gehe geradeaus": "Forwards",
    "geradeaus fahren": "Forwards",
    "gehe voran geradeaus": "Forwards",
    "setze den weg geradeaus": "Forwards",
    "setze den pfad geradeaus": "Forwards",
    "setze den kurs geradeaus": "Forwards",
    "setze die route geradeaus": "Forwards",
    "setze die richtung geradeaus": "Forwards",
    "laufe geradeaus": "Forwards",
    "folge der spur geradeaus": "Forwards",
    "folge der linie geradeaus": "Forwards",
    "folge dem weg geradeaus": "Forwards",
    "verfolge den weg geradeaus": "Forwards",
    "verfolge den pfad geradeaus": "Forwards",
    "verfolge den kurs geradeaus": "Forwards",
    "verfolge die route geradeaus": "Forwards",
    "verfolge die linie geradeaus": "Forwards",
    "fahre weiter geradeaus": "Forwards",
    "gehe weiter geradeaus": "Forwards",
    "laufe weiter geradeaus": "Forwards",
    "folge dem weg weiter geradeaus": "Forwards",
    "folge der straße weiter geradeaus": "Forwards",
    "folge der linie weiter geradeaus": "Forwards",
    "folge der schiene weiter geradeaus": "Forwards",

    "vorwärts": "Forwards",
    "fahre vorwärts": "Forwards",
    "richtig vorwärts": "Forwards",
    "in richtung vorwärts": "Forwards",
    "fahre in richtung vorwärts": "Forwards",
    "fahre in die richtung vorwärts": "Forwards",
    "in richtung vorwärts fahren": "Forwards",
    "in richtung vorwärts bewegen": "Forwards",
    "bewege dich vorwärts": "Forwards",
    "vorwärts fahren": "Forwards",
    "gehe voran vorwärts": "Forwards",
    "setze den weg auf vorwärts": "Forwards",
    "setze den pfad auf vorwärts": "Forwards",
    "setze den kurs auf vorwärts": "Forwards",
    "setze die route auf vorwärts": "Forwards",
    "setze die richtung auf vorwärts": "Forwards",
    "laufe vorwärts": "Forwards",
    "folge der spur vorwärts": "Forwards",
    "folge der linie vorwärts": "Forwards",
    "folge dem weg vorwärts": "Forwards",
    "verfolge den weg vorwärts": "Forwards",
    "verfolge den pfad vorwärts": "Forwards",
    "verfolge den kurs vorwärts": "Forwards",
    "verfolge die route vorwärts": "Forwards",
    "verfolge die linie vorwärts": "Forwards",
    "gehe weiter vorwärts": "Forwards",
    "laufe weiter vorwärts": "Forwards",
    "folge dem weg weiter vorwärts": "Forwards",
    "folge der straße weiter vorwärts": "Forwards",
    "folge der linie weiter vorwärts": "Forwards",
    "folge der schiene weiter vorwärts": "Forwards",
    "gerade vorwärts": "Forwards",
    "gehe vorwärts": "Forwards",
    "vorwärts bewegen": "Forwards",
    "fahre weiter vorwärts": "Forwards",

    "gerade nach vorne": "Forwards",
    "voran": "Forwards",
    "nach vorn": "Forwards",
    "nach vorn bewegen": "Forwards",
    "bewege dich nach vorn": "Forwards",
    "bewege dich voran": "Forwards",
    "gehe voran": "Forwards",
    "fahre weiter voran": "Forwards",
    "fahre nach vorne": "Forwards",


    #Direction backwards
    "rückwärts": "Backwards",
    "fahre rückwärts": "Backwards",
    "richtig rückwärts": "Backwards",
    "in richtung rückwärts": "Backwards",
    "fahre in richtung rückwärts": "Backwards",
    "fahre in die richtung rückwärts": "Backwards",
    "in richtung rückwärts fahren": "Backwards",
    "in richtung rückwärts bewegen": "Backwards",
    "bewege dich rückwärts": "Backwards",
    "gehe rückwärts": "Backwards",
    "rückwärts fahren": "Backwards",
    "setze den weg rückwärts": "Backwards",
    "setze den pfad rückwärts": "Backwards",
    "setze den kurs rückwärts": "Backwards",
    "setze die route rückwärts": "Backwards",
    "setze die richtung rückwärts": "Backwards",
    "laufe rückwärts": "Backwards",
    "folge der spur rückwärts": "Backwards",
    "folge der linie rückwärts": "Backwards",
    "folge dem weg rückwärts": "Backwards",
    "verfolge den weg rückwärts": "Backwards",
    "verfolge den pfad rückwärts": "Backwards",
    "verfolge den kurs rückwärts": "Backwards",
    "verfolge die route rückwärts": "Backwards",
    "verfolge die linie rückwärts": "Backwards",
    "fahre weiter rückwärts": "Backwards",
    "gehe weiter rückwärts": "Backwards",
    "laufe weiter rückwärts": "Backwards",
    "folge dem weg weiter rückwärts": "Backwards",
    "folge der straße weiter rückwärts": "Backwards",
    "folge der linie weiter rückwärts": "Backwards",
    "folge der schiene weiter rückwärts": "Backwards",

    "nach hinten": "Backwards",
    "fahre nach hinten": "Backwards",
    "richtig nach hinten": "Backwards",
    "in richtung nach hinten": "Backwards",
    "fahre in richtung nach hinten": "Backwards",
    "fahre in die richtung nach hinten": "Backwards",
    "in richtung nach hinten fahren": "Backwards",
    "in richtung nach hinten bewegen": "Backwards",
    "bewege dich nach hinten": "Backwards",
    "nach hinten fahren": "Backwards",
    "setze den weg auf nach hinten": "Backwards",
    "setze den pfad auf nach hinten": "Backwards",
    "setze den kurs auf nach hinten": "Backwards",
    "setze die route auf nach hinten": "Backwards",
    "setze die richtung auf nach hinten": "Backwards",
    "laufe nach hinten": "Backwards",
    "folge der spur nach hinten": "Backwards",
    "folge der linie nach hinten": "Backwards",
    "folge dem weg nach hinten": "Backwards",
    "verfolge den weg nach hinten": "Backwards",
    "verfolge den pfad nach hinten": "Backwards",
    "verfolge den kurs nach hinten": "Backwards",
    "verfolge die route nach hinten": "Backwards",
    "verfolge die linie nach hinten": "Backwards",
    "gehe weiter nach hinten": "Backwards",
    "laufe weiter nach hinten": "Backwards",
    "folge dem weg weiter nach hinten": "Backwards",
    "folge der straße weiter nach hinten": "Backwards",
    "folge der linie weiter nach hinten": "Backwards",
    "folge der schiene weiter nach hinten": "Backwards",
    "gehe nach hinten": "Backwards",
    "nach hinten bewegen": "Backwards",
    "fahre weiter nach hinten": "Backwards",

    "gerade nach hinten": "Backwards",
    "fahre geradewegs nach hinten": "Backwards",


    "stop": 0,
    "halte an": 0,
    "anhalten": 0,
    "start": 500,
    "fahre los": 500,
    "fahre so schnell wie möglich": 1000,
}

switches = {
    "weiche eins": "weiche_1",
    "weiche zwei": "weiche_2",
    "weiche drei": "weiche_3",
    "weiche vier": "weiche_4",
    "weiche fünf": "weiche_5",
    "weiche sechs": "weiche_6",
    "weiche sieben": "weiche_7",
    "weiche acht": "weiche_8",
    "weiche neun": "weiche_9",

    "gleis eins": "weiche_1",
    "gleis zwei": "weiche_2",
    "gleis drei": "weiche_3",
    "gleis vier": "weiche_4",
    "gleis fünf": "weiche_5",
    "gleis sechs": "weiche_6",
    "gleis sieben": "weiche_7",
    "gleis acht": "weiche_8",
    "gleis neun": "weiche_9",
}

trains = {
    "zug eins": "zug_1",
    "zug zwei": "zug_2",
    "zug drei": "zug_3",
    "zug vier": "zug_4",
    "bahn eins": "zug_1",
    "bahn zwei": "zug_2",
    "bahn drei": "zug_3",
    "bahn vier": "zug_4",
}

for train_name, train_id in trains.items():
    for action, value in train_standard_commands.items():
        command_name = f"{train_name} {action}"
        if isinstance(value, str):
            commands[command_name] = lambda tid=train_id, val=value: http_client.set_train_direction(tid, val)
        else:
            commands[command_name] = lambda tid=train_id, val=value: http_client.set_train_speed(tid, val)

    for action, value in train_custom_speed_commands.items():
        command_name = f"{train_name} {action}"
        commands[command_name] = lambda tid=train_id, val=value: http_client.add_train_speed(tid, val)

for switch_name, switch_id in switches.items():
    for action in custom_switch_commands:
        command_name = f"{action} {switch_name}"
        commands[command_name] = lambda sid=switch_id: http_client.set_switch(sid)
        command_name = f"{switch_name} {action}"
        commands[command_name] = lambda sid=switch_id: http_client.set_switch(sid)

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
