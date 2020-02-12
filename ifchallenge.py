name = input("What is your name? ")
age = int(input("What is your age? "))

if 18 <= age < 31:
    print("Welcome to the Holiday, {}".format(name))
else:
    print("I'm sorry, {}, but you must be between the ages of 18 and 30 to join the Holiday".format(name))