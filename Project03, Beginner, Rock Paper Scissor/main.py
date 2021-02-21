# 30.01.2021
# level : Beginner
# project: create rock paper scissors game

# ASCII image for rock, paper, scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

# player's decision
person = int(input('What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n')) # input by a default results in a string

  # check for invalid number
if person < 0 or person >= 3: #needs to be at the beginning so the conditional is first checked
  print('Invalid number')
else:
  print(game_images[person])

# computer's random decisiom
import random
computer = random.randint(0,2)

print(game_images[person])

# result
if person == computer:
  print('It\'s a draw')
elif person > computer:
  print('You win')
elif person < computer:
  print("You lose")