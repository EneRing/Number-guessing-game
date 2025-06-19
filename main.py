import random

print("""Welcome to the Number Guessing Game!
I'm thinking of a number  between 1 and 100.
You have 5 chances to guess the correct number.


Please select a difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)


""")

Choice_Difficulty = int(input("Enter your choice: "))

if Choice_Difficulty == 1:
	print("Great! You have selected the Easy difficulty level.")
	Chances = 10

elif Choice_Difficulty == 2:
	print("Great! You have selected the Medium difficulty level.")
	Chances = 5

elif Choice_Difficulty == 3:
	print("Great! You have selected the Hard difficulty level.")
	Chances = 3

Random_Number = random.randint(1, 100)

print("Let's start the game!")

Guess = int(input("Enter your guess: "))
Attempts = 0
while Guess != Random_Number and Chances != 0:
	if Guess > Random_Number:
		print("Incorrect! The number is less than ", Guess)
	elif Guess < Random_Number:
		print("Incorrect! The number is greater than ", Guess)
	Chances -= 1
	Attempts += 1
	Guess = int(input("Enter your guess: "))
print("Congratulations! You guessed the correct number in ", Attempts, "attempts.")
