import random

choices = ["R","P","S"]

computer = random.choice(choices)
player = None

while player not in choices:
	player = input('''
Pick an option from the following:
R for Rock
P for Paper
S for Scissors
''').upper()

if player == computer:
    print("CPU: ",computer)
    print("player: ",player)
    print("It's a Tie")
elif player == "R":
  if computer == "P":
    print("CPU: ",computer)
    print("player: ",player)
    print("CPU win:")
  if computer == "S":
    print("CPU: ",computer)
    print("player: ",player)
    print("You win:")
elif player == "S":
  if computer == "R":
    print("CPU: ",computer)
    print("player: ",player)
    print("CPU win:")
  if computer == "paper":
    print("CPU: ",computer)
    print("player: ",player)
    print("You win:")
elif player == "P":
  if computer == "S":
    print("CPU: ",computer)
    print("player: ",player)
    print("CPU win:")
  if computer == "R":
    print("CPU: ",computer)
    print("player: ",player)
    print("You win:")
