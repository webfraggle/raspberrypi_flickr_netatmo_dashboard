#!/usr/bin/python
#--------------------------------------
#
#              ds18b20.py
#  Read DS18B20 1-wire temperature sensor
#
# Author : Matt Hawkins
# Date   : 10/02/2015
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import Adafruit IO REST client.
from Adafruit_IO import Client

from settings import *

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_KEY)

def gettemp(id):
  try:
    mytemp = ''
    filename = 'w1_slave'
    f = open('/sys/bus/w1/devices/' + DS18B20_ID+ '/' + filename, 'r')
    line = f.readline() # read 1st line
    crc = line.rsplit(' ',1)
    crc = crc[1].replace('\n', '')
    if crc=='YES':
      line = f.readline() # read 2nd line
      mytemp = line.rsplit('t=',1)
    else:
      mytemp = None
    f.close()

    return int(mytemp[1])

  except:
    return None

if __name__ == '__main__':

  # Script has been called directly
  temp = gettemp(id)/float(1000); 
  if temp is not None:
      print "Temp : " + '{:.3f}'.format(temp)
      aio.send('temperature1',temp)
