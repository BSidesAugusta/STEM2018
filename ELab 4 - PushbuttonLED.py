#############################################
# Filename: ELab 4 - PushbuttonLED.py
# Developer: BSides Augusta STEM
# Language: Python 3.4
# Description: The Raspberry Pi detects when the pushbutton
# is pressed and then turns ON the LED.
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
 
# Configure Variable for GPIO Pins
Pushbutton = 18
LEDred = 16

# Configure Control Variables
LEDonDelay = 3.0
 
# Config to Refer to GPIO by Pin Number
GPIO.setmode(GPIO.BCM)
 
# Configure GPIO Pins to Inputs/Outputs
GPIO.setup(Pushbutton,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LEDred,GPIO.OUT)
 
#############################################
# Main Program
#############################################
# Run the code until the CTL+C buttons end the program.
# The try...except handles the keyboard interruption
# with the CTL+C button press, it allows the program to
# shut down the program in a more graceful & safer way.
 
print ('Press CTL+C to Shut down the Pushbutton LED Program')
try:
        # Run the Loop Continuously
        while(True):
               
                # Check Input State
                input_state = GPIO.input(Pushbutton)
 
                if input_state == False:

                    # Turn ON the Red LED
                    GPIO.output(LEDred, True)
                    print('Button Pressed - Turn LED ON for',LEDonDelay,'seconds')
                    time.sleep(LEDonDelay)

                    # Turn OFF the Red LED
                    GPIO.output(LEDred, False)
                    print('Reset LED to OFF')
                            
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
