#############################################
# Filename: Lab 7 - TrafficLight.py
# Developer: BSides Augusta STEM
# Language: Python 2.7
# Description: This program will make the Raspberry Pi three GPIO
# output ports control three LEDs.  The Red, Yellow and Green LEDs
# turn ON/OFF like a street traffic light.
# This traffic light control program runs in an infinite loop.

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
LEDredOnTime = 5.0
LEDyellowOnTime = 2.0
LEDgreenOnTime = LEDredOnTime - LEDyellowOnTime

# Configure LED Variables to GPIO Pins
# Traffic Light 1
LEDred = 16
LEDyellow = 20
LEDgreen = 21

# Traffic Light 2
LEDred2 = 13
LEDyellow2 = 19
LEDgreen2 = 26

# Config to Refer to GPIO by Pin Number
GPIO.setmode(GPIO.BCM)

# Configure GPIO Pins to Outputs
# Traffic Light 1
GPIO.setup(LEDgreen,GPIO.OUT)
GPIO.setup(LEDred,GPIO.OUT)
GPIO.setup(LEDyellow,GPIO.OUT)

# Traffic Light 2
GPIO.setup(LEDgreen2,GPIO.OUT)
GPIO.setup(LEDred2,GPIO.OUT)
GPIO.setup(LEDyellow2,GPIO.OUT)

#############################################
# Main Program
#############################################
# Run the code until the CTL+C buttons end the program.
# The the try...except handles the keyboard interruption
# with the CTL+C button press, It allows the programmer
# to shut down the program in a more graceful & safer way.

print ('Press CTL+C to Shut Down the Traffic Light Program')
try:
        # Run the Loop Continuously
        while(1):
                ################################
                # 1 Red Light ON
                GPIO.output(LEDred, True)
                GPIO.output(LEDgreen, False)
                GPIO.output(LEDyellow, False)
                print ('RD1 ON for',LEDredOnTime,'seconds')
                # 2 Green Light ON
                GPIO.output(LEDred2, False)
                GPIO.output(LEDgreen2, True)
                GPIO.output(LEDyellow2, False)
                print ('GN2 ON for',LEDgreenOnTime,'seconds\n')               
                time.sleep(LEDgreenOnTime)
                
                # 2 Yellow ON
                GPIO.output(LEDred2, False)
                GPIO.output(LEDgreen2, False)
                GPIO.output(LEDyellow2, True)
                print ('YL2 ON for',LEDyellowOnTime,'seconds\n') 
                time.sleep(LEDyellowOnTime)

                ################################ 
                # 1 Green Light ON
                GPIO.output(LEDred, False)
                GPIO.output(LEDyellow, False)
                GPIO.output(LEDgreen, True)
                print ('GN1 ON for',LEDgreenOnTime,'seconds')
                # 2 Red Light ON
                GPIO.output(LEDred2, True)
                GPIO.output(LEDgreen2, False)
                GPIO.output(LEDyellow2, False)
                print ('RD2 ON for',LEDredOnTime,'seconds\n')
                time.sleep(LEDgreenOnTime)
                
                GPIO.output(LEDred2, True)
                GPIO.output(LEDgreen2, False)
                GPIO.output(LEDyellow2, False)

                ################################                
                # 2 Yellow ON
                GPIO.output(LEDred, False)
                GPIO.output(LEDyellow, True)
                GPIO.output(LEDgreen, False)
                print ('YL1 ON for',LEDyellowOnTime,'seconds\n')
                time.sleep(LEDyellowOnTime)
              
            
# The exception section is called whenever a keyboard interrupt happens.
# This allows you to control how gracefully the program shuts down.
except KeyboardInterrupt:

        # Safety Shut Down Configuration for the Raspberry Pi.
        # The cleanup() method sets all initialized GPIO outputs back to
        # input pins. This will prevent you from accidently shorting out
        # an output pin to ground during the electronic breadboarding
        # process. All GPIO pins should be configured to inputs when the
        # program is not running.
        GPIO.cleanup() 

        # Output the Shut Down Message
        print ('Program has been properly shut down. Goodbye!')
