import random
import string

def game_start():

	# get all the words from the file
	wordlist = [line.strip() for line in open('wordlist.txt')]

	# pick a word
	myst_word = wordlist[random.randint(0, 58108)].upper()

	# set of guessed letters
	guessed_letters = set()
	# set of word letters
	word_letters = set(myst_word)
	# set of the alphabet
	alphabet = set(string.ascii_uppercase)

	# number of turns
	turns = 10 
	# game loop
	while len(word_letters) > 0 and turns > 0:

		word = [letter if letter in guessed_letters else '-' for letter in myst_word]
		print("Word: ", ''.join(word))
		print("Turn: ", turns, "Guessed letters: ", ' '.join(guessed_letters))

		guess = input("Take a guess: ").upper()
		if guess in alphabet - guessed_letters:
			guessed_letters.add(guess)
			
			if guess in word_letters:
				word_letters.remove(guess)
				print('')

			else:
				turns-=1
				print("\nLetter ", guess, ' is not on the word.')

		else:
			print("\nLetter alread guessed. Try again.")

	if turns == 0:
		print("Game over. You lost.\n")

	else:
		print('You guessed the word. You win.\n')



def game():
	print("Hangman Game")

	exit = False

	while not exit:
		new_game = input("\nStart new game? y/n: ")

		if new_game.lower() == 'y':
			print('')
			game_start()

		elif new_game.lower() == 'n':
			print("Quitting the game.")
			quit()
		else:
			print("Input is not correct.\n ")

def main():
	game()

if __name__ == '__main__':
	main()