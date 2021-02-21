# 01.02.2021
# level: Beginner

#  computer solves the Fizz Buzz game from number 1 to 100 (if the number is devisible by 3, print Fizz. If the number is devisible by 5 print Buzz. If its devisible by both, print FizzBuzz. Otherwise print the number.)

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
  elif number % 3 == 0:
    print ('Fizz')
  elif number % 5 == 0:
    print('Buzz')
  else:
    print(number)
