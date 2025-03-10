from hx711_multi import HX711
from time import perf_counter
import RPi.GPIO as GPIO  # import GPIO
from array import *

GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering 
readings_to_average = 10
sck_pin = 6
weight_multiple = array("f", [])
dout_pins = [17]  # 1, 2, 3, 4 [22, 4, 17, 27]
for i in range(0, 4):
    Cell = int(input("What Load cell do you want to calibrate (1-4)"))
    if (Cell == 1):
        dout_pins = [22]
        cell = 0
    if (Cell == 2):
        dout_pins = [4]
        cell = 1
    if (Cell == 3):
        dout_pins = [17]
        cell = 2
    if (Cell == 4):
        dout_pins = [27]
        cell = 3

    hx711 = HX711(dout_pins=dout_pins,
                  sck_pin=sck_pin,
                  channel_A_gain=64,
                  channel_select='A',
                  all_or_nothing=False,
                  log_level='CRITICAL')

    # reset ADC, zero it
    hx711.reset()

    cal = hx711.run_calibration(known_weights=[1, 2, 5, 10])
    weight_multiple.append(cal)
    print(f'Weight multiple = {weight_multiple[cell]}')

cell = 0
for i in range(0, 4):
    print(f'Weight multiple = {weight_multiple[cell]}')
    cell = cell + 1
