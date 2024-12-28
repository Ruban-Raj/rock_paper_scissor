rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

from random import randint

game = True

while game == True:
    your_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
    if your_input >= 3 or your_input < 0:
        print("You typed an invalid number, you lose!")
        game = False
    else:
        options = [rock, paper, scissors]
        your_selection = options[your_input]
        random_choice = randint(0,2)
        system_selection = options[random_choice]
        print(f" You have selected \n {your_selection}")
        print(f" Computer have selected \n {system_selection}")

        if your_input == 0 and random_choice == 2:
            print("You win!")
        elif random_choice == 0 and your_input == 2:
            print("You lose")
            game = False
        elif random_choice > your_input:
            print("You lose")
            game = False
        elif your_input > random_choice:
            print("You win!")
        elif random_choice == your_input:
            print("It's a draw")