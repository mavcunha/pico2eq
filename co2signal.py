import urequests as requests

CO2SIGNAL_URL='http://api.co2signal.com/v1/latest'

class CO2Error(Exception):
    """raised when we fail to fetch data from co2signal"""

class CO2Signal:
    def __init__(self, token, lon, lat):
        self._headers = { 'auth-token': token }
        self._lon = lon
        self._lat = lat
        self._last = None


    def intensity(self):
        result = requests.get(f'{CO2SIGNAL_URL}?lon={self._lon}&lat={self._lat}',
                     headers = self._headers)
        if result.status_code == 200:
            json = result.json()
            self._last = Intensity(
                intensity=json['data']['carbonIntensity'],
                unit=json['units']['carbonIntensity'],
                percentage=json['data']['fossilFuelPercentage'],
                date=json['data']['datetime'])
            return self._last
        else:
            raise CO2Error(f'request failed status={result.status_code} reason={result.reason}')

    def last_reading(self):
        """last reading"""
        return self._last


class Intensity:
    def __init__(self, intensity, unit, percentage, date):
        self.value = intensity
        self.unit = unit
        self.fossil = percentage
        self.renewables = 100 - self.fossil
        self.date = date

    def __repr__(self):
        return f'Intensity({self.value=},{self.unit=},{self.fossil=},{self.renewables=},{self.date=})'
