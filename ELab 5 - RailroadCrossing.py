#############################################
# Filename: ELab 5 - RailroadCrossing.py
# Developer: BSides Augusta STEM
# Language: Python 3.4
# Description: This program will make the Raspberry Pi 3
# a railroad crossing sign light controller. The two Red
# LEDs will alternate the flash back and forth. Each LED
# will stay on for 3 seconds at a time. After 18 seconds,
# both LEDs should stay on for 10 seconds. This program
# runs in an infinite loop.

#############################################
# Import Classes
#############################################
# Import Time Class
import time

# Import Raspberry Pi General Purpose Input & Output Class
import RPi.GPIO as GPIO

#############################################
# Initialization
#############################################
# Configure LED ON Time in Seconds
LEDredOnTime = 3.0
LEDBothOnTime = 10.0

# Configure LED Variables to GPIO Pins
LEDred1 = 16
LEDred2 = 20

# Config to Refer to GPIO by Pin Number
GPIO.setmode(GPIO.BCM)

# Configure GPIO Pins to Outputs
GPIO.setup(LEDred1,GPIO.OUT)
GPIO.setup(LEDred2,GPIO.OUT)

#############################################
# Main Program
#############################################
# Run the code until the CTL+C buttons end the program.
# The the try...except handles the keyboard interruption
# with the CTL+C button press, it allows the programmer
# to shut down the program in a more graceful & safer way.

print ('Press CTL+C to Shut Down the Stoplight Program')
try:
        # Run the Loop Continuously
        while(1):
                # Red LED1 ON & Red LED2 OFF
                GPIO.output(LEDred1, True)
                GPIO.output(LEDred2, False)
                print ('Red LED1 ON & Red LED2 OFF for',LEDredOnTime,'seconds')
                time.sleep(LEDredOnTime)

                # Red LED1 OFF & Red LED2 ON
                GPIO.output(LEDred1, False)
                GPIO.output(LEDred2, True)
                print ('Red LED1 OFF & Red LED2 ON for ',LEDredOnTime,'seconds')
                time.sleep(LEDredOnTime)

            
# The exception section is called whenever a keyboard interrupt happens.
# This allows you to control how gracefully the program shuts down.
except KeyboardInterrupt:

        # Safety Shut Down Configuration for the Raspberry Pi.
        # The cleanup() method sets all initialized GPIO outputs back to
        # input pins. This will prevent you from accidentally shorting out
        # an output pin to ground during the electronic breadboarding
        # process. All GPIO pins should be configured to inputs when the
        # program is not running.
        GPIO.cleanup() 

        # Output the Shut Down Message
        print ('Program has been properly shut down. Goodbye!')
