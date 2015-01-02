#!/usr/bin/python
import Adafruit_DHT
import sqlite3
import datetime

sensor = Adafruit_DHT.DHT11
pin = '4'

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

i = 0
hum = 0
temp = 0

while i < 5:
        if humidity is not None and temperature is not None:
                hum += humidity
                temp += temperature
                i += 1

hum = hum/5
temp = temp/5

try:
        conn = sqlite3.connect('/home/pi/weather.db3')
        c = conn.cursor()
        c.execute("INSERT INTO weather (temp, hum) VALUES ({0}, {1})".format(temp, hum))
        conn.commit()
        conn.close()
except:
        f = open('weather.log', 'w')
        f.write('Error ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        f.close()
