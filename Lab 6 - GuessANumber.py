#############################################
# Filename: Lab 6 - GuessANumber.py
# Developer: BSides Augusta STEM
# Language: Python 3.4
# Description: This game will ask the user to guess a number 
# between 1 and 10. The program will inform the user if they
# are correct.
# Enter 11 or More to quit.

# Import Special Classes
from random import randint

# Initialization
guess = 0
RandomNumber = 0

# Inform the User How to Quit the Game.
print ('Enter 11 or More to Quit the Game.\n\n')

# Loop until they want to quit by entering more than 10.
while guess < 11:
    
    # Prompt for the Number Guess
    print ('\n\nHow lucky are you?')
    print ('Guess an integer number from 1 to 10.')
    guess = int(input())

    if (1 <= guess <= 10):
        # Capture the Input
        RandomNumber = randint(1,10)

        # Output the Number
        print('You guessed ',guess)
        print('The Random Number was ',RandomNumber)

        if (guess == RandomNumber):
            # Sprinkles for the Winner
            print('\nSPRINKLES FOR THE WINNER!')

# Thank you for playing the game
print ('Thank you for playing!\n\n')
