import urequests as requests

CO2SIGNAL_URL='http://api.co2signal.com/v1/latest'

class CO2Signal:
    def __init__(self, token, lon, lat):
        self._headers = { 'auth-token': token }
        self._lon = lon
        self._lat = lat

        
    def intensity(self):
        result = requests.get(f'{CO2SIGNAL_URL}?lon={self._lon}&lat={self._lat}',
                     headers = self._headers)
        if result.status_code == 200:
            json = result.json()
            return Intensity(
                json['data']['carbonIntensity'],
                json['units']['carbonIntensity'],
                json['data']['fossilFuelPercentage'])
        else:
            raise ValueError(f'request failed status={result.status_code} reason={result.reason}')
    
    
class Intensity:
    def __init__(self, intensity, unit, percentage):
        self.value = intensity
        self.unit = unit
        self.fossil = percentage
        self.renewables = 100 - self.fossil

    def __repr__(self):
        return f'Intensity({self.value=},{self.unit=},{self.fossil=},{self.renewables=})'
