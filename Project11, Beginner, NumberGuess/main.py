# 05.02.2021, Frollo
# Level Beginner
# Project: Number Guessing Game

# computer randlomly picks an integer between 1 and 100, player needs to guess the number

import random
from art import logo

EASY_LEVEL_TURNS = 10 # constants are accessible in functions
HARD_LEVEL_TURNS = 5

# compare two numbers
def compare(number, num_guess):
  if num_guess > number:
    print("Too high.")
    case = 0
  elif num_guess < number:
    print("Too low.")
    case = 1
  elif num_guess == number:
    print("You guessed! The number was {number}")
    case = 2
  return case

#chose a difficulty
def set_difficulty():
  def_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if def_difficulty == "hard":
    return HARD_LEVEL_TURNS
  elif def_difficulty == "easy":
    return EASY_LEVEL_TURNS


def play_game():
  # select a random number between 1 and 100
  all_numbers = list(range(1,101)) # can be written as ? randint(1,100)
  rand_number = random.choice(all_numbers)
  #print(number)

  print(logo)
  print("Welcome to the Number Guessing Game!")

  attempts = set_difficulty()

  game_over = False
  while not game_over:
    print(f"You have {attempts} attempts remaining to guess the number.")
    num_guess = int(input("Make a guess: "))
    case = compare(rand_number, num_guess)
    # reduce the number of attempts
    attempts -= 1
    # end the game if you run out of attempts, game over
    if attempts == 0:
      print("Game lost")
      game_over = True
    # if not guessed, try again
    elif case == 0 or case == 1:
      print("Guess again.")
    # if guesssed, stop the game
    elif case == 2:
      game_over = True
  
play_game()
  
  

