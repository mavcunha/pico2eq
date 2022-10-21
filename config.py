import json

class Config:

    def __init__(self, ssid, pwd, token, lat, lon):
        # wifi
        self.ssid = ssid
        self.pwd = pwd
        # co2signal
        self.token = token
        self.lat = lat
        self.lon = lon
    
    @classmethod
    def load(cls, file):
        with open(file, 'r') as f:
            conf = json.load(f)
            return Config(
                ssid=conf['wifi']['ssid'],
                pwd=conf['wifi']['password'],
                token=conf['co2signal']['token'],
                lon=conf['co2signal']['longitude'],
                lat=conf['co2signal']['latitude'])
