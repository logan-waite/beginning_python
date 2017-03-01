# From Quantum 7's code in stack overflow
# stackoverflow.com/posts/30259745/revisions

def to_alphabetic(i, base=26):
    if base < 0 or 62 < base:
        raise ValueError("Invalid Base")

    if i < 0:
        return '-' + to_alphabetic(-i-1)

    quot = int(i) / base
    rem = int(i) % base
    if rem < 26:
        letter = chr( ord("A") + rem)
    elif rem < 36:
        letter = str( rem - 26 )
    else:
        letter = chr( ord("a") + rem - 36)
    if quot == 0:
        return letter
    else:
        return to_alphabetic(quot - 1, base) + letter


user_choice = raw_input("Please enter a number\n")
number = int(user_choice) #- 1
print (to_alphabetic(number))
