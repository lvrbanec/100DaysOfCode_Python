# 02.02.2021, Frollo
# project: create Casear Cipher
# level Beginner
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# define a function for encryption
def caesar(word, shift_ammount, direction):
  encrypted_word = ''
  if direction == 'decode':
      shift_ammount *= -1 # substract the position if decoding
  for char in word:
    if char in alphabet:
      position = alphabet.index(char) # gives only the first index
      encrypted_letter = alphabet[position + shift_ammount]
      encrypted_word += encrypted_letter
    else:
      encrypted_word += char
  print(f"The {direction}d text is '{encrypted_word}'.")

should_continue = True # run again?
while should_continue: 
# give input to encript
  desired_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  # if the user imputs huge number find the one that corresponds to alphabet, 26 letters our alphabet
  shift = shift % 26 
  
  # call function
  caesar(word = text, shift_ammount = shift, direction = desired_direction )

  # run again?
  run_again = input("Type 'yes' if you want to run again. Otherwise type 'no'\n.")
  if run_again == "no":
    should_continue = False
    print("Goodbye")