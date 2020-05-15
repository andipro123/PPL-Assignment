#Make a program that randomly chooses a number to guess and 
#then the user will have a few chances to guess the number correctly. 
#In each wrong attempt, the computer will give a hint that the number is 
#greater or smaller than the one you have guessed.

import random

num = random.randint(0, 100)

noOfAttempts = 3

while noOfAttempts:
    guess = int(input('Guess the number: '))
    if guess == num:
        break
    elif guess > num:
        print("A little lower\n")
    else:
        print("A little higher\n")
    print(f'No of Attempts remaining: {noOfAttempts - 1}')
    noOfAttempts -= 1

print(f"The number is {num}")   