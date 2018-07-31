# Challenge 1: Create a Guess the Number game using a while loop
# Limit the player to 3 tries
# Tell them if they should guess higher or lower

import random
randomnum = random.randrange(0,11)
guess = int(input("Guess a number 1-10!"))
while guess != randomnum:
            if guess > randomnum:
                guess = int(input("Guess lower!"))
                break
            elif guess < randomnum:
                guess = int(input("Guess higher!"))
                break
            elif guess == randomnum:
                print ("You got it!")
                break
print ("The number was", randomnum)
print ("Try again!")
