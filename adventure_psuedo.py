# Carol, Asiah

#example room1 - alien attack
def alien_room():
  # some prompts
  # '\n' is to print the line in a new line
  print("\nYou have spotted aliens and they are going to attack!")
  print("The aliens are close behind\nThere are two doors to choose from. Which one do you choose? (1 or 2)")

  #get user input take input()
  answer = input(">")

  if answer == "1":
    print("You decided to temporarily zap them out of consciousness. Run away and hide")
    alien_room2()
  elif answer == "2":
    game_over("You entered a room filled with armored ailens and get killed!")
  else:
    game_over("You have been killed!")

def alien_room2():
  # some prompts
  # '\n' is to print the line in a new line
  print("\nNow you entered the kitchen and you see a group of aliens eating")
  print("\nThere are two weapons to choose from. Which one do you choose? (laser gun or shield and sword)")
 
  # get user input take input()
  answer = input(">")

  if answer == "laser gun":
    print("You have slayed the aliens")
    alien_room3()
  elif answer == "shield and sword":
    game_over("Your shield and sword have been eaten and you got cut and bled to death")
  else:
    game_over("You have been killed!")

def alien_room3():
  # some prompts
  # '\n' is to print the line in a new line
  print("\nNow you entered the room of The Headmaster!")
  print("We have spotted and taken the key to the control room)\nThere are two buttons to choose from. Which one do you choose? (red or blue)")
 
  # get user input take input()
  answer = input(">")
  if answer == "red":
    print("The red button saved the world and the humans have succesfully taken over! All the aliens have been exterminated.")
  elif answer == "blue":
    game_over("The blue button destroys all life existence. The world has blew up, and everyone is dead.")
  else:
    game_over("You have died")

# function to ask play again or not
def play_again():
  print(" do you want to play again? y/n")
  # get input
  answer = input(">").lower
  # evaluate input using conditional 
  if answer == "y":
    start()
  else:
    # if user types anything besides "yes" or "y", exit() the program
    exit()

# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # STRETCH: maybe ask player to play again or not. 
  play_again()


def start():
  # give some prompts.
  print("\nThere is an alien invasion.")
  print("There is a door to your left and right, which one do you take? (l or r)")
  
  # convert the player's input() to lower_case
  answer = input(">").lower()

  if "l" in answer:
    # if player typed "left" or "l" lead him to alien_room()
    alien_room()
  elif "r" in answer:
    # else if player typed "right" or "r" lead him to alien_room2()
    alien_room2()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type something properly?")

 # calling start function. 
start()