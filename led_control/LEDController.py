from sys import platform

def is_platform_linux():
    return platform == "linux" or platform == "linux2"

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


    def set_color(r, g, b):
        for x in range(LED_COUNT):
            strip.setPixelColor(x, Color(r, g, b))
        strip.show()


    def voice_control_inactive():
        set_color(0, 0, 0)  # LEDs off

    def voice_control_active():
        set_color(255, 255, 255)  # LEDs white

    def activation_word_detected():
        set_color(0, 0, 255)  # LEDs blue

    def processing_command():
        set_color(0, 255, 255)  # LEDs cyan

    def command_executed():
        set_color(0, 255, 0)  # LEDs green

    def command_not_recognized():
        set_color(255, 0, 0)  # LEDs red

    def connection_failed():
        set_color(255, 255, 0)  # LEDs yellow

    def no_microphone_detected():
        set_color(255, 165, 0)  # LEDs orange

except ImportError:
    pass

