import machine
import time


LED = machine.Pin("LED", machine.Pin.OUT)


def blink(times=3, short=100, long=0):
    for _ in range(times):
        LED.toggle()
        time.sleep_ms(short)
    time.sleep(long)

def wait(secs=300, callback=None):
    for _ in range(secs):
        blink(1, long=1)
        if callback:
            callback()
