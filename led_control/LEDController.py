import threading
from sys import platform
from led_control import ColorStatus

timer = None

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

except Exception as e:
    print("Error initializing LED strip: ", e)


def set_led_color(r, g, b):
    if not platform.startswith("linux"):
        return False

    try:
        for x in range(LED_COUNT):
            strip.setPixelColor(x, Color(r, g, b))
        strip.show()
    except Exception as e:
        print("Error setting LED color: ", e)
        return False
    return True


def cancel_timer():
    global timer
    if timer is not None and timer.is_alive():
        timer.cancel()
        print("Timer cancelled")


def voice_control_inactive():
    cancel_timer()
    if set_led_color(*ColorStatus.OFF):
        print("Color set to off")


def voice_control_active():
    global timer
    cancel_timer()
    timer = threading.Timer(5, lambda: set_led_color(*ColorStatus.ACTIVE) and print("Color set to White"))
    timer.start()


def activation_word_detected():
    cancel_timer()
    if set_led_color(*ColorStatus.DETECTED):
        print("Color set to Blue")


def command_executed():
    cancel_timer()
    if set_led_color(*ColorStatus.EXECUTED):
        print("Color set to Green")


def command_not_recognized():
    cancel_timer()
    if set_led_color(*ColorStatus.NOT_RECOGNIZED):
        print("Color set to Red")


def connection_failed():
    cancel_timer()
    if set_led_color(*ColorStatus.CONNECTION_FAILED):
        print("Color set to Yellow")

