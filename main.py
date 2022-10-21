from utils import blink, wait
from config import Config
from machine import Timer
from display import Display
from unet import Wifi
from co2signal import CO2Signal, Intensity
from pimoroni import Button

conf = Config.load('config.json')

button_a = Button(12)

display = Display()
wifi = Wifi(conf.ssid, conf.pwd)
co2s = CO2Signal(conf.token, conf.lon, conf.lat)

def reset(timer):
    if button_a.read():
        display.warn('reseting...')
        wait(1)
        machine.reset()

def main():
    blink(2, short=1000) # 2 long = booting
    while True:
        if wifi.is_connected():
            try:
                blink(2, short=100) # 2 short updating
                display.warn('updating...')
                intensity = co2s.intensity()
                display.intensity(intensity)
                wait(300) # wait 5 min
            except ValueError as e:
                print(e)
                display.error('updating...failed')
                wait(10) # wait 10 seconds before retry
        else:
            try:
                display.warn('connecting...')
                wifi.connect()
            except RuntimeError as e:
                print(e)
                display.error('connecting...failed')


if __name__ == '__main__':
    timer = machine.Timer(-1)
    timer.init(period=500, mode=Timer.PERIODIC, callback=reset)
    main()
