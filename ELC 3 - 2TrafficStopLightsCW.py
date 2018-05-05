#############################################
# Filename: ELC 3 - 2TrafficStopLightsCW.py
# Developer: BSides Augusta STEM
# Language: Python 3.4
# Description: This program will make the Raspberry Pi control
# four GPIO output ports which will turn ON/OFF four LEDs: Red,
# Yellow, Green & White. The LEDs will simulate two traffic
# lights with crosswalk sign and pushbuttons.
# Pressing the Cross Walk Pushbutton will add 10 Seconds to the
# Traffic Stop Light time.
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
def TrafficLightsCtl(RedPin,RedTF,YellowPin,YellowTF,GreenPin,GreenTF,WhitePin,WhiteTF):
        # Input Parameters
        # RedPin    => GPIO Pin Number
        # RedTF     => True Turns ON LED; False Turns OFF LED
        # YellowPin => GPIO Pin Number
        # YellowTF  => True Turns ON LED; False Turns OFF LED
        # GreenPin  => GPIO Pin Number
        # GreenTF   => True Turns ON LED; False Turns OFF LED
        # WhitePin  => GPIO Pin Number
        # WhiteTF   => True Turns ON LED; False Turns OFF LED

        GPIO.output(RedPin,RedTF)
        GPIO.output(YellowPin,YellowTF)
        GPIO.output(GreenPin,GreenTF)
        GPIO.output(WhitePin,WhiteTF)
     

#############################################
# Initialization
#############################################
# Configure Pushbutton Variables
Pushbutton1 = 18
Pushbutton2 = 22

# Configure LED ON Time in Seconds
LEDredOnTime = 5.0
LEDyellowOnTime = 2.0
LEDgreenOnTime = LEDredOnTime - LEDyellowOnTime

# Configure LED Variables to GPIO Pins
# Traffic Light 1
LEDred1 = 16
LEDyellow1 = 20
LEDgreen1 = 21
LEDwhite1 = 12

# Traffic Light 2
LEDred2 = 13
LEDyellow2 = 19
LEDgreen2 = 26
LEDwhite2 = 5

# Congigure Red LED ON Time Delay for Crosswalk
LEDredDelay = 10
LEDgreenDelay = LEDredDelay - LEDyellowOnTime

# Config to Refer to GPIO by Pin Number
GPIO.setmode(GPIO.BCM)

# Configure GPIO Pins to Inputs/Outputs
GPIO.setup(Pushbutton1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(Pushbutton2,GPIO.IN,pull_up_down=GPIO.PUD_UP)

# Configure GPIO Pins to Outputs
# Traffic Light 1
GPIO.setup(LEDred1,GPIO.OUT)
GPIO.setup(LEDyellow1,GPIO.OUT)
GPIO.setup(LEDgreen1,GPIO.OUT)
GPIO.setup(LEDwhite1,GPIO.OUT)

# Traffic Light 2
GPIO.setup(LEDred2,GPIO.OUT)
GPIO.setup(LEDgreen2,GPIO.OUT)
GPIO.setup(LEDyellow2,GPIO.OUT)
GPIO.setup(LEDwhite2,GPIO.OUT)

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
                ################################################################
                # Check to See if the Crosswalk 1 Pushbutton Was Pressed
                # Add a Delay to the Next Traffic Light 1 Red Light when Pressed
                input_state = GPIO.input(Pushbutton1)

                # Add Red LED Delay if PB is Pressed
                if input_state==False:
                        print('Crosswalk 1 Button Pressed')
                        CalcLEDredOnTime = LEDredOnTime + LEDredDelay
                        CalcLEDgreenTime = CalcLEDredOnTime - LEDyellowOnTime
                else:
                        CalcLEDredOnTime = LEDredOnTime
                        CalcLEDgreenTime = LEDredOnTime - LEDyellowOnTime
                
                ################################################################
                # Red Traffic Light 1 Control Section
                # Traffic Light 2 Yellow Light ON Time is a Constant Amount of Time               
                # Traffic Light 2 Green Light ON Time is Calculated
                #       Green Light 2 = Red Light 1 - Yellow Light Constant
                
                ################################ 
                # 1 Red Traffic Light ON
                TrafficLightsCtl(LEDred1,True,LEDyellow1,False,LEDgreen1,False,LEDwhite1,True)
                print ('RD1 ON for',CalcLEDredOnTime,'seconds')                

                ################################ 
                # 2 Green Traffic Light ON
                TrafficLightsCtl(LEDred2,False,LEDyellow2,False,LEDgreen2,True,LEDwhite2,False)
                print ('GN2 ON for',CalcLEDgreenTime,'seconds\n')               
                time.sleep(CalcLEDgreenTime)

                ################################        
                # 2 Yellow Traffic Light ON
                TrafficLightsCtl(LEDred2,False,LEDyellow2,True,LEDgreen2,False,LEDwhite2,False)
                print ('YL2 ON for',LEDyellowOnTime,'seconds\n') 
                time.sleep(LEDyellowOnTime)





                ################################################################
                # Check to See if the Crosswalk 2 Pushbutton Was Pressed 
                # Add a Delay to the Next Traffic Light 1 Red Light when Pressed
                input_state = GPIO.input(Pushbutton2)

                # Add Red LED Delay if PB is Pressed
                if input_state==False:
                        print('Crosswalk 2 Button Pressed')
                        CalcLEDredOnTime = LEDredOnTime + LEDredDelay
                        CalcLEDgreenTime = CalcLEDredOnTime - LEDyellowOnTime
                else:
                        CalcLEDredOnTime = LEDredOnTime
                        CalcLEDgreenTime = LEDredOnTime - LEDyellowOnTime
                
                ################################################################
                # Red Traffic Light 2 Control Section
                # Traffic Light 1 Yellow Light ON Time is a Constant Amount of Time               
                # Traffic Light 1 Green Light ON Time is Calculated
                #       Green Light 1 = Red Light 2 - Yellow Light Constant
                
                ################################ 
                # 1 Green Light ON
                TrafficLightsCtl(LEDred1,False,LEDyellow1,False,LEDgreen1,True,LEDwhite1,False)
                print ('GN1 ON for',CalcLEDgreenTime,'seconds')

                ################################                 
                # 2 Red Light ON
                TrafficLightsCtl(LEDred2,True,LEDyellow2,False,LEDgreen2,False,LEDwhite2,True)
                print ('RD2 ON for',CalcLEDredOnTime,'seconds\n')
                time.sleep(CalcLEDgreenTime)
  
                ################################                
                # 2 Yellow ON
                TrafficLightsCtl(LEDred1,False,LEDyellow1,True,LEDgreen1,False,LEDwhite1,False)
                print ('YL1 ON for',LEDyellowOnTime,'seconds\n')
                time.sleep(LEDyellowOnTime)
              
            
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
