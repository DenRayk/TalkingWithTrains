import speech_recognition as sr
import whisper
import warnings
import time
import os

wake_word = 'Bahnhof'
r = sr.Recognizer()

# Load this file from cache if it exists, otherwise download it
tiny_model_path = os.path.expanduser('~/.cache/whisper/tiny.pt')
base_model_path = os.path.expanduser('~/.cache/whisper/base.pt')

tiny_model = whisper.load_model(tiny_model_path)
base_model = whisper.load_model(base_model_path)

listening_for_wake_word = True
source = sr.Microphone()
warnings.filterwarnings("ignore", category=UserWarning, module='whisper.transcribe', lineno=114)


def transcribe(audio, file_path):

    with open(file_path, "wb") as f:
        f.write(audio.get_wav_data())

    result = tiny_model.transcribe(file_path, language="de")
    return result['text']


def listen_for_wake_word(audio):
    global listening_for_wake_word

    text_input = transcribe(audio, "wake_word.wav")
    print(text_input)

    if wake_word.lower() in text_input.lower().strip():
        print("Wake word detected. Please speak your prompt to TalkingWithTrains.")
        listening_for_wake_word = False


def prompt(audio):
    global listening_for_wake_word

    try:
        prompt_text = transcribe(audio, "voice-recognition/prompt.wav")

        if len(prompt_text.strip()) == 0:
            print("Empty prompt. Please speak again.")
            listening_for_wake_word = True
        else:
            print('User: ' + prompt_text)
            print('\nSay', wake_word, 'to wake me up. \n')
            listening_for_wake_word = True

    except Exception as e:
        print("Prompt error: ", e)


def callback(recognizer, audio):
    global listening_for_wake_word

    if listening_for_wake_word:
        listen_for_wake_word(audio)
    else:
        prompt(audio)


def start_listening():
    with source as s:
        r.adjust_for_ambient_noise(s, duration=3)

    print('\nSay', wake_word, 'to wake me up. \n')

    r.listen_in_background(source, callback, phrase_time_limit=5)

    while True:
        time.sleep(1)


if __name__ == '__main__':
    start_listening()
