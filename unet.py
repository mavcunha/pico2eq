import time
import network
import utils

class Wifi:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

    def connect(self):
        self.wlan.connect(self.ssid, self.password)
        max_wait = 10
        while max_wait > 0:
            if self.wlan.status() < 0:
                utils.blink(3)
                raise RuntimeError('connection failed.')
            elif self.wlan.status() >= 3:
                break
            max_wait -= 1
            print('waiting for connection...')
            utils.wait(1)
            
    def disconnect(self):
        self.wlan.disconnect()

    def is_connected(self):
        return self.wlan.status() == 3