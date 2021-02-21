# 03.02.21, Frollo
# Level: beginner
# Project: Easy calculator

from art import logo

print(logo)

# Operations
# Add
def add(n1, n2):
  return n1 + n2

# Substract
def substract(n1, n2):
  return n1 - n2

# Multipy
def multipy(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
"+" : add,
 "-" : substract,
 "*" : multipy,
 "/" : divide
  }

def call_again(): # to restart the code upon conditional
  switch = True
  while switch:
  # pick a first number
    num1 = float(input("What's the first number?: "))

    # pick a second number and an operation, and if wanted claculate with a previous result
    while switch:
      print("Pick one of the following operation:")
      for key in operations:
        print(key)
      operation_symbol= input()
      chosen_function = operations[operation_symbol]
      num2 = float(input("What's the next number?: ")) 
      result = chosen_function(num1, num2)
      print(f"{num1} {operation_symbol} {num2} = {result}")

      should_continue = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or type 'esc' to exit.\n")
      if should_continue == "esc":
        switch = False
        print("Thank you for using our calculator.")
      elif should_continue == 'y': 
        num1 = result
      elif should_continue == 'n':
        call_again()
        
call_again()