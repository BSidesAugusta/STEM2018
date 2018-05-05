#############################################
# Filename: ELab 3 - RedLEDFlash.py
# Developer: BSides Augusta STEM
# Language: Python 3.4
# Description: This program will make the Raspberry Pi flash
# the Red LED ON for 5 seconds and then OFF for 3 seconds.
# This program runs in an infinite loop until CTL-C is pressed.

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
# Configure LED ON/OFF Times in Seconds
LEDredOnTime = 5.0
LEDredOffTime = 3.0

# Configure LED Variable to GPIO Pins
LEDred = 16

# Config to Refer to GPIO by Pin Number
GPIO.setmode(GPIO.BCM)

# Configure GPIO Pins to Outputs
GPIO.setup(LEDred,GPIO.OUT)

#############################################
# Main Program
#############################################
# Run the code until the CTL+C buttons end the program.
# The the try...except handles the keyboard interruption
# with the CTL+C button press, It allows the program to
# shutdown the program in a more graceful & safer way.

print ('Press CTL+C to Shutdown the Red Flashing LED Program')
try:
        # Run the Loop Continuously
        while(1):
                # Turn ON the Red LED
                GPIO.output(LEDred, True)
                print ('Red LED ON for',LEDredOnTime,'seconds')
                time.sleep(LEDredOnTime)
				
		# Turn OFF the Red LED
                GPIO.output(LEDred, False)
                print ('Red LED OFF for',LEDredOffTime,'seconds')
                time.sleep(LEDredOffTime)

# The exception section is called whenever a keyboard interrupt happens.
# This allows you to control how gracefully the program shuts down.
except KeyboardInterrupt:

        # Safety Shutdown Configuration for the Raspberry Pi.
        # The cleanup() method sets all initialized GPIO outputs back to
        # input pins. This will prevent you from accidentally shorting out
        # an output pin to ground during the electronic breadboarding
        # process. All GPIO pins should be configured to inputs when the
        # program is not running.
        GPIO.cleanup() 

        # Output the Shutdown Message
        print ('Program has been properly shutdown. Goodbye!')
