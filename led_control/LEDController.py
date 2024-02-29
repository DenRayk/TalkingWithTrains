from sys import platform
from led_control import ColorStatus

try:
    from rpi_ws281x import PixelStrip, Color

    LED_COUNT = 4
    LED_PIN = 18
    LED_FREQ_HZ = 800000
    LED_DMA = 10
    LED_BRIGHTNESS = 255
    LED_INVERT = False
    LED_CHANNEL = 0

    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

except ImportError:
    pass

def set_led_color(r, g, b):
    if not platform.startswith("linux"):
        return

    try:
        for x in range(LED_COUNT):
            strip.setPixelColor(x, Color(r, g, b))
        strip.show()
    except:
        pass

def voice_control_inactive():
    set_led_color(*ColorStatus.OFF)
    print("Color set to off")

def voice_control_active():
    set_led_color(*ColorStatus.ACTIVE)
    print("Color set to White")

def activation_word_detected():
    set_led_color(*ColorStatus.DETECTED)
    print("Color set to Blue")

def processing_command():
    set_led_color(*ColorStatus.PROCESSING)
    print("Color set to Cyan")

def command_executed():
    set_led_color(*ColorStatus.EXECUTED)
    print("Color set to Green")

def command_not_recognized():
    set_led_color(*ColorStatus.NOT_RECOGNIZED)
    print("Color set to Red")

def connection_failed():
    set_led_color(*ColorStatus.CONNECTION_FAILED)
    print("Color set to Yellow")
def no_microphone_detected():
    set_led_color(*ColorStatus.NO_MICROPHONE)
    print("Color set to Orange")
