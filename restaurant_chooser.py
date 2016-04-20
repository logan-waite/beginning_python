print("Welcome to your restaurant chooser!")

restaurants = ['Taco Bell', 'Oregano', 'Burger King', 'BYU Creamery', 'Olive Garden', 'Applebees', 'The Bombay House', 'Pho+']

def list_restaurants():
	for place in restaurants:
		print place

def add_restaurant():
	new_restaurant = raw_input("What is the name of the new restaurant?: ")
	restaurants.append(new_restaurant)
	print(new_restaurant + " was added to the list!")

def remove_restaurant():
	user_input = raw_input("What restaurant would you like removed? ")
	try:
		to_remove = restaurants.index(user_input)
		restaurants.pop(to_remove)
		print (user_input + " was removed from the list!")
	except:
			print("Couldn't remove the restaurant!")

leaving = False
while not leaving:
	good_option = False
	while not good_option:
		a_number = False
		while not a_number:
			print("Please select a number for one of the following options: ")

			print("1 - Display all restaurants ")
			print("2 - Add a restaurant ")
			print("3 - Remove a restaurant ")
			print("4 - Shuffle the list ")
			print("5 - Begin the tournament ")
			print("6 - Quit the program ")

			user_input = raw_input()
			#Check to make sure the input is okay
			try:
				choice = int(user_input)
				a_number = True
			except ValueError:
				print("That wasn't a whole number! Try again.")

		# Check if input is one of the options
		if not (choice > 0 and choice < 7):
			print(choice)
			print("That wasn't one of the options! Try again.")
		else:
			good_option = True

	# Begin actual program
	if choice == 6: 	
		print ("Goodbye!")
		leaving = True
	elif choice == 1:	
		print ("Here are all the restaurants I have!")
		list_restaurants()
	elif choice == 2:
		print ("Add a restaurant")
		add_restaurant()
	elif choice == 3:
		print ("Remove a restaurant")
		remove_restaurant();
	elif choice == 4:
		print ("Shuffling the list")

	elif choice == 5:
		print ("Starting the tournament!")