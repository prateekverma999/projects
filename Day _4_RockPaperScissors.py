import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____) Chose "0" for ROCK
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)   Chose "1" for PAPER
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)  Chose "2" for SCISSORS
      (____)
---.__(___)
'''

print(f"Welcome to Rock Paper Scissors Game !!! {rock}{paper}{scissors}")

player_selection = int(
    input('''Please Select you option: Chose "0" for ROCK", Chose "1" for PAPER, Chose "2" for SCISSORS : '''))
computer_selection = random.randint(0, 2)

game_image = [rock, paper, scissors]

if player_selection >= 3 or player_selection < 0:
    print("Invalid entry!! YOU LOSE !!")
else:
    print("Your Selection : ")
    print(game_image[player_selection])
    print("Computer Select: ")
    print(game_image[computer_selection])
    if player_selection == 0 and computer_selection == 2:
        print("YOU WIN")
    elif player_selection == 2 and computer_selection == 0:
        print(" YOU LOSE ")
    elif player_selection > computer_selection:
        print("YOU WIN")
    elif player_selection < computer_selection:
        print("YOU LOSE")
    elif player_selection == computer_selection:
        print("MATCH DRAW")
