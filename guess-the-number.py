# Prompt: Write a program where the user is to guess a number randomly generated between 0-20, telling the user whether their guess is
# higher/lower each time they're wrong until they get it right and record how many attempts they had

import random # Random library gives us access to random.randint

rand_num = random.randint(1, 20) # Generate a random integer between 0-20
attempts = 0 # Attempt counter
success_msg = "You have guessed the correct number, {number}, after {attempts} attempt{s}. Well done." # A formatted success message

# Prompt the user to guess
user_guess = input("We have generated a number between 1 and 20. Guess correctly: ")

# Check whether user's guess is correct or not
while int(user_guess) != rand_num:
  attempts += 1 # Increment attempt counter
  user_guess = input("Incorrect, too " + ("low" if int(user_guess) < rand_num else "high") + ". Try again: ") # Re-prompt the user

# Print a success message that includes the correct number and the amount of attempts
print(success_msg.format(number = rand_num, attempts = attempts, s = '' if attempts == 1 else 's'))

"""
Things I learned from this project:
- brief overview of 'random' library
- string formatting
- input() method
- while/if syntax
- python ternary operator - x if condition else y
"""