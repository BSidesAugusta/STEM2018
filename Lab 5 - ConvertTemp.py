#############################################
# Filename: Lab 5 - ConvertTemp.py
# Developer: BSides Augusta STEM
# Language: Python 3.4
# Description: This program prompts the user for the temperature
# in Fahrenheit and converts it to Celsius. The Celsius
# temperature value is displayed to the screen and whether
# the temperature is perfect, too cold or very hot.

print ('Enter the Fahrenheit temperature: ') 
tempF = float( input() )

tempC = (tempF - 32.0)*(5.0/9.0)
print ('The Celsius temperature is: ', tempC, ' degrees')

if (tempF > 85):
        print ('It is very hot!') 
elif (tempF < 60):
                print ('It is too cold!')
else:
        print ('The temperature is perfect!') 
