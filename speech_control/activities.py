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

train_speed_commands = {
    "stop": 0,
    "halt": 0,
    "halte an": 0,
    "anhalten": 0,
    "bleib stehen": 0,
    "start": 500,
    "beginne": 500,
    "starte": 500,
    "fahre": 500,
    "fahre los": 500,
    "losfahren": 500,
    "fahre so schnell wie möglich": 1000,
    "fahre mit voller geschwindigkeit": 1000,
    "maximale beschleunigung": 1000,
    "maximale geschwindigkeit": 1000,
}

increaseTrainSpeed = 200
reduceTrainSpeed = -200
train_add_speed_commands = {
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

train_direction_commands = {
    #Commands for train direction with speed stop

    #Direction forwards
    "geradeaus": "Forwards",
    "schalte geradeaus": "Forwards",
    "schalte in richtung geradeaus": "Forwards",
    "schalte in die richtung geradeaus": "Forwards",

    "setze den weg geradeaus": "Forwards",
    "setze den pfad geradeaus": "Forwards",
    "setze den kurs geradeaus": "Forwards",
    "setze die route geradeaus": "Forwards",
    "setze die richtung geradeaus": "Forwards",

    "vorwärts": "Forwards",
    "schalte vorwärts": "Forwards",
    "schalte in richtung vorwärts": "Forwards",
    "schalte in die richtung vorwärts": "Forwards",

    "setze den weg auf vorwärts": "Forwards",
    "setze den pfad auf vorwärts": "Forwards",
    "setze den kurs auf vorwärts": "Forwards",
    "setze die route auf vorwärts": "Forwards",
    "setze die richtung auf vorwärts": "Forwards",

    #Direction backwards
    "rückwärts": "Backwards",
    "schalte rückwärts": "Backwards",
    "schalte in richtung rückwärts": "Backwards",
    "schalte in die richtung rückwärts": "Backwards",

    "setze den weg rückwärts": "Backwards",
    "setze den pfad rückwärts": "Backwards",
    "setze den kurs rückwärts": "Backwards",
    "setze die route rückwärts": "Backwards",
    "setze die richtung rückwärts": "Backwards",

    "nach hinten": "Backwards",
    "schalte nach hinten": "Backwards",
    "schalte in richtung nach hinten": "Backwards",
    "schalte in die richtung nach hinten": "Backwards",

    "setze den weg auf nach hinten": "Backwards",
    "setze den pfad auf nach hinten": "Backwards",
    "setze den kurs auf nach hinten": "Backwards",
    "setze die route auf nach hinten": "Backwards",
    "setze die richtung auf nach hinten": "Backwards",
}

train_direction_speed_commands = {
    #Commands for train direction with speed continue

    #Direction forwards
    "fahre rückwärts": "Forwards",
    "fahre in richtung rückwärts": "Forwards",
    "fahre in die richtung rückwärts": "Forwards",
    "fahre weiter rückwärts": "Forwards",
    "fahre weiter in richtung rückwärts": "Forwards",
    "fahre weiter in die richtung rückwärts": "Forwards",
    "fahre mit selber geschwindigkeit rückwärts": "Forwards",
    "fahre mit gleicher geschwindigkeit rückwärts": "Forwards",
    "fahre mit gleicher geschwindigkeit in richtung rückwärts": "Forwards",
    "fahre mit gleicher geschwindigkeit in die richtung rückwärts": "Forwards",
    "fahre mit der selber geschwindigkeit rückwärts": "Forwards",
    "fahre mit der gleicher geschwindigkeit rückwärts": "Forwards",
    "fahre mit der gleicher geschwindigkeit in richtung rückwärts": "Forwards",
    "fahre mit der gleicher geschwindigkeit in die richtung rückwärts": "Forwards",
    "in richtung rückwärts fahren": "Forwards",
    "in richtung rückwärts bewegen": "Forwards",
    "gleiche geschwindigkeit rückwärts": "Forwards",
    "gleiche geschwindigkeit in richtung rückwärts": "Forwards",
    "gleiche geschwindigkeit in die richtung rückwärts": "Forwards",
    "mit gleicher geschwindigkeit rückwärts": "Forwards",
    "mit gleicher geschwindigkeit in richtung rückwärts": "Forwards",
    "mit gleicher geschwindigkeit in die richtung rückwärts": "Forwards",
    "mit der gleicher geschwindigkeit rückwärts": "Forwards",
    "mit der gleicher geschwindigkeit in richtung rückwärts": "Forwards",
    "mit der gleicher geschwindigkeit in die richtung rückwärts": "Forwards",

    "fahre nach hinten": "Forwards",
    "fahre in richtung nach hinten": "Forwards",
    "fahre in die richtung nach hinten": "Forwards",
    "fahre weiter nach hinten": "Forwards",
    "fahre weiter in richtung nach hinten": "Forwards",
    "fahre weiter in die richtung nach hinten": "Forwards",
    "fahre mit selber geschwindigkeit nach hinten": "Forwards",
    "fahre mit gleicher geschwindigkeit nach hinten": "Forwards",
    "fahre mit gleicher geschwindigkeit in richtung nach hinten": "Forwards",
    "fahre mit gleicher geschwindigkeit in die richtung nach hinten": "Forwards",
    "fahre mit der selber geschwindigkeit nach hinten": "Forwards",
    "fahre mit der gleicher geschwindigkeit nach hinten": "Forwards",
    "fahre mit der gleicher geschwindigkeit in richtung nach hinten": "Forwards",
    "fahre mit der gleicher geschwindigkeit in die richtung nach hinten": "Forwards",
    "in richtung nach hinten fahren": "Forwards",
    "in richtung nach hinten bewegen": "Forwards",
    "gleiche geschwindigkeit nach hinten": "Forwards",
    "gleiche geschwindigkeit in richtung nach hinten": "Forwards",
    "gleiche geschwindigkeit in die richtung nach hinten": "Forwards",
    "mit gleicher geschwindigkeit nach hinten": "Forwards",
    "mit gleicher geschwindigkeit in richtung nach hinten": "Forwards",
    "mit gleicher geschwindigkeit in die richtung nach hinten": "Forwards",
    "mit der gleicher geschwindigkeit nach hinten": "Forwards",
    "mit der gleicher geschwindigkeit in richtung nach hinten": "Forwards",
    "mit der gleicher geschwindigkeit in die richtung nach hinten": "Forwards",

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
    "fahre geradeaus": "Backwards",
    "fahre in richtung geradeaus": "Backwards",
    "fahre in die richtung geradeaus": "Backwards",
    "fahre weiter geradeaus": "Backwards",
    "fahre weiter in richtung geradeaus": "Backwards",
    "fahre weiter in die richtung geradeaus": "Backwards",
    "fahre mit selber geschwindigkeit geradeaus": "Backwards",
    "fahre mit gleicher geschwindigkeit geradeaus": "Backwards",
    "fahre mit gleicher geschwindigkeit in richtung geradeaus": "Backwards",
    "fahre mit gleicher geschwindigkeit in die richtung geradeaus": "Backwards",
    "fahre mit der selber geschwindigkeit geradeaus": "Backwards",
    "fahre mit der gleicher geschwindigkeit geradeaus": "Backwards",
    "fahre mit der gleicher geschwindigkeit in richtung geradeaus": "Backwards",
    "fahre mit der gleicher geschwindigkeit in die richtung geradeaus": "Backwards",
    "in richtung geradeaus fahren": "Backwards",
    "in richtung geradeaus bewegen": "Backwards",
    "gleiche geschwindigkeit geradeaus": "Backwards",
    "gleiche geschwindigkeit in richtung geradeaus": "Backwards",
    "gleiche geschwindigkeit in die richtung geradeaus": "Backwards",
    "mit gleicher geschwindigkeit geradeaus": "Backwards",
    "mit gleicher geschwindigkeit in richtung geradeaus": "Backwards",
    "mit gleicher geschwindigkeit in die richtung geradeaus": "Backwards",
    "mit der gleicher geschwindigkeit geradeaus": "Backwards",
    "mit der gleicher geschwindigkeit in richtung geradeaus": "Backwards",
    "mit der gleicher geschwindigkeit in die richtung geradeaus": "Backwards",

    "fahre vorwärts": "Backwards",
    "fahre in richtung vorwärts": "Backwards",
    "fahre in die richtung vorwärts": "Backwards",
    "fahre weiter vorwärts": "Backwards",
    "fahre weiter in richtung vorwärts": "Backwards",
    "fahre weiter in die richtung vorwärts": "Backwards",
    "fahre mit selber geschwindigkeit vorwärts": "Backwards",
    "fahre mit gleicher geschwindigkeit vorwärts": "Backwards",
    "fahre mit gleicher geschwindigkeit in richtung vorwärts": "Backwards",
    "fahre mit gleicher geschwindigkeit in die richtung vorwärts": "Backwards",
    "fahre mit der selber geschwindigkeit vorwärts": "Backwards",
    "fahre mit der gleicher geschwindigkeit vorwärts": "Backwards",
    "fahre mit der gleicher geschwindigkeit in richtung vorwärts": "Backwards",
    "fahre mit der gleicher geschwindigkeit in die richtung vorwärts": "Backwards",
    "in richtung vorwärts fahren": "Backwards",
    "in richtung vorwärts bewegen": "Backwards",
    "gleiche geschwindigkeit vorwärts": "Backwards",
    "gleiche geschwindigkeit in richtung vorwärts": "Backwards",
    "gleiche geschwindigkeit in die richtung vorwärts": "Backwards",
    "mit gleicher geschwindigkeit vorwärts": "Backwards",
    "mit gleicher geschwindigkeit in richtung vorwärts": "Backwards",
    "mit gleicher geschwindigkeit in die richtung vorwärts": "Backwards",
    "mit der gleicher geschwindigkeit vorwärts": "Backwards",
    "mit der gleicher geschwindigkeit in richtung vorwärts": "Backwards",
    "mit der gleicher geschwindigkeit in die richtung vorwärts": "Backwards",

    "gerade nach hinten": "Backwards",
    "nach hinten": "Backwards",
    "nach hinten bewegen": "Backwards",
    "bewege dich nach hinten": "Backwards",
    "bewege dich hinten": "Backwards",
    "gehe hinten": "Backwards",
    "fahre weiter hinten": "Backwards",
}

accessories_light_commands = {
    "an": True,
    "aktiviert": True,
    "aktiviere": True,
    "aktivieren": True,
    "ein": True,
    "einschalten": True,
    "schalte ein": True,
    "schalte dich ein": True,
    "schalte an": True,
    "schalte dich an": True,
    "gehe an": True,

    "aus": False,
    "deaktiviert": False,
    "deaktiviere": False,
    "deaktivieren": False,
    "ausschalten": False,
    "schalte aus": False,
    "schalte dich aus": False,
    "schalte ab": False,
    "schalte dich ab": False,
    "gehe aus": False,
}

accessories_general_turnouts_commands = {
    #Weichen Gerade/Grün
    "gerade": True,
    "schalte gerade": True,
    "schalte dich gerade": True,
    "schalte in die gerade position": True,
    "schalte in die position gerade": True,
    "schalte auf gerade": True,
    "schalte auf gerade um": True,
    "schalte dich auf gerade": True,
    "schalte dich auf gerade um": True,
    "setze auf gerade": True,
    "stelle auf gerade": True,
    "aktiviere gerade position": True,
    "wähle gerade aus": True,
    "lege auf gerade": True,
    "lege auf gerade um": True,
    "ändere auf gerade": True,

    "grün": True,
    "schalte grün": True,
    "schalte dich grün": True,
    "schalte dich auf grün": True,
    "schalte dich auf grün um": True,
    "schalte in die grün position": True,
    "schalte in die position grün": True,
    "schalte auf grün": True,
    "schalte auf grün um": True,
    "setze auf grün": True,
    "stelle auf grün": True,
    "aktiviere grün position": True,
    "wähle grün aus": True,
    "lege auf grün": True,
    "lege auf grün um": True,
    "ändere auf grün": True,

    # Weichen Rot/Kurve/Abzweigend
    "kurve": False,
    "schalte kurve": False,
    "schalte die Kurve": False,
    "schalte auf Kurve": False,
    "schalte auf die Kurve um": False,
    "setze auf Kurve": False,
    "stelle auf Kurve": False,
    "aktiviere Kurve-Position": False,
    "wähle Kurve aus": False,
    "lege auf Kurve": False,
    "ändere auf Kurve": False,

    "abzweigend": False,
    "schalte abzweigend": False,
    "schalte abzweigend um": False,
    "schalte auf abzweigend": False,
    "schalte auf die Abzweigend-Position": False,
    "setze auf abzweigend": False,
    "stelle auf abzweigend": False,
    "aktiviere Abzweigend-Position": False,
    "wähle Abzweigend aus": False,
    "lege auf abzweigend": False,
    "ändere auf abzweigend": False,

    "rot": False,
    "schalte rot": False,
    "schalte dich rot": False,
    "schalte dich auf rot": False,
    "schalte dich auf rot um": False,
    "schalte in die rot position": False,
    "schalte in die position rot": False,
    "schalte auf rot": False,
    "schalte auf rot um": False,
    "setze auf rot": False,
    "stelle auf rot": False,
    "aktiviere rot position": False,
    "wähle rot aus": False,
    "lege auf rot ": False,
    "lege auf rot um": False,
    "ändere auf rot": False,
}

accessories_right_turnouts_commands = {
    "rechts": False,
    "schalte rechts": False,
    "schalte dich rechts": False,
    "schalte dich auf rechts": False,
    "schalte dich auf rechts um": False,
    "schalte in die rechts position": False,
    "schalte in die rechte position": False,
    "schalte auf rechts": False,
    "schalte auf rechts um": False,
    "setze auf rechts": False,
    "stelle auf rechts": False,
    "aktiviere rechte position": False,
    "wähle rechts aus": False,
    "lege auf rechts": False,
    "lege auf rechts um": False,
    "ändere auf rechts": False,

    "links": True,
    "schalte links": True,
    "schalte dich links": True,
    "schalte dich auf links": True,
    "schalte dich auf links um": True,
    "schalte in die links position": True,
    "schalte in die linke position": True,
    "schalte auf links": True,
    "schalte auf links um": True,
    "setze auf links": True,
    "stelle auf links": True,
    "aktiviere linke position": True,
    "wähle links aus": True,
    "lege auf links": True,
    "lege auf links um": True,
    "ändere auf links": True,
}

accessories_left_turnouts_commands = {
    "rechts": True,
    "schalte rechts": True,
    "schalte dich rechts": True,
    "schalte dich auf rechts": True,
    "schalte dich auf rechts um": True,
    "schalte in die rechts position": True,
    "schalte in die rechte position": True,
    "schalte auf rechts": True,
    "schalte auf rechts um": True,
    "setze auf rechts": True,
    "stelle auf rechts": True,
    "aktiviere rechte position": True,
    "wähle rechts aus": True,
    "lege auf rechts": True,
    "lege auf rechts um": True,
    "ändere auf rechts": True,

    "links": False,
    "schalte links": False,
    "schalte dich links": False,
    "schalte dich auf links": False,
    "schalte dich auf links um": False,
    "schalte in die links position": False,
    "schalte in die linke position": False,
    "schalte auf links": False,
    "schalte auf links um": False,
    "setze auf links": False,
    "stelle auf links": False,
    "aktiviere linke position": False,
    "wähle links aus": False,
    "lege auf links": False,
    "lege auf links um": False,
    "ändere auf links": False,
}

accessories_triple_switch_commands = {
    #Dreiwegweichen
    #"links"
    #"mitte"
    #"rechts"
}

accessories_uncoupling_tracks_commands = {
    "aktivier": True,
    "aktiviere": True,
    "aktivieren": True,
    "aktiviert": True,
    "schalte ein": True,
    "schalte dich ein": True,
    "schalte an": True,
    "schalte dich an": True,
    "gehe an": True,
    "schalte auf": True,
    "entkuppeln": True,
    "entkupple": True,
    "abkuppeln": True,
    "entkupple dich": True,
    "löse Verbindung": True,
    "löse die Verbindung": True,
    "löse die Kupplung": True,
    "löse die Verbindung zwischen Wagen": True,
    "trenne Wagen": True,
    "trenne die Wagen": True,
    "löse die Wagen": True,
    "löse den Zug": True,
    "löse den Zugteil": True,
    "löse die Lokomotive": True,
    "kuppel ab": True,
    "kuppel die Wagen ab": True,
    "kuppel die Lokomotive ab": True,
    "kuppel den Zugteil ab": True,
    "kuppel den Zug ab": True,
    "kuppel dich ab": True,
    "kuppel die Kupplung ab": True,
    "trenne die Kupplung": True,
    "löse die Verbindung zwischen Lokomotive und Wagen": True,
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

accessories_right_turnouts = {
    #Rechtsweichen
    "weiche drei": "W 3",
    "weiche neun": "W 9",
    "weiche zehn": "W 10",
    "weiche zwölf": "W 12",
    "weiche dreizehn": "W 13",
    "weiche vierzehn": "W 14",

    "weiche w drei": "W 3",
    "weiche w neun": "W 9",
    "weiche w zehn": "W 10",
    "weiche w zwölf": "W 12",
    "weiche w dreizehn": "W 13",
    "weiche w vierzehn": "W 14",

    "gleis drei": "W 3",
    "gleis neun": "W 9",
    "gleis zehn": "W 10",
    "gleis zwölf": "W 12",
    "gleis dreizehn": "W 13",
    "gleis vierzehn": "W 14",

    "gleis w drei": "W 3",
    "gleis w neun": "W 9",
    "gleis w zehn": "W 10",
    "gleis w zwölf": "W 12",
    "gleis w dreizehn": "W 13",
    "gleis w vierzehn": "W 14",

    "w drei": "W 3",
    "w neun": "W 9",
    "w zehn": "W 10",
    "w zwölf": "W 12",
    "w dreizehn": "W 13",
    "w vierzehn": "W 14",
}

accessories_left_turnouts = {
    #Linksweichen
    "weiche sechs": "W 6",
    "weiche w sechs": "W 6",
    "gleis sechs": "W 6",
    "gleis w sechs": "W 6",
    "w sechs": "W 6",
}

accessories_Three_way_turnouts = {
    #Dreiwegweichen
    #TODO: Add commands list for three way switches
    #TODO: Dynamically create commands for three way switches
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


#Dynamically create commands for trains
for train_name, train_id in trains.items():
    #Commands for train speed
    for action, value in train_speed_commands.items():
        command_name = f"{train_name} {action}"
        commands[command_name] = lambda tid=train_id, val=value: http_client.set_train_speed(tid, val)
    #Commands for train direction
    for action, value in train_direction_commands.items():
        command_name = f"{train_name} {action}"
        commands[command_name] = lambda tid=train_id, val=value: http_client.set_train_direction(tid, val)
    #Commands for train direction with speed
    for action, value in train_direction_speed_commands.items():
        command_name = f"{train_name} {action}"
        commands[command_name] = lambda tid=train_id, val=value: http_client.set_train_direction_with_speed(tid, val)
    #Commands for train adding speed
    for action, value in train_add_speed_commands.items():
        command_name = f"{train_name} {action}"
        commands[command_name] = lambda tid=train_id, val=value: http_client.add_train_speed(tid, val)

#Dynamically create commands for accessory signals
for accessory_name, accessory_id in accessories_light_signals.items():
    #Commands for accessories light
    for action, value in accessories_light_commands.items():
        command_name = f"{accessory_name} {action}"
        commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_status(aid, val)

#Dynamically create commands for accessory right turnouts
for accessory_name, accessory_id in accessories_right_turnouts.items():
    #Commands for accessories right turnouts
    for action, value in accessories_general_turnouts_commands.items():
        command_name = f"{accessory_name} {action}"
        commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_status(aid, val)
    for action, value in accessories_right_turnouts_commands.items():
        command_name = f"{accessory_name} {action}"
        commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_status(aid, val)

#Dynamically create commands for accessory left turnouts
for accessory_name, accessory_id in accessories_left_turnouts.items():
    #Commands for accessories left turnouts
    for action, value in accessories_general_turnouts_commands.items():
        command_name = f"{accessory_name} {action}"
        commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_status(aid, val)
    for action, value in accessories_left_turnouts_commands.items():
        command_name = f"{accessory_name} {action}"
        commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_status(aid, val)

#Dynamically create commands for accessory uncoupling tracks
for accessory_name, accessory_id in accessories_uncoupling_tracks.items():
    #Commands for accessories uncoupling tracks
    for action, value in accessories_uncoupling_tracks_commands.items():
        command_name = f"{accessory_name} {action}"
        commands[command_name] = lambda aid=accessory_id, val=value: http_client.set_accessory_status(aid, val)

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
