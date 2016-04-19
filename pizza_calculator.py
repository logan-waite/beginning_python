print ("Pizza Calculator! \n")

import math

a_number = False

while not a_number:
	user_input = raw_input("How many guests will be attending?\n")
	try:
		guest_count = int(user_input)
		a_number = True
	except ValueError:
		print ("Not a whole number! Try again")

larges = 0
mediums = 0
smalls = 0

larges = guest_count / 7
large_leftovers = guest_count % 7
mediums = large_leftovers / 3
smalls = large_leftovers % 3


print("Large pizzas needed: " + str(larges))
print("Medium pizzas needed: " + str(mediums))
print("Small pizzas needed: " + str(smalls))
