"""
snake = 1
water = -1
gun = 0

"""

import random

computer = random.choice([1, -1, 0])
your_choice = input("Enter the choice: ")
you_dict = {"s": 1, "w": -1, "g": 0}
reverse_dict = {1: "snake", -1: "water", 0: "gun"}

if your_choice not in you_dict:
    print("Invalid input ")
    exit()

you = you_dict[your_choice]
print(f"you chose {reverse_dict[you]} \n computer chose {reverse_dict[computer]} ")

if computer == you:
    print("its draw")
else:
	if computer == -1 and you == 1:
		print("You Win")
	elif computer == -1 and you == 0:
		print("You loose")
	elif computer == 1 and you == 0:
		print("you loose")
	elif computer == 1 and you == -1:
		print("You win")
	elif computer == 0 and you == -1:
		print("You win")
	elif computer == 0 and you == 1:
		print("You loose")
	else:
		print("invalid input")