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
    "fahre mit maximaler geschwindigkeit": 1000,
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

train_function_commands = {
    "licht an": 0,
    "licht aus": 0,
    "rauch an": 1,
    "rauch aus": 1,
    "hupe": 3
}


train_direction_speed_commands = {
    # Commands for train direction with speed continue

    # Direction backwards
    "zurück": "Backwards",
    "fahe zurück": "Backwards",
    "rückwärts": "Backwards",
    "schalte rückwärts": "Backwards",
    "schalte in richtung rückwärts": "Backwards",
    "schalte in die richtung rückwärts": "Backwards",

    "setze den weg rückwärts": "Backwards",
    "setze den pfad rückwärts": "Backwards",
    "setze den kurs rückwärts": "Backwards",
    "setze die route rückwärts": "Backwards",
    "setze die richtung rückwärts": "Backwards",

    "schalte nach hinten": "Backwards",
    "schalte in richtung nach hinten": "Backwards",
    "schalte in die richtung nach hinten": "Backwards",

    "setze den weg auf nach hinten": "Backwards",
    "setze den pfad auf nach hinten": "Backwards",
    "setze den kurs auf nach hinten": "Backwards",
    "setze die route auf nach hinten": "Backwards",
    "setze die richtung auf nach hinten": "Backwards",
    "fahre rückwärts": "Backwards",
    "fahre in richtung rückwärts": "Backwards",
    "fahre in die richtung rückwärts": "Backwards",
    "fahre weiter rückwärts": "Backwards",
    "fahre weiter in richtung rückwärts": "Backwards",
    "fahre weiter in die richtung rückwärts": "Backwards",
    "fahre mit gleicher geschwindigkeit rückwärts": "Backwards",
    "fahre mit gleicher geschwindigkeit in richtung rückwärts": "Backwards",
    "fahre mit gleicher geschwindigkeit in die richtung rückwärts": "Backwards",
    "fahre mit der gleicher geschwindigkeit rückwärts": "Backwards",
    "fahre mit der gleicher geschwindigkeit in richtung rückwärts": "Backwards",
    "fahre mit der gleicher geschwindigkeit in die richtung rückwärts": "Backwards",
    "in richtung rückwärts fahren": "Backwards",
    "in richtung rückwärts bewegen": "Backwards",
    "gleiche geschwindigkeit rückwärts": "Backwards",
    "gleiche geschwindigkeit in richtung rückwärts": "Backwards",
    "gleiche geschwindigkeit in die richtung rückwärts": "Backwards",
    "mit gleicher geschwindigkeit rückwärts": "Backwards",
    "mit gleicher geschwindigkeit in richtung rückwärts": "Backwards",
    "mit gleicher geschwindigkeit in die richtung rückwärts": "Backwards",
    "mit der gleicher geschwindigkeit rückwärts": "Backwards",
    "mit der gleicher geschwindigkeit in richtung rückwärts": "Backwards",
    "mit der gleicher geschwindigkeit in die richtung rückwärts": "Backwards",

    "fahre nach hinten": "Backwards",
    "fahre in richtung nach hinten": "Backwards",
    "fahre in die richtung nach hinten": "Backwards",
    "fahre weiter nach hinten": "Backwards",
    "fahre weiter in richtung nach hinten": "Backwards",
    "fahre weiter in die richtung nach hinten": "Backwards",
    "fahre mit gleicher geschwindigkeit nach hinten": "Backwards",
    "fahre mit gleicher geschwindigkeit in richtung nach hinten": "Backwards",
    "fahre mit gleicher geschwindigkeit in die richtung nach hinten": "Backwards",
    "fahre mit der gleicher geschwindigkeit nach hinten": "Backwards",
    "fahre mit der gleicher geschwindigkeit in richtung nach hinten": "Backwards",
    "fahre mit der gleicher geschwindigkeit in die richtung nach hinten": "Backwards",
    "in richtung nach hinten fahren": "Backwards",
    "in richtung nach hinten bewegen": "Backwards",
    "gleiche geschwindigkeit nach hinten": "Backwards",
    "gleiche geschwindigkeit in richtung nach hinten": "Backwards",
    "gleiche geschwindigkeit in die richtung nach hinten": "Backwards",
    "mit gleicher geschwindigkeit nach hinten": "Backwards",
    "mit gleicher geschwindigkeit in richtung nach hinten": "Backwards",
    "mit gleicher geschwindigkeit in die richtung nach hinten": "Backwards",
    "mit der gleicher geschwindigkeit nach hinten": "Backwards",
    "mit der gleicher geschwindigkeit in richtung nach hinten": "Backwards",
    "mit der gleicher geschwindigkeit in die richtung nach hinten": "Backwards",

    "gerade nach hinten": "Backwards",
    "nach hinten": "Backwards",
    "nach hinten bewegen": "Backwards",
    "bewege dich nach hinten": "Backwards",
    "bewege dich hinten": "Backwards",
    "gehe hinten": "Backwards",
    "fahre weiter hinten": "Backwards",

    # Direction forwards
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
    "fahre geradeaus": "Backwards",
    "fahre in richtung geradeaus": "Backwards",
    "fahre in die richtung geradeaus": "Backwards",
    "fahre weiter geradeaus": "Backwards",
    "fahre weiter in richtung geradeaus": "Backwards",
    "fahre weiter in die richtung geradeaus": "Backwards",
    "fahre mit gleicher geschwindigkeit geradeaus": "Backwards",
    "fahre mit gleicher geschwindigkeit in richtung geradeaus": "Backwards",
    "fahre mit gleicher geschwindigkeit in die richtung geradeaus": "Backwards",
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

    "fahre vorwärts": "Forwards",
    "fahre in richtung vorwärts": "Forwards",
    "fahre in die richtung vorwärts": "Forwards",
    "fahre weiter vorwärts": "Forwards",
    "fahre weiter in richtung vorwärts": "Forwards",
    "fahre weiter in die richtung vorwärts": "Forwards",
    "fahre mit gleicher geschwindigkeit vorwärts": "Forwards",
    "fahre mit gleicher geschwindigkeit in richtung vorwärts": "Forwards",
    "fahre mit gleicher geschwindigkeit in die richtung vorwärts": "Forwards",
    "fahre mit der gleicher geschwindigkeit vorwärts": "Forwards",
    "fahre mit der gleicher geschwindigkeit in richtung vorwärts": "Forwards",
    "fahre mit der gleicher geschwindigkeit in die richtung vorwärts": "Forwards",
    "in richtung vorwärts fahren": "Forwards",
    "in richtung vorwärts bewegen": "Forwards",
    "gleiche geschwindigkeit vorwärts": "Forwards",
    "gleiche geschwindigkeit in richtung vorwärts": "Forwards",
    "gleiche geschwindigkeit in die richtung vorwärts": "Forwards",
    "mit gleicher geschwindigkeit vorwärts": "Forwards",
    "mit gleicher geschwindigkeit in richtung vorwärts": "Forwards",
    "mit gleicher geschwindigkeit in die richtung vorwärts": "Forwards",
    "mit der gleicher geschwindigkeit vorwärts": "Forwards",
    "mit der gleicher geschwindigkeit in richtung vorwärts": "Forwards",
    "mit der gleicher geschwindigkeit in die richtung vorwärts": "Forwards",

    "gerade nach vorne": "Forwards",
    "voran": "Forwards",
    "nach vorn": "Forwards",
    "nach vorn bewegen": "Forwards",
    "bewege dich nach vorn": "Forwards",
    "bewege dich voran": "Forwards",
    "gehe voran": "Forwards",
    "fahre weiter voran": "Forwards",
    "fahre nach vorne": "Forwards",
}
