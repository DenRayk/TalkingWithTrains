from vosk import Model, KaldiRecognizer

model = Model(lang="de")

rec = KaldiRecognizer(model, 16000)
rec.SetGrammar(
    '["modellbahn",'
    '"bahnhof",'
    '"zug",'
    '"eins",'
    '"zwei",'
    '"drei",'
    '"fahre",'
    '"nach",'
    '"[unk]"]')


def transcribe(audio, file_path):
    with open(file_path, "wb") as f:
        f.write(audio.get_wav_data())

    rec.AcceptWaveform(audio.get_wav_data())
    result = rec.Result()
    return result
