############################################
# ASCII encrypter v3
# Uses ASCII values to encrypt a user
# generated password.
############################################

from random import randint

MIN_VALUE = 65
MAX_VALUE = 122

# dictionary for later use

def encrypt(userPass):

	newPass = ''

	for char in userPass:

		# ASCII value of the character
		newCharValue = ord(char)
		
		# gives two options 0 and 1 		
		coinFlip = randint(0, 1)
		
		# if coin lands on 0, set to minimum and add a random
		# integer to the ASCII of the character
		if (coinFlip == 0):
			newCharValue = MIN_VALUE + randint(0, MAX_VALUE - MIN_VALUE)
		# if coin lands on 1, set to maximum and subtract a random
		# integer to the ASCII of the character
		else:
			newCharValue = MAX_VALUE - randint(0, MAX_VALUE - MIN_VALUE)
		
		# grabs the character value of the ASCII number 
		# stores it
		newChar = chr(newCharValue)
		
		# adds the new character to the encrypted password
		newPass += newChar
	
	return newPass

