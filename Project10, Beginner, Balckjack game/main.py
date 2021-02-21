# 04.02.2021, Frollo
# Level: Beginner
# project: simulation of a blackjack game


############### Our Blackjack House Rules #####################
 
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 if sum < 21 or 1 if sum > 21.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
from art import logo
from replit import clear
import random

# fuction for dealing 1 card
def deal_one_card():
  """ returns a random card from the deck """
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

# fuction for dealing 2 cards
def deal_two_cards():
  """ returns two random cards from the deck as a tuple"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  first_card = random.choice(cards)
  second_card = random.choice(cards)
  return first_card, second_card # returns tuple

# fuction for calculating sum of cards and declaring a blackjack
def calculate_score(cards):
  """ calculates a score of a deck of cards (from a tuple) """
  if sum(cards) == 21 and len(cards) == 2:
    return 0 # blackjack!
  if 11 in cards and sum(cards) > 21:
    cards = tuple(list(cards).remove(11).append(1)) # check if works  
  return sum(cards)

# function to compare player_cards, and pc scores
def compare(player_sum, pc_sum):
  if pc_sum > 21 and player_sum > 21:
    return "You went over. You lose."
  elif player_sum == pc_sum:
    return "Draw"
  elif pc_sum == 0:
    return "Lose, opponen has Blackjack"
  elif player_sum == 0:
    return "Win with a Blackjack"
  elif player_sum > 21:
    return "You went over, you lose."
  elif pc_sum > 21:
    return "Computer went over, you win." 
  elif player_sum > pc_sum:
    return "Your win."
  else: 
    return "You lose."

# blackjack game
def play_game():
  
  print (logo)

  player_cards = deal_two_cards()
  pc_cards = deal_two_cards()

  # decisions of a player, ie does she/he wants another card?
  is_game_over = False
  while not is_game_over:
    player_sum = calculate_score(player_cards)
    pc_sum = calculate_score(pc_cards)
    print(f"Your cards are: {player_cards}. Current score : {player_sum}.")
    print(f"Computer's first card: {pc_cards[0]}")
    
    if player_sum == 0 or pc_sum == 0 or player_sum > 21 :
      is_game_over = True
    else:
      additional_card = input("Type 'y' to get another card, type 'n' to pass: ") 
      if additional_card == 'y':
        player_cards += (deal_one_card(),) # adding an int to tuple. int has to be in a (int,) form

      else: 
        is_game_over = True

  # decisions of a computer, ie if computer has less than 17, needs to draw one more card
  while pc_sum !=0 and pc_sum < 17: # 0 is blackjack
    pc_cards += (deal_one_card(),)
    pc_sum = calculate_score(pc_cards)
    print(f"Your cards are: {player_cards}. Final score : {player_sum}.")
    print(f"Computer's cards are: {pc_cards}. Final score : {pc_sum}.")
    print(compare(player_sum, pc_sum))

# Do you want to restart a game?
while input("Do you want to play the game of blackjack? Type 'y' or 'n': ") == 'y':
  clear()
  play_game() 

 
