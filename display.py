from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4
from pimoroni import RGBLED

from ui import Chart

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
        self.chart = Chart(display_height=135)
        self.dot_on = False
        _LED.set_rgb(0, 0, 0) # RGB led off
        _DISPLAY.set_backlight(0.5)
        _DISPLAY.set_font('sans')
        self.clear()
    
    def clear(self):
        _DISPLAY.set_pen(BLACK)
        _DISPLAY.clear()
        _DISPLAY.update()

    def text(self, msg, color=WHITE):
        print(msg) # show on console too
        self.clear()
        _DISPLAY.set_pen(color)
        _DISPLAY.text(msg, 2, 20, 240, 1)
        _DISPLAY.update()

    def error(self, msg):
        self.text(msg, color=RED)

    def warn(self, msg):
        self.text(msg, color=YELLOW)

    def dot(self, color):
        _DISPLAY.set_pen(color)
        _DISPLAY.circle(236,4,4)
        _DISPLAY.update()

    def dot_err(self):
        self.dot(RED)

    def dot_warn(self):
        self.dot(YELLOW)

    def dot_ok(self):
        self.dot(GREEN)

    def blink_err(self):
        self.blink_dot(RED)

    def blink_warn(self):
        self.blink_dot(YELLOW)

    def blink_dot(self, color=MAGENTA):
        if self.dot_on: 
            self.dot_on = False
            self.dot(BLACK)
        else:
            self.dot_on = True
            self.dot(color)
        
    def _column_color(self, height):
        if height < 31:
            return RED
        else:
            return GREEN

    def _refresh_led(self, renewables):
        if renewables < 50:
            _LED.set_rgb(55, 0, 0)
        else:
            _LED.set_rgb(0, 55, 0)

    def _draw_values(self, intensity):
        _DISPLAY.set_pen(WHITE)
        _DISPLAY.text(f'{intensity.value} g/kWh', 2, 16, 240, 1)
        _DISPLAY.text(f'{intensity.renewables} %', 2, 56, 240, 1)

    def _draw_chart(self, renewables):
        _DISPLAY.set_pen(WHITE)
        _DISPLAY.line(0, 72, 250, 72)
        self.chart.add(renewables)
        for (x, y, w, h) in self.chart.render():
            _DISPLAY.set_pen(self._column_color(h))
            _DISPLAY.rectangle(x, y, w, h)

    def intensity(self, intensity):
        print(intensity) # show on console
        self.clear()
        self._draw_values(intensity)
        self._draw_chart(intensity.renewables)
        self._refresh_led(intensity.renewables)
        _DISPLAY.update()
