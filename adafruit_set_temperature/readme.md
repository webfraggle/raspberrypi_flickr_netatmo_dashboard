# Send Temperature from DS18B20 to Adafruit IO with Raspberry Pi

## Requirements

*Working Adafruit IO Python Client Library
https://github.com/adafruit/io-client-python
*Adafruit IO account and io key
*Working DS18B20 sensor
http://www.raspberrypi-spy.co.uk/2013/03/raspberry-pi-1-wire-digital-thermometer-sensor/

## Settings
Just set your Adafruit IO key and the sensor's id in settings.py

## Cronjob
To start the python program every minute and send it to adafruit use Crontab
Use `crontab -e`
and add this line 
`*/1 * * * *     /home/pi/temperature.io/ds18b20.py`