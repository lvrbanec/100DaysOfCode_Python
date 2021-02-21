# 01.02.2021
# Lever: Beginner

# Password Generator Project
# generate a password with the number of letters, numbers and symbols specified by a subject
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# select a random letter
selected_letters=[] # for a string, we would write selected_letters = ""
for i in range(nr_letters):
  rand_letter = letters[random.randint(0, len(letters)-1)] # or rand_letter = random.choice(letters)
  selected_letters.append(rand_letter) # or  use sellected_letters += rand_letter
print(selected_letters)

# select a random number
selected_numbers=[]
for i in range(nr_numbers):
  rand_number = numbers[random.randint(0, len(numbers)-1)]
  selected_numbers.append(rand_number)
print(selected_numbers)

# select a random symbol
selected_symbols=[]
for i in range(nr_symbols):
  rand_symbol = symbols[random.randint(0, len(symbols)-1)]
  selected_symbols.append(rand_symbol)
print(selected_symbols)

password_list = selected_letters + selected_numbers + selected_symbols
random.shuffle(password_list) # automatically overwrites variable. if new variable needed use random.sample(x, len(x))
password_str = "".join(password_list)
print(password_str)


