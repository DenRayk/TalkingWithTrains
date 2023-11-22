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
    '"vier",'
    '"fahre",'
    '"nach",'
    '"vorwärts",'
    '"rückwärts",'
    '"geradeaus",'
    '"stop",'
    '"halte",'
    '"an",'
    '"geschwindigkeit",'
    '"mit",'
    '"zu",'
    '"gleis",'
    '"abschnitt",'
    '"weiche",'
    '"stelle",'
    '"toggle",'
    '"alle",'
    '"weiter",'
    '"[unk]"]')


def transcribe(audio, file_path):
    with open(file_path, "wb") as f:
        f.write(audio.get_wav_data())

    rec.AcceptWaveform(audio.get_wav_data())
    result = rec.Result()
    return result
