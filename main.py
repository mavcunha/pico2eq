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
    if button_a.read():
        display.warn('reseting...')
        wait(1)
        machine.reset()

def refresh(timer):
    if button_b.read():
        display.dot_ok()

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
                display.error('connecting...error')
                wait(10, display.blink_err) # wait 10s before retry


if __name__ == '__main__':
    machine.Timer(-1, period=83, mode=Timer.PERIODIC, callback=reset)
    machine.Timer(-1, period=89, mode=Timer.PERIODIC, callback=refresh)
    main()
