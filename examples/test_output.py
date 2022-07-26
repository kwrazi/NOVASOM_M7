# Import modules
import time
import NOVASOM_M7.GPIO as GPIO

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
    if not GPIO.setup(iCh, GPIO.OUT, initial=GPIO.LOW):
        continue
    for x in range(5):
        time.sleep(0.5)
        GPIO.output(iCh, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(iCh, GPIO.LOW)
    GPIO.cleanup(iCh)

