# 30.01.2021
# level Beginner

# The point of the game is to find the water in the deser to escape Mr. Death

print('''
**********************************************************************
                                             ###  
                                            ####  
                                  #         ###   
                                ####         ###   
                             ########       ####    
                            #########    ## ####     
                             #    ###   #  ######     
                             #    ###  #     ###      
                             #   ###  #    #####        
                             #   ### #     #####         
         #                   #   ####   #########        
         ##       ###        #   #################       
     ######      #####        #  ##################      
   ########     #####         ##   ###############      
  ##########      #######            ##############     
   ##  #####     #####               #####    #####
   #   ####      ######               ###      ## #
   #   ####   #########               ##       ##
   #  ####    #########               ##       ##
   #  ####   #  #######               ##       ##
   # #####  #    #####                ##       ##
   # ####  #     ######               ##       ##
   # ######    #########             ##       ##
   #  ####################
    # #####################
     #######################
       #####################
        ###################
        ######      #######
         ####       ######
         ###         #####
         ###         ### #
         ###         ### #
         ###          ## #          
         ###          ####
        ##           ###
************************************************************************
''')
# the art is taken from https://ascii.co.uk/art/camels
print("Welcome to The Desert.")
print("You were riding cammels, when your cammel (with you on the back) ran away and you got lost in the desert.") # \' escapes the '
print("You\'r mission is to find the water, or otherwise you will meet Mr. Death. You have 3 days until you dehydrate.")

dome = input("You see one huge sand dome on the right. Other than that there is not much to see. The sand is everywhere. Where should you go? Write \"right\" to climb the dome, or \"left\" to walk next to the dome.\n").lower()
if dome == "left":
  night = input("You tried to walk next to the dome but a huge wind came over and the dome fell apart. Good think you didn't climb that dome, or you would have died. Lucky you. The night has finally fallen. You see the sky. Should you follow the brighest star and move towards the north, or would you rather rest and sleep? Write \"walk\" or \"rest\".\n").lower()
  if night == "walk":
    elephants = input("Good choice! You walked towards the north until you met a group of elephants. Should you continue walking north, should you try to shoe the elephants away, or should you follow the elephants? Write \"walk\", \"shoo\" or \"follow\".\n").lower()
    if elephants == "walk":
      print("You continued walking norht, but you never reached the water. Sorry man.")
    elif elephants == "shoo":
      print("The elephants felt attached and smashed you with their huge legs. Be smarter next time.")
    elif elephants == "follow":
      print ("It is well known that the elephants remember the paths to the water in desert. Seems like you watched some documentaries on netflix. You found water. You are the survivor.")
  else:
    print("You decided to rest, but the temparatures fell under zero. You froze. Try again.")
else:
  print("You climbed the dome and from the top saw your city, but the strong winds came and the dome collapsed. You got burried under the sand. Mr. Death came. Bad luck.")