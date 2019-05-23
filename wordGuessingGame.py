#!/usr/bin/env python3
from random import randint


word_list = ['python', 'women', 'programming', 'money', 'rangerover',
'accounting', 'computerized', 'netwoking', 'javascript', 'widow', 'security',
'anonymous', 'liberation', 'government', 'nairobi', 'information', 'blessings']

def random_word():
	size = len(word_list)
	random_num = randint(0, size-1)
	return word_list[random_num]


magic_word = random_word()


def check_if_user_is_correct(guessed_word):
	if guessed_word == magic_word:
		return True
	elif guessed_word != magic_word:
		return False
	else:
		pass

def main():
	det = 0
	while True:
		print()
		userInput = input('Guess any word of your choice: ')
		guess = check_if_user_is_correct(userInput)

		if guess is True:
			print()
			print('Congrats! You win.')
			break
		elif guess is False:
			det += 1
			print()
			print('Loser! Try again.')

			if det is 3:
				print()
				print('Hint: ' + magic_word[0:4] + '.')
				continue
			else:
				continue


if __name__ == '__main__':
	main()
