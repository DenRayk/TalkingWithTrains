import whisper
import warnings
import os

# Load this file from cache if it exists, otherwise download it
tiny_model_path = os.path.expanduser('~/.cache/whisper/tiny.pt')
base_model_path = os.path.expanduser('~/.cache/whisper/base.pt')

tiny_model = whisper.load_model(tiny_model_path)
base_model = whisper.load_model(base_model_path)

warnings.filterwarnings("ignore", category=UserWarning, module='whisper.transcribe', lineno=115)


def transcribe(audio, file_path):
    with open(file_path, "wb") as f:
        f.write(audio.get_wav_data())

    result = tiny_model.transcribe(file_path, language="de")
    return result['text']
