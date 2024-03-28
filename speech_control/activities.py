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


accessories_light_signals = {
    # lichtsignale
    "lichtsignal eins": "S 1",
    "lichtsignal zwei": "S 2",
    "lichtsignal drei": "S 3",
    "lichtsignal fünf": "S 5",
    "lichtsignal sechs": "S 6",
    "lichtsignal sieben": "S 7",
    "lichtsignal acht": "S 8",
    "lichtsignal s eins": "S 1",
    "lichtsignal s zwei": "S 2",
    "lichtsignal s drei": "S 3",
    "lichtsignal s fünf": "S 5",
    "lichtsignal s sechs": "S 6",
    "lichtsignal s sieben": "S 7",
    "lichtsignal s acht": "S 8",
    "Ampel eins": "S 1",
    "Ampel zwei": "S 2",
    "Ampel drei": "S 3",
    "Ampel fünf": "S 5",
    "Ampel sechs": "S 6",
    "Ampel sieben": "S 7",
    "Ampel acht": "S 8",
    "Ampel s eins": "S 1",
    "Ampel s zwei": "S 2",
    "Ampel s drei": "S 3",
    "Ampel s fünf": "S 5",
    "Ampel s sechs": "S 6",
    "Ampel s sieben": "S 7",
    "Ampel s acht": "S 8",
    "s eins": "S 1",
    "s zwei": "S 2",
    "s drei": "S 3",
    "s fünf": "S 5",
    "s sechs": "S 6",
    "s sieben": "S 7",
    "s acht": "S 8",
}

accessories_normal_switches = {
    #Normale Weichen
    "weiche drei": "W 3",
    "weiche sechs": "W 6",
    "weiche neun": "W 9",
    "weiche zehn": "W 10",
    "weiche zwölf": "W 12",
    "weiche dreizehn": "W 13",
    "weiche vierzehn": "W 14",

    "weiche w drei": "W 3",
    "weiche w sechs": "W 6",
    "weiche w neun": "W 9",
    "weiche w zehn": "W 10",
    "weiche w zwölf": "W 12",
    "weiche w dreizehn": "W 13",
    "weiche w vierzehn": "W 14",

    "gleis drei": "W 3",
    "gleis sechs": "W 6",
    "gleis neun": "W 9",
    "gleis zehn": "W 10",
    "gleis zwölf": "W 12",
    "gleis dreizehn": "W 13",
    "gleis vierzehn": "W 14",

    "gleis w drei": "W 3",
    "gleis w sechs": "W 6",
    "gleis w neun": "W 9",
    "gleis w zehn": "W 10",
    "gleis w zwölf": "W 12",
    "gleis w dreizehn": "W 13",
    "gleis w vierzehn": "W 14",

    "w drei": "W 3",
    "w sechs": "W 6",
    "w neun": "W 9",
    "w zehn": "W 10",
    "w zwölf": "W 12",
    "w dreizehn": "W 13",
    "w vierzehn": "W 14",
}

accessories_triple_switch = {
    #Dreiwegweichen
    #TODO: Add commands for three way switches
}

accessories_uncoupling_tracks = {
    #Entkupplungsgleise
    "entkupplungsgleis vier": "W 4",
    "entkupplungsgleis elf": "W 11",

    "entkupplungsgleis w vier": "W 4",
    "entkupplungsgleis w elf": "W 11",

    "w vier": "W 4",
    "w elf": "W 11",
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
