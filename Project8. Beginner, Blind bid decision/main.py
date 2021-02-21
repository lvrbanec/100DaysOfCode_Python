# 03.02.21, Frollo
# level: Beginner
# project: Create a blind bid program

from replit import clear
from art import logo

print(logo)

# add a new bidder function
bidder_info = [] # could be also saved as {name1: amount1, name2: amount2}
def add_bidder_info(val_name, val_bid):
    new_bidder = {"name": val_name, "bid": val_bid}
    bidder_info.append(new_bidder)

# find the highest bidder function
def find_highest_bidder(list_of_dictionary):
  max_bid = 0
  for dictionary in list_of_dictionary:
    bid = dictionary["bid"]
    if bid > max_bid:
      max_bid = bid
      max_name = dictionary["name"]
  print(f'Highest bid is {max_bid}$ bidded by {max_name}.')

# save info about the bidders
will_continue = True
while will_continue:
  input_name = input("What is your name?\n")
  input_bid = float(input("What's your bid?\n$"))
  input_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  add_bidder_info(val_name = input_name, val_bid = input_bid)
  clear()
  if  input_continue == "no":
    will_continue = False

print(bidder_info)
find_highest_bidder(bidder_info)