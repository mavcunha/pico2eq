from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4
from pimoroni import RGBLED

_DISPLAY = PicoGraphics(display=DISPLAY_PICO_DISPLAY, rotate=0, pen_type=PEN_P4)

WHITE = _DISPLAY.create_pen(255, 255, 255)
RED   = _DISPLAY.create_pen(255, 0, 0)
BLACK = _DISPLAY.create_pen(0, 0, 0)
CYAN = _DISPLAY.create_pen(0, 255, 255)
MAGENTA = _DISPLAY.create_pen(255, 0, 255)
YELLOW = _DISPLAY.create_pen(255, 255, 0)
GREEN = _DISPLAY.create_pen(0, 255, 0)

_LED = RGBLED(6, 7, 8)

class Display:
    def __init__(self):
        _DISPLAY.set_backlight(0.5)
        _DISPLAY.set_font('sans')
    
    def clear(self):
        _DISPLAY.set_pen(BLACK)
        _DISPLAY.clear()
        _DISPLAY.update()

    def text(self, msg, color=WHITE):
        self.clear()
        _DISPLAY.set_pen(color)
        _DISPLAY.text(msg, 2, 20, 240, 1)
        _DISPLAY.update()

    def error(self, msg):
        self.text(msg, color=RED)

    def warn(self, msg):
        self.text(msg, color=YELLOW)

    def _refresh_led(self, renewables):
        if renewables < 50:
            _LED.set_rgb(255, 0, 0)
        else:
            _LED.set_rgb(0, 255, 0)

    def intensity(self, int):
        self.clear()
        _DISPLAY.set_pen(WHITE)
        _DISPLAY.text(f'{int.value} g/kWh', 2, 16, 240, 1)
        _DISPLAY.text(f'{int.renewables} %', 2, 56, 240, 1)
        self._refresh_led(int.renewables)
        _DISPLAY.update()
