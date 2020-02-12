answer = 5

print("Please guess number between 1 and 10: ")

# wrapping input() within int() casts the input as a integer
guess = int(input())

# Refactor
if guess == answer:
    print("You got it first time")
else:
    if guess < answer:
        print("Please guess higher")
    else: # guess must be greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guess correctly")

# Old Code
# if guess < answer:
#     print("Please guess higher")
#     # second guess added
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")

#     # second guess added
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")
