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

    pwm=GPIO.PWM(iCh, 60)                                # Create PWM object/instance
    print("#### PWM Output - DutyCycle - High Precision ####")
    print("60Hz at 50% duty cycle for 3 seconds")
    pwm.start(50)
    time.sleep(3)
    print("60Hz at 25% duty cycle for 3 seconds")
    pwm.ChangeDutyCycle(25)
    time.sleep(3)
    print("60Hz at 10% duty cycle for 3 seconds")
    pwm.ChangeDutyCycle(10)
    time.sleep(3)
    print("60Hz at  1% duty cycle for 3 seconds")
    pwm.ChangeDutyCycle(1)
    time.sleep(3)
    print("60Hz at 50% duty cycle for 3 seconds")
    pwm.ChangeDutyCycle(50)
    time.sleep(3)
    print("30Hz at 50% duty cycle for 3 seconds")
    pwm.ChangeFrequency(30)
    time.sleep(3)
    print("10Hz at 50% duty cycle for 3 seconds")
    pwm.ChangeFrequency(10)
    time.sleep(3)
    print("3Hz at 50% duty cycle for 3 seconds")
    pwm.ChangeFrequency(3)
    pwm.stop()
    GPIO.cleanup(iCh)

