import json
from vosk import Model, KaldiRecognizer

model = Model(lang="de")
rec = KaldiRecognizer(model, 48000)


def load_grammar(file_path):
    with open(file_path, 'rb') as file:
        return json.load(file)


grammar = load_grammar("speech_control/grammar.json")
rec.SetGrammar(json.dumps(grammar, ensure_ascii=False))


def transcribe(audio, file_path=None):
    if file_path:
        with open(file_path, "wb") as file:
            file.write(audio.get_wav_data())

    rec.AcceptWaveform(audio.get_wav_data())
    result = rec.Result()
    return result
