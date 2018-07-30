import random

target = random.randrange(0, 101)

x = int(input('Generate a random number between 0 and 100 (inclusive): '))
number_of_tries = 10

while number_of_tries >= 0:
	number_of_tries -= 1
	if x < target:
		print('Your guess is low\n')
		if number_of_tries == 0:
			print('You have lost the game.')
			break
		x = int(input('Try again: '))
	elif x > target:
		print('Your guess is high\n')

		if number_of_tries == 0:
			print('You have lost the game.')
			break
		x = int(input('Try again: '))
	elif x == target:
		print('You guessed right!')
		x = 'winner'
		break
	
# if x != 'winner':
# 	print('You have lost the game')





	
