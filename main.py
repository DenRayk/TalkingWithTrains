import speech_recognition as sr
import sounddevice  # do not remove this line (it is used to fix an error with alsa)

from speech_control.activities import extract_activity
from speech_control.transcription import transcribe
import time
import services.http_client as http_client

wake_word = 'Modellbahn'
source = sr.Microphone(sample_rate=16000, chunk_size=1024)
recognizer = sr.Recognizer()

listening_for_wake_word = True
recognizer.dynamic_energy_threshold = False


def listen_for_wake_word(audio):
    global listening_for_wake_word

    text_input = transcribe(audio)
    print(text_input)

    if wake_word.lower() in text_input.lower().strip():
        print("Wake word detected. Please speak your prompt to TalkingWithTrains.")
        listening_for_wake_word = False


def prompt(audio):
    global listening_for_wake_word

    try:
        prompt_text = transcribe(audio)

        if len(prompt_text.strip()) == 0:
            print("Empty prompt. Please speak again.")
            listening_for_wake_word = True
        else:
            print('User: ' + prompt_text)
            extract_activity(prompt_text)

            print('\nSay', wake_word, 'to wake me up. \n')
            listening_for_wake_word = True

    except Exception as e:
        print("Prompt error: ", e)
        print('\nSay', wake_word, 'to wake me up. \n')
        listening_for_wake_word = True


def callback(recognizer, audio):
    global listening_for_wake_word

    if listening_for_wake_word:
        listen_for_wake_word(audio)
    else:
        prompt(audio)


def start_listening():
    with source as s:
        print("Adjusting for ambient noise, please be quiet for a moment.")
        recognizer.adjust_for_ambient_noise(s, duration=2)

    print('\nSay', wake_word, 'to wake me up. \n')

    recognizer.listen_in_background(source, callback)

    while True:
        time.sleep(1)


if __name__ == '__main__':
    http_client.get_hash()
    start_listening()
