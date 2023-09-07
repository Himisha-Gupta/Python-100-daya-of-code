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

user_choice = input("Type 0 for rock , 1 for paper and 2 for siccsors")
computer_choice = print(random.randint(0,2))

if user_choice == computer_choice:
    print("It's a draw")
elif user_choice == 0 and computer_choice == 1:
    print("You won")
elif user_choice == 1 and computer_choice == 0:
    print("Computer won")
elif user_choice == 0 and computer_choice == 2:
    print("You won")
elif user_choice == 2 and computer_choice == 0:
    print("Computer won")
elif user_choice == 1 and computer_choice == 2:
    print("You won")
elif user_choice == 2 and computer_choice == 1:
    print("Computer won")
else:
    print("Error")

