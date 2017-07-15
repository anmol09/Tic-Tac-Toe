

class game_board:


	values = {1:'', 2 : '' , 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
	#player = {'X':'', 'O': ''}

	def __init__(self):
		self.count = 1



	def display(self):
		print(game_board.values[1] + '|' + game_board.values[2] + '|' + game_board.values[3])
		print('-+-+-')
		print(game_board.values[4] + '|' + game_board.values[5] + '|' + game_board.values[6])
		print('-+-+-')
		print(game_board.values[7] + '|' + game_board.values[8] + '|' + game_board.values[9])

	def add_X(self,value):
		self.value = value

		if game_board.values[self.value] == ""
			game_board.values[key] = 'X'
		else:
			print("Already filled, enter another block or you entered the wrong symbol")
			return False
		reutrn True


	
	def add_O(self,value):
		self.value = value

		if game_board.values[self.value] == ""
			game_board.values[key] = 'O'
		else:
			print("Already filled, enter another block or you entered the wrong symbol")
			return False
		reuturn True

	def game_logic(self):

		self.count += 1

		if game_board.values[1] == game_board.valeus[2] == game_board.values[3]:
			if game_board.values[1]== 'X':
				print("Player 1 has won the game")
				exit()
			if game_board.values[1] == 'O':
				print("Player 2 has won the game")
				exit()

		if game_board.values[4] == game_board.valeus[5] == game_board.values[6]:
			if game_board.values[4]== 'X':
				print("Player 1 has won the game")
				exit()
			if game_board.values[4] == 'O':
				print("Player 2 has won the game")
				exit()

		if game_board.values[7] == game_board.valeus[8] == game_board.values[9]:
			if game_board.values[7]== 'X':
				print("Player 1 has won the game")
				exit()
			if game_board.values[7] == 'O':
				print("Player 2 has won the game")
				exit()

		if game_board.values[1] == game_board.valeus[4] == game_board.values[7]:
			if game_board.values[1]== 'X':
				print("Player 1 has won the game")
				exit()
			if game_board.values[1] == 'O':
				print("Player 2 has won the game")
				exit()	

		if game_board.values[2] == game_board.valeus[5] == game_board.values[8]:
			if game_board.values[2]== 'X':
				print("Player 1 has won the game")
				exit()
			if game_board.values[2] == 'O':
				print("Player 2 has won the game")
				exit()

		if game_board.values[3] == game_board.valeus[6] == game_board.values[9]:
			if game_board.values[3]== 'X':
				print("Player 1 has won the game")
				exit()
			if game_board.values[3] == 'O':
				print("Player 2 has won the game")
				exit()

		if game_board.values[1] == game_board.valeus[5] == game_board.values[9]:
			if game_board.values[1]== 'X':
				print("Player 1 has won the game")
				exit()
			if game_board.values[1] == 'O':
				print("Player 2 has won the game")
				exit()

		if game_board.values[7] == game_board.valeus[5] == game_board.values[3]:
			if game_board.values[3]== 'X':
				print("Player 1 has won the game")
				exit()
			if game_board.values[3] == 'O':
				print("Player 2 has won the game")
				exit()	



def main():
	print("Welcome to the Tic-Tac-Toe game ")

	print_instructions()

	game_run()






def print_instructions():


	print("Player 1 : 'X'")
	print("Player 2 : 'O'")
	print("First player will take the first turn")
	print("You will see the board after every game")
	print("You will get 10 seconds to chose an option")
	print("Enter i to see the instructions again")
	print("Enter r to restart again")

def game_run():
	board = game_board()

	while(True):

		argument = input()

		if argument == 'r':
			del board
			board = game_board()
			continue

		elif argument == 'i':
			print_instructions()

		else:

			try:
				if argument>9 || argument <1:
					raise ValueError

				if game_board.count%2 == 1:
					status_X = board.add_X(argument)
					if status_X:
						board.game_logic()
					else:
						continue
				else:
					status_O = board.add_O(argument)
					if status_O:
						board.game_logic()
					else:
						continue
				
			except ValueError:
				print("Enter an inbound value (1-9)")







main()






# Diagnosis Code: 300
# Service Code: A007