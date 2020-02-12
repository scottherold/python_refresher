# a Hi/Lo guessing game for the computer to guess a number
# This program uses a binary search algorithm

# variables
low = 1
high = 1000

# PROMPT
print("Please think of a number {} and {}".format(low, high))
input("Press ENTER to start")

# LOGIC
guesses = 1
while low != high:
    print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h for higher or l for lower, "
                     .format(guess)).casefold()

    if high_low == "h":
        # Guess Higher. 
        # The low end of the range becomes 1 greater than the guess
        low = guess + 1
    elif high_low == "l":
        # Guess lower. 
        # The high end of the range becomes one less than the guess
        high = guess - 1
    else:
        print("Please enter h for higher, l for lower.")

    guesses += 1

# Correct guess will be printed
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses!".format(guesses))
