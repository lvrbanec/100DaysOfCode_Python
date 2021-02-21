# 30.01.2021
# level: Beginner

# The aim of this code is to create a love calculator, which "predicts" how well two people match based on their names. The logic is based on the game we played as a kids, and is explained at https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_together = name1 + name2
name_together_low = name_together.lower()
#print(name_together_low)

score_true = name_together_low.count("t")+ name_together_low.count("r") + name_together_low.count("u") + name_together_low.count("e")
#print(score_true)

score_love= name_together_low.count('l') + name_together_low.count('o') + name_together_low.count('v') + name_together_low.count('e')
#print(score_love)

final_score = int(f"{score_true}{score_love}")
#print(final_score)

if final_score < 10 or final_score>90:
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score <= 50 and final_score >= 40:
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}.")