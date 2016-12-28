# https://www.dexterindustries.com/BrickPi/
# https://github.com/DexterInd/BrickPi3
#
# Copyright (c) 2016 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information, see https://github.com/DexterInd/BrickPi3/blob/master/LICENSE.md
#
# This code is an example for reading an NXT color sensor with RED LED connected to PORT_1 of the BrickPi3

from __future__ import print_function
from __future__ import division

import time
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.NXT_COLOR_RED) # Configure for an NXT color sensor with RED LED.

try:
    while True:
        print(BP.get_sensor(BP.PORT_1)[0]) # read and display the sensor value
        time.sleep(0.02)                   # delay 20ms
except KeyboardInterrupt:
    BP.reset_all()