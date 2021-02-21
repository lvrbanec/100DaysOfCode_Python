# 02.01.21, Frollo
# level: Beginner
# Project: Create a Hangman game

import random
from hangman_words import word_list #import wordlist
from hangman_art import logo, stages # imports pictures of a stages of hanging man

# pick a word randomly
chosen_word = random.choice(word_list)
# print(f"the secret word is {chosen_word}")
# show logo of the game
print(logo)
# create a drawing of the chosen_word
drawing = []
for i in chosen_word:
  drawing.append('_')
print(drawing)
#create a drawing of a hangman
print(stages[6])

# guess the word until you win or die
end_of_game = False
lives = 6
previous_guesses = []

while not end_of_game:
  # guess a letter
  guess = input('Please choose a letter\n').lower()
      
  # check if you guessed right
  index = 0 #index od a letter
  for letter in chosen_word: # or to get a position can write for i in len(chosen_word)
    index += 1
    if guess == letter:
      drawing[index-1] = letter
  print(drawing)

  # if the letter isnt guessed, remove one life
  if (guess not in chosen_word) and (guess not in previous_guesses):
    lives -= 1
    print(f'Letter {guess} is not in the chosen word.')
    print(stages[lives])
  #
  if guess in previous_guesses:
    print(f'You already tried letter {guess}.')
  previous_guesses.append(guess)

  # win condition
  if "_" not in drawing:
    end_of_game = True
    print("You win.")
  # lose condition
  if lives == 0:
    end_of_game = True
    print("You lost.")