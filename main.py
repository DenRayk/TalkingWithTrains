import sounddevice as sd
import whisper
import time

from datetime import datetime
from os.path import abspath, dirname, join, exists
from scipy.io.wavfile import write

model = whisper.load_model("base")

# Sampling frequency
# Regardless of the sampling rate used in the original audio file,
# the audio signal gets resampled to 16kHz (via ffmpeg). Anything grater than 16kHz should work.
# see https://github.com/openai/whisper/discussions/870.
freq = 44100

# Recording duration in seconds
duration = int(input("select duration of the audio: "))

# Start recorder with the given values of
# duration and sample frequency.

recording = sd.rec(int(duration * freq),
                   samplerate=freq, channels=2)

# Record audio for the given number of seconds
sd.wait()

date = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
audioPath = join(dirname(abspath(__file__)), "prompts", f"prompt_{date}.wav")

write(audioPath, freq, recording)

result = model.transcribe(audioPath)

print(result)
