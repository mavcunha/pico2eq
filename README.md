## Pico2eq - A carbon intensity monitor

![](https://uat.marcovaltas.com/assets/img/posts/pico/pico_green.jpeg)

This is a hack project to create a small Carbon Intensity Monitor using
[Raspberry Pi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/) 
and data from [CO2 signal](https://www.co2signal.com/). Information on how to put this
together can be found
[here](https://uat.marcovaltas.com/2022/10/29/pico2eq.html).

### Configuration

This code relies on a configuration file called `config.json`, here's a template:

```json
{
  "wifi": {
    "ssid": "YOUR_WIFI_NAME",
    "password":"YOUR_WIFI_PASSWORD"
  },
  "co2signal": {
    "token": "YOUR_API_TOKEN",
    "longitude": YOUR_LONGITUDE,
    "latitude": YOUR_LATITUDE
  }
}
```

### Functions on buttons

* button a: reset the Pico
* button b: display the update date from CO2 signal
* button x: force refresh the data

### Pico led behavior

The Pico led should be blinking all the time at 1 second intervals. This is
an indicator that the program is alive and running. If you notice the led stuck
on or off, reset the Pico. Other blinks:

* 2 long blinks: starting the program
* 3 short blinks: connecting to the WiFi
* 2 short blinks: updating the data
* continuous 1 sec blink: waiting

### Display indicators

At the corner of the display you have a continuous blink, similar to the led above. 
But it will change colors depending on the program status.

* white circle: waiting
* yellow circle: warning
* red circle: error

The Yellow and Red are normal conditions that the program will handle. If they persist
for too long that might indicate a problem reaching the internet, connecting to the WiFi
or getting the data from CO2 signal.


