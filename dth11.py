#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import logging
import Adafruit_DHT

log = logging.getLogger(__name__)

def main(args=None):

    logging.basicConfig(filename='values.csv',datefmt='%Y-%m-%d %H:%M:%S',format='%(asctime)s;%(message)s',level=logging.DEBUG)

    try:
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(11, 4)
            if humidity is not None and temperature is not None:
                print('T:{0:0.1f};H:{1:0.1f}%'.format(temperature, humidity).replace('.',','))
                log.info('{0:0,.1f};{1:0,.1f}'.format(temperature, humidity).replace('.',','))
            else:
                log.info('{0:0.1f};{1:0.1f}'.format(0, 0).replace('.',','))
    except (KeyboardInterrupt):
        log.info('{0:0.1f};{1:0.1f}'.format(0, 0).replace('.',','))
    finally:
        sys.exit()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]) or 0)