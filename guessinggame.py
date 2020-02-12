# MODULES
import random

highest = 1000 # highest number in random range decalred as variable (to be used in multiple locations)
answer = random.randint(1, highest) # generates random number between 1 and 10
guess = 0 # initialize to any number that doesn't equal the answer

print("Please guess number between 1 and {}: ".format(highest))

# LOGIC
while guess != answer:
    # new guess
    guess = int(input())

    # Quitting option
    if guess == 0:
        print("Thank you for playing, please try again another time!")
        break

    # Just right
    if guess == answer:
        print("Well done, you guessed it")
        break

    else:
        # too high
        if guess < answer:
            print("Please guess higher")

        # too low
        else:
            print("Please guess lower")