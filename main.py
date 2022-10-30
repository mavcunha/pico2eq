from utils import blink, wait
from config import Config
from machine import Timer
from display import Display
from unet import Wifi
from co2signal import CO2Signal, Intensity
from pimoroni import Button

conf = Config.load('config.json')

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

display = Display()
wifi = Wifi(conf.ssid, conf.pwd)
co2s = CO2Signal(conf.token, conf.lon, conf.lat)


def reset(timer):
    """causes pico to reset"""
    if button_a.read():
        display.warn('reseting...')
        wait(1)
        machine.reset()

def display_date(timer):
    """display date in the last reading"""
    if button_b.read():
        last = co2s.last_reading()
        display.text(last.date.split('T'))
        wait(2, display.blink_warn)
        display.intensity(last)

def force_refresh(timer):
    """force refresh"""
    if button_x.read():
        display.warn('refreshing...')
        try:
            intensity = co2s.intensity()
            display.intensity(intensity)
        except ValueError as e:
            print(e)
            wait(10, display.blink_err) # wait 10s before retry


def main():
    blink(2, short=1000) # 2 long = booting
    while True:
        if wifi.is_connected():
            try:
                blink(2, short=100) # 2 short updating
                display.dot_warn()
                intensity = co2s.intensity()
                display.intensity(intensity)
                wait(300, display.blink_dot) # wait 5 min
            except ValueError as e:
                print(e)
                wait(10, display.blink_err) # wait 10s before retry
        else:
            try:
                display.warn('connecting...')
                wifi.connect()
            except RuntimeError as e:
                print(e)
                display.error('connecting...')
                wait(10, display.blink_err) # wait 10s before retry


if __name__ == '__main__':
    machine.Timer(-1, period=83, mode=Timer.PERIODIC, callback=reset)
    machine.Timer(-1, period=89, mode=Timer.PERIODIC, callback=display_date)
    machine.Timer(-1, period=97, mode=Timer.PERIODIC, callback=force_refresh)
    main()
