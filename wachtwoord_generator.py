# Maak een programma die een wachtwoord van 24 tekens genereerd.

# Het wachtwoord moet aan de volgende eisen voldoen:


# 2 tot 6 hoofdletters.
# Minimaal 8 kleine letters.
# 3 speciale tekens uit de volgende reeks: @ # $ % & _ ?.
# De speciale tekens mogen niet op de eerste of laatste positie staan en ook niet op een vaste plek.
# 4 tot 7 cijfers (0 t/m 9).,
# Op de eerste 3 posities mag geen cijfer 

import random
import string 



## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	## length of password from the user
	length = int(input("Enter password length: "))

	## shuffling the characters
	random.shuffle(characters)
	
	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	## printing the list
	print("".join(password))



## invoking the function
generate_random_password()