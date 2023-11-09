import speech_recognition as sr
import sys
import time

keyword = ["merklin", "märklin", "merkel"]

recognizer = sr.Recognizer()


def speech_to_text(audio):
    # Test speed of speech recognition
    start = time.time()
    text = recognizer.recognize_vosk(audio, language="de-DE")
    end = time.time()
    print("Time spent for recognition: {}".format(end - start))
    return text.lower()


def listen_for_wakeword():
    while True:

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            print("Listening for wakeword...")
            audio = recognizer.listen(source)

        try:
            text = speech_to_text(audio)
            print("You said: {}".format(text))

            if text in keyword:
                listen_for_command()
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))


def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)

        text = speech_to_text(audio)

        if text is not None:
            print("You said: {}".format(text))
            process_command(text)
        else:
            print("Could not understand audio")


def process_command(text):
    print("Processing command...")
    # TODO: Add code to process commands


while True:
    try:
        listen_for_wakeword()
    except KeyboardInterrupt:
        sys.exit(0)
