#############################################
# Filename: Lab 7 - TrafficLight.py
# Developer: BSides Augusta STEM
# Language: Python 3.4
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
# Functions
#############################################
# Traffic Lights Control
def TrafficLightsCtl(RedPin,RedTF,YellowPin,YellowTF,GreenPin,GreenTF):
        GPIO.output(RedPin,RedTF)
        GPIO.output(YellowPin,YellowTF)
        GPIO.output(GreenPin,GreenTF)

#############################################
# Initialization
#############################################
# Configure LED ON Time in Seconds
LEDredOnTime = 5.0
LEDyellowOnTime = 2.0
LEDgreenOnTime = LEDredOnTime - LEDyellowOnTime

# Configure LED Variables to GPIO Pins
LEDred = 16
LEDyellow = 20
LEDgreen = 21

# Config to Refer to GPIO by Pin Number
GPIO.setmode(GPIO.BCM)

# Configure GPIO Pins to Outputs
GPIO.setup(LEDgreen,GPIO.OUT)
GPIO.setup(LEDred,GPIO.OUT)
GPIO.setup(LEDyellow,GPIO.OUT)

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
                TrafficLightsCtl(LEDred,True,LEDyellow,False,LEDgreen,False)
                print ('RD1 ON for',LEDredOnTime,'seconds')
                time.sleep(LEDredOnTime)

                ################################ 
                # 1 Green Light ON
                TrafficLightsCtl(LEDred,False,LEDyellow,False,LEDgreen,True)
                print ('GN1 ON for',LEDgreenOnTime,'seconds')
                time.sleep(LEDgreenOnTime)

                ################################                
                # 1 Yellow ON
                TrafficLightsCtl(LEDred,False,LEDyellow,True,LEDgreen,False)
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
