# Prompt: Create a rock-paper-scissors game, player vs computer.

import random # random.randint

valid_choices = ("rock", "paper", "scissors") # A tuple containing valid user input.

"""
The choice on the left is true if it wins, 0 if it draws.
            rock (0) paper (1) scissors (2)
rock (0)      0       -1         1 
paper (1)     1       0         -1
scissors (2)  -1       1         0
"""
game_rules = ((0, -1, 1), (1, 0, -1), (-1, 1, 0)) # A 2D tuple containing a key that represents which choices win/draw against each other.

# Function allows us to easily commence a rock-paper-scissor round and get the outcome
def throw():
  """Begins a rock-paper-scissor prompt with the user and returns true if the user wins.
  
  The user gets prompted to type rock, paper or scissors. User's answer is validated then matched against the computers.
  Returns 1 if user wins, 0 if user draws, and -1 if user loses
  """
  computer_choice = random.randint(0, 2) # 0 = Rock, 1 = Paper, 2 = Scissors

  user_choice = input("Rock, paper, scissors, shoot!\nType your choice, 'rock', 'paper', or 'scissors': ")

  # Validate user's input
  while user_choice.lower() not in valid_choices:
    user_choice = input("Please type 'rock', 'paper', or 'scissors': ")

  # Print the computer's choice
  print(valid_choices[computer_choice].capitalize() + "!")

  # Using our game rules 2D tuple we can check if the user's choice has won, or drew.
  return game_rules[valid_choices.index(user_choice)][computer_choice] # 1 if won, 0 if drew, -1 if lost

# Begin a round.
game_outcome = throw()
while (game_outcome == 0): # As long as the user draws, keep trying.
  print("Uh oh, we had a draw. Let's go again.")
  game_outcome = throw()

# Print a success/failure message
print("You won!" if game_outcome == 1 else "You lost.")

"""
Things I learned from this project:
- Functions and their syntax
- Docstrings, how to comment and document functions
- String methods e.g lower() and capitalize()
- Tuples and 2D tuples
"""