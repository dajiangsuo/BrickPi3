#!/usr/bin/env python
#
# https://www.dexterindustries.com/BrickPi/
# https://github.com/DexterInd/BrickPi3
#
# Copyright (c) 2016 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information, see https://github.com/DexterInd/BrickPi3/blob/master/LICENSE.md
#
# This code is an example for reading an EV3 infrared sensor connected to PORT_1 of the BrickPi3
# 
# Hardware: Connect an EV3 infrared sensor to BrickPi3 sensor port 1.
# 
# Results:  When you run this program, the infrared remote status will be printed.

from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

# Configure for an EV3 color sensor.
# BP.set_sensor_type configures the BrickPi3 for a specific sensor.
# BP.PORT_1 specifies that the sensor will be on sensor port 1.
# BP.Sensor_TYPE.EV3_INFRARED_REMOTE specifies that the sensor will be an EV3 infrared sensor.
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_INFRARED_REMOTE)

try:
    while True:
        # BP.get_sensor retrieves a sensor value.
        # BP.PORT_1 specifies that we are looking for the value of sensor port 1.
        # BP.get_sensor returns a list of two values.
        #     The first item in the list is a list of the sensor values (what we want to display).
        #     The second item in the list is the error value (should be equal to BP.SUCCESS if the sensor is configured and the value was read successfully)
        print(BP.get_sensor(BP.PORT_1)[0]) # print the infrared remote values
        
        time.sleep(0.02)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()        # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.