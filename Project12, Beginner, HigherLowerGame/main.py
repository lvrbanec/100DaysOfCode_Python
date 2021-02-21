# 05/02/2021, Frollo
# Level: Beginner
# Project: Higher Lower game

import art 
from game_data import data
import random
from replit import clear


# select a random datapoint 
def select_datapoint():
  """"Selects a random datapoint from a list, returns it as a dictionary"""
  index = random.randint(0, len(data)-1) # !can also use random.choice(list)
  datapoint_dict = data[index]
  return datapoint_dict


# check if the player made a right decision and count the score
def compare_datapoints(dic_A, dic_B, player_decision, prev_score):
  ''' Looks if the player made a right decision and if yes increases the final score by 1. Output is guessed (True) or not guessed (False). '''
  # if the player is right print it
  if (dic_A['follower_count'] > dic_B['follower_count'] and player_decision == "a") or (dic_A['follower_count'] < dic_B['follower_count'] and player_decision == "b"):
    prev_score += 1
    print(f"You're right! Current score: {prev_score}")
    return [True, prev_score]
  # if the player is wrong print it
  else: 
    print(f"Sorry, that's wrong. Current score: {prev_score}")
    return [False, prev_score]


print(art.logo)
A = select_datapoint()

game_over = False
score = 0
while not game_over:
  print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.")
  print(art.vs)

  B = select_datapoint()
  while A == B: # if two datapoints are selected, pick again
    B = select_datapoint()
  print(f"Against B: {B['name']}, {B['description']}, from {B['country']}.")
 
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()

  clear()
  print(art.logo)

  guessed, score = compare_datapoints(dic_A = A, dic_B = B, player_decision = answer, prev_score = score ) # returns true if player  guessed
  A = B
  if not guessed:
    game_over = True




