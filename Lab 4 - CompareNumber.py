#############################################
# Filename: Lab 4 - CompareNumber.py
# Developer: BSides Augusta STEM
# Language: Python 3.4
# Description: The user is prompted to enter a number from 0 & 10. 
# That number is then compared to numbers from 0 to 10 and outputs
# the comparison of True or False.

# Prompt the User for a Number
print ('Enter a number from 0 to 10')

# Convert the entered character value into an Integer number.
num = int(input())

# Loop x from 0 to 10
for x in range(11):
    
    # Output the Entered Number to x Loop and Output Comparison
    print ('Is',num,'equal to ',x,'?', num == x)
