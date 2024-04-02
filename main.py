import argparse
import speech_recognition as sr
import sounddevice  # do not remove this line (it is used to fix an error with alsa)

from speech_control.activities import extract_activity
from speech_control.transcription import transcribe
from led_control import LEDController
import time
import services.http_client as http_client

wake_word = 'Modellbahn'
source = sr.Microphone(sample_rate=48000)
recognizer = sr.Recognizer()

listening_for_wake_word = True
recognizer.dynamic_energy_threshold = False


def activate_voice_control():
    global listening_for_wake_word
    print('\nSay', wake_word, 'to wake me up. \n')
    LEDController.voice_control_active()
    listening_for_wake_word = True


def listen_for_wake_word(audio):
    global listening_for_wake_word

    if args.wav:
        text_input = transcribe(audio, "wake_word.wav")
    else:
        text_input = transcribe(audio)
    print(text_input)

    if wake_word.lower() in text_input.lower().strip():
        print("Wake word detected. Please speak your prompt to TalkingWithTrains.")
        LEDController.activation_word_detected()
        listening_for_wake_word = False


def prompt(audio):
    global listening_for_wake_word

    try:
        if args.wav:
            prompt_text = transcribe(audio, "prompt.wav")
        else:
            prompt_text = transcribe(audio)

        if len(prompt_text.strip()) == 0:
            print("Empty prompt. Please speak again.")
            LEDController.command_not_recognized()
            listening_for_wake_word = True
        else:
            result = extract_activity(prompt_text)
            if result == "COMMAND_EXECUTED_SUCCESSFULLY":
                LEDController.command_executed()
            elif result == "CONNECTION_ERROR":
                LEDController.connection_failed()
            elif result == "COMMAND_NOT_FOUND":
                LEDController.command_not_recognized()

            activate_voice_control()

    except Exception as e:
        print("Prompt error: ", e)
        LEDController.command_not_recognized()

        activate_voice_control()


def callback(recognizer, audio):
    global listening_for_wake_word

    if listening_for_wake_word:
        listen_for_wake_word(audio)
    else:
        prompt(audio)


def start_listening():
    with source as s:
        if args.energy_threshold:
            recognizer.energy_threshold = args.energy_threshold
        else:
            print("Adjusting for ambient noise, please be quiet for a moment.")
            recognizer.adjust_for_ambient_noise(s, duration=2)

    print("Energy threshold: ", recognizer.energy_threshold)

    activate_voice_control()

    recognizer.listen_in_background(source, callback, phrase_time_limit=3)

    while True:
        time.sleep(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Voice control for TalkingWithTrains')
    parser.add_argument('--energy_threshold', type=int, help='Energy threshold for audio recognition')
    parser.add_argument('--wav', type=bool, default=False, help='Create wav files for debugging purposes')
    args = parser.parse_args()

    http_client.get_hash()
    start_listening()
