import string
#help(string) #affiche tout ce que contient la bibliothèque string

alphabet = string.printable + "éèêàôëùïü"

def cesar_cipher(message, key):

	crypted_message = ""
	for char in message:
		"""
		on va chiffrer le caractère 
			1- trouver la positon du carac dans l'alphabet
			2- y rajouter la clef à la positon du carac dans l'alphabet
			3- reccupérer le caractère chiffré
		on va stocker le caractère chiffrer
		"""
		index_carac_in_printable = alphabet.index(char)
		index_crypted_char = (index_carac_in_printable + key) % len(alphabet)
		cryted_char = alphabet[index_crypted_char]

		crypted_message += cryted_char
	
	return crypted_message


def cesar_uncipher(crypted_message, key):
	return cesar_cipher(crypted_message, -key)

crypted_message = cesar_cipher("salut les bgs aujourd'hui on va corriger l'exercice", 13)
print(crypted_message)

def brute_force_cesar_cipher(crypted_message):
	for possible_key in range(0, len(alphabet)):
		print(cesar_uncipher(crypted_message, possible_key))
		print("_"*15)


brute_force_cesar_cipher(crypted_message)


def convert_password_to_list_of_keys(password):
	list_of_keys = []
	for char in password:
		list_of_keys.append(alphabet.index(char))
	return list_of_keys



def vigenere_cipher(message, password, reverse=False):
	list_of_keys = convert_password_to_list_of_keys(password)
	crypted_message = ""
	
	for index, char in  enumerate(message):
		current_key = list_of_keys[index % len(list_of_keys)]
		crypted_message += cesar_uncipher(char, current_key) if reverse else cesar_cipher(char, current_key)

	return crypted_message


