# To create a guessing game, we need to write a program to select a random number between 1 and 10. To give hints to the user, we can use conditional statements to tell the user if the guessed number is smaller, greater than or equal to the randomly selected number.

# So below is how you can write a program to create a number guessing game using Python:

import random

n = random.randrange(1,10)
guess = int(input("Enter any number: "))

while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter another number: "))
    elif guess > n:
        print("Too high")
        guess = int(input("Enter another number: "))
    else:
        break
print("You guess it right!")