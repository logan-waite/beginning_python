print ("Welcome to Rock, Paper, Scissors!\n")

import random

exit = False

user_wins = 0
computer_wins = 0
ties = 0

while exit == False:

	def user_won(user_choice, computer_choice):
		global user_wins
		print ("You win! " + user_choice + " beats " + computer_choice)
		user_wins += 1

	def computer_won(user_choice, computer_choice):
		global computer_wins
		print ("You lose. " + computer_choice + " beats " + user_choice)
		computer_wins += 1

	rand_int = random.randint(1,3)
	if rand_int == 1:
		computer_choice = 'rock'
	elif rand_int == 2:
		computer_choice = 'paper'
	elif rand_int == 3:
		computer_choice = 'scissors'

	good_choice = False
	while good_choice == False and exit == False:
		user_choice = raw_input("Please choose 'rock', 'paper', or 'scissors', or 'exit' to quit:\n")
		
		if user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissors':
			good_choice = True
		
		elif user_choice == 'exit':
			exit = True

	if exit == False:
		if user_choice == computer_choice:
			print ("Tie for " + user_choice)
			ties += 1
		
		elif user_choice == 'rock' and computer_choice == 'scissors':
			user_won(user_choice, computer_choice)
		
		elif user_choice == 'paper' and computer_choice == 'rock':
			user_won(user_choice, computer_choice)
		
		elif user_choice == 'scissors' and computer_choice == 'paper':
			user_won(user_choice, computer_choice)
		
		else:
			computer_won(user_choice, computer_choice)

		print("\n")

print ("\n")
print ("User wins: " + str(user_wins))
print ("Computer wins: " + str(computer_wins))
print ("Ties: " + str(ties))

print ("Total games: " + str((ties + computer_wins + user_wins)) + "\n")