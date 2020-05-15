#Rolling Dice Simulator
#Question: The dice rolling simulator will imitate the experience of rolling a dice. 
#It will generate a random number and the user can play again and again to get a number 
#from the dice until the user decides to quit the program.

import random
import readline

#Function to generate random number between 1 to 6
while True:
    inp = input("Roll?(y/n):")
    if inp.lower() == 'y':
        print(random.randint(1, 6))
    else:
        break      