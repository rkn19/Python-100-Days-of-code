import random 
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

images = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user > 2:
  print("You choosed an invalid number, you lose!")
else:
  print(images[user])
  computer_choice = random.randint(0,2)
  print(f"Computer chose:")
  print(images[computer_choice])
  if user == computer_choice :
    print("It's a draw!")
  elif user == 2 and computer_choice == 0 or user == 0 and computer_choice == 1 or user == 1 and computer_choice == 2:
    print("You lose!")
  elif user == 0 and computer_choice == 2 or user == 1 and computer_choice == 0 or user == 2 and computer_choice == 1:
    print("You win!")

  
