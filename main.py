import random
print("Infinity Die")

sides_of_die = int(input("How many sides?"))
playGame = "yes"

def rollDie(sides_of_die):
	print("You rolled ",random.randint(1,sides_of_die))
while playGame == "yes":
	rollDie(sides_of_die)
	playGame = input("Roll again? ")

