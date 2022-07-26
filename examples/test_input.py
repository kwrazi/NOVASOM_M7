# Import modules
import time
import NOVASOM_M7.GPIO as GPIO
from NOVASOM_M7.GPIO import ACT_HIGH, ACT_LOW

# Select nummbering scheme BOARD (GPIO number will correspond to physical pin number of J9 connection on M7 board)
GPIO.setmode(GPIO.BOARD)

# Set warning mode
GPIO.setwarnings(True)

while True:
    sCh = input("Enter GPIO pin: ")
    if not sCh.isnumeric():
        continue
    iCh = int(sCh)
    if iCh == 0:
        exit(0)
    if iCh > 40:
        continue
    if not GPIO.setup(iCh, GPIO.IN, act_high_low=ACT_HIGH):
        continue
    for x in range(10):
        print ("Value:{}".format(GPIO.input(iCh)))
        time.sleep(1)
    GPIO.cleanup(iCh)

