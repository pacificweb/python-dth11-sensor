#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import logging
import time
from datetime import datetime
import Adafruit_DHT

log = logging.getLogger(__name__)

def main(args=None):

    _filename=datetime.now().strftime('%Y%m%d.csv')
    logging.basicConfig(filename=_filename,datefmt='%Y-%m-%d %H:%M:%S',format='%(asctime)s;%(message)s',level=logging.DEBUG)

    try:
        # GPIO17, GPIO27
        # Pin 11, Pin 13
        pins = [17, 27]
        while True:
            for pin in pins:
                humidity, temperature = Adafruit_DHT.read_retry(11, pin)
                if humidity is not None and temperature is not None:
                    print(format(temperature, '.1f'))
                    print(format(humidity, '.1f'))
                    #log.info('{0:0,.1f};{1:0,.1f}'.format(temperature, humidity).replace('.',','))
                else:
                    print('Read error on pin number ' + pin)
                    #log.info('{0:0.1f};{1:0.1f}'.format(0, 0).replace('.',','))
            time.sleep(10)
    except (KeyboardInterrupt):
        print('T:{0:0.1f};H:{1:0.1f}'.format(0, 0).replace('.',','))
        #log.info('{0:0.1f};{1:0.1f}'.format(0, 0).replace('.',','))
    finally:
        sys.exit()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]) or 0)
