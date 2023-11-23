import json
from vosk import Model, KaldiRecognizer

model = Model(lang="de")
rec = KaldiRecognizer(model, 16000)


def load_grammar(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


grammar = load_grammar("speech_control/grammar.json")
rec.SetGrammar(json.dumps(grammar))


def transcribe(audio, file_path):
    with open(file_path, "wb") as f:
        f.write(audio.get_wav_data())

    rec.AcceptWaveform(audio.get_wav_data())
    result = rec.Result()
    return result
