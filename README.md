# M7_GPIO
A Python GPIO library for the Novasom M7 single-board computer.<br />
It has been inspired to similar [RPi.GPIO](https://sourceforge.net/projects/raspberry-gpio-python/) library).

## Importing the module
To import the NOVASOM_M7.GPIO module:

    import NOVASOM_M7.GPIO as GPIO

By doing it this way, you can refer to it as just GPIO through the rest of your script.

## Pin numbering
There are two ways of numbering the IO pins on a NOVASOM M7 board within NOVASOM_M7.GPIO:
1. BOARD numbering system. This refers to the pin numbers on the P1 header of the M7 board. The advantage of using this numbering system is that your hardware will always work, regardless of the board revision of the NOVASOM_M7.
To select this numbering scheme use

        GPIO.setmode(GPIO.BOARD)

2. RK3328 gpio numbering. This is a lower level way of working: it refers to the gpio channel numbers on Rockchip RK3328 SoC.
To specify which you are using using (mandatory):
To select this numbering scheme use:

        GPIO.setmode(GPIO.RK)

To detect which pin numbering system has been set (for example, by another Python module) use:

    mode = GPIO.getmode()

## Warnings
This library can provide some warning printouts (i.e. when you are trying to setup a GPIO channel that has alreaby been taken).

Warnings are enabled by default; you can disable them with:

    GPIO.setwarnings(False)

## Setup up a channel
You need to set up every channel you are using as an input or an output. To configure a channel as an input:

    GPIO.setup(channel, GPIO.IN)

where channel is the channel number according to the numbering scheme you have specified (BOARD or RK).

To set up a channel as an output:

    GPIO.setup(channel, GPIO.OUT)

where channel is the channel number according to the numbering scheme you have specified (BOARD or RK).

You can also specify an initial value for your output channel:

    GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)

For input channels you can also specify if the input has to considered active high (default) or active low:

    GPIO.setup(channel, GPIO.IN, act_high_low=ACT_LOW):

### Setup more than one channel
You can set up more than one channel using a single call. Example:

    chan_list = [11,12]    # add as many channels as you want!
                           # you can tuples instead i.e.:
                           #   chan_list = (11,12)
    GPIO.setup(chan_list, GPIO.OUT)

## Input channels
To read the value of a GPIO channel:

    GPIO.input(channel)

where channel is the channel number according to the numbering scheme you have specified (BOARD or RK).
This will return either 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True

## Output channels
To set the output state of a GPIO channel:

    GPIO.output(channel, state)

where *channel* is the channel number according to the numbering scheme you have specified (BOARD or RK).

*state* can be 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.

You can also output to many channels in the same call, example:

    chan_list = [11,12]                             # also works with tuples
    GPIO.output(chan_list, GPIO.LOW)                # sets all to GPIO.LOW
    GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW))   # sets first HIGH and second LOW

## PWM
Each GPIO channel can be configured for software PWM mode.

    pwm=GPIO.PWM(channel, frequency)

where *channel* is the channel number according to the numbering scheme you have specified (BOARD or RK).

*frequency* is the expected PWM frequency in Hz

This function will return a instance to a GPIO.PWM class that can be used for other methods call.

### PWM start

    pwm.start(dutycycle)

where *dutycycle* is the expected dutycycle

This will start the PWM output at desired frequency and dutycycle

### Frequency change

    pwm.ChangeFrequency(frequency)

where *frequency* is the new expected PWM frequency in Hz

### Duty-cycle change

    pwm.ChangeDutyCycle(dutycycle)

where *dutycycle* is the new expected dutycycle

### PWM stop

    pwm.stop()

## Cleanup
At the end any program, it is good practice to release up any resources you might have used.<br />
This can avoid accidental damage to your NOVASOM M7 board by shorting out the pins stil,l configured as outputs when you change your hardware setup.<br />
To clean up at the end of your script:

    GPIO.cleanup()

Note that this will only clean up GPIO channels that your script has used; Note also that GPIO.cleanup() clears the pin numbering system in use as well.

It is possible that don't want to clean up every channel leaving some set up when your program exits. You can clean up individual channels, a list or a tuple of channels:

    GPIO.cleanup(channel)
    GPIO.cleanup( (channel1, channel2) )
    GPIO.cleanup( [channel1, channel2] )

# Resources
List of resources and reference material used while building the scripts and libraries in this repository
* [Kernel.org - GPIO/SYSFS Documentation](https://www.kernel.org/doc/Documentation/gpio/sysfs.txt)
* [Novasom Website ](http://www.novasomindustries.com)

# Credits
Initially developed by [Pier Francesco Maria Santi](https://www.linkedin.com/in/pierfrancescomariasanti/) aka PFM (pfm.santi@hexcape.com)

Rewieved by [Paolo Geninatti](mailto:tech@pagit.eu) - [Pagit](http://www.pagit.eu)
