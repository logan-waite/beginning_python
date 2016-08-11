number = input("Enter a number: \n")
num_array = list(str(number))

change_to_four = False
num_counter = 0 # Used for the index of the number array
magic_number = []
for num in num_array:
    if change_to_four:
        magic_number.append('4')
        continue

    if int(num) is 4 or int(num) is 7: # The number we want: don't touch it and move on.
        magic_number.append(num)
    elif int(num) < 4: # Less than 4: everything to the right of this number should be a 4 inclusive
        magic_number.append('4')
        change_to_four = True
    elif int(num) > 4 and int(num) < 7: # Between 4 and 7: this number is a 7 and everything to the right is a 4.
        magic_number.append('7')
        change_to_four = True
    elif int(num) > 7: # Bigger than a 7: everything to right is 4, number to left should be 4, moving left until a 4 changes to a 7 or we reach the far left, when we add one more 4.
        magic_number.append('4')
        while True: # Increment up until a 4 goes to a 7 or we reach the end
            i = 0 # counter
            if num_counter == 0 or (num_counter - i) == 0:
                magic_number.insert(0, "4")
                break
            elif num_array[num_counter - (i+1)] == '4':
                magic_number[i] = '7'
                break
            elif num_array[num_counter - (i+1)] == '7':
                magic_number[i] = '4'
            else:
                pass
        change_to_four = True
    num_counter += 1

print(''.join(magic_number))
