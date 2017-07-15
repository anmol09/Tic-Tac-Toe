

class game_board:


	values = {1:' ', 2 : ' ' , 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
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

		if game_board.values[self.value] == " ":
			game_board.values[self.value] = 'X'
		else:
			print("Already filled, enter another block or you entered the wrong symbol")
			return False
		return True


	
	def add_O(self,value):
		self.value = value

		if game_board.values[self.value] == " ":
			game_board.values[self.value] = 'O'
		else:
			print("Already filled, enter another block or you entered the wrong symbol")
			return False
		return True

	def __del__(self):
		# print("Creating a new board")


	def game_logic(self):

		self.count += 1

		if game_board.values[1] == game_board.values[2] == game_board.values[3]:
			if game_board.values[1]== 'X':
				self.display()
				print("Player 1 has won the game")
				exit()
			if game_board.values[1] == 'O':
				self.display()
				print("Player 2 has won the game")
				exit()

		if game_board.values[4] == game_board.values[5] == game_board.values[6]:
			if game_board.values[4]== 'X':
				self.display()
				print("Player 1 has won the game")
				exit()
			if game_board.values[4] == 'O':
				self.display()
				print("Player 2 has won the game")
				exit()

		if game_board.values[7] == game_board.values[8] == game_board.values[9]:
			if game_board.values[7]== 'X':
				self.display()
				print("Player 1 has won the game")
				exit()
			if game_board.values[7] == 'O':
				self.display()
				print("Player 2 has won the game")
				exit()

		if game_board.values[1] == game_board.values[4] == game_board.values[7]:
			if game_board.values[1]== 'X':
				self.display()
				print("Player 1 has won the game")
				exit()
			if game_board.values[1] == 'O':
				self.display()
				print("Player 2 has won the game")
				exit()	

		if game_board.values[2] == game_board.values[5] == game_board.values[8]:
			if game_board.values[2]== 'X':
				self.display()
				print("Player 1 has won the game")
				exit()
			if game_board.values[2] == 'O':
				self.display()
				print("Player 2 has won the game")
				exit()

		if game_board.values[3] == game_board.values[6] == game_board.values[9]:
			if game_board.values[3]== 'X':
				self.display()
				print("Player 1 has won the game")
				exit()
			if game_board.values[3] == 'O':
				self.display()
				print("Player 2 has won the game")
				exit()

		if game_board.values[1] == game_board.values[5] == game_board.values[9]:
			if game_board.values[1]== 'X':
				self.display()
				print("Player 1 has won the game")
				exit()
			if game_board.values[1] == 'O':
				self.display()
				print("Player 2 has won the game")
				exit()

		if game_board.values[7] == game_board.values[5] == game_board.values[3]:
			if game_board.values[3]== 'X':
				self.display()
				print("Player 1 has won the game")
				exit()
			if game_board.values[3] == 'O':
				self.display()
				print("Player 2 has won the game")
				exit()	





def print_instructions():


	print("Player 1 : 'X' \n ")
	print("Player 2 : 'O' \n")
	print("First player will take the first turn \n")
	print("You will see the board after every game \n")
	# print("You will get 10 seconds to chose an option \n")
	print("Enter i to see the instructions again\n ")
	# print("Enter r to restart again \n")
	print("Enter q to quit")

def game_run():
	board = game_board()

	while(True):

		board.display()
		# try:
		argument = raw_input()

		if argument == 'r':
			# print("I am here")
			# del board
			# board = game_board()
			continue

		elif argument == 'i':
			print_instructions()

		elif argument == 'q':
			exit()

		else:
			
			try:
				argument = int(argument)

				if int(argument)>9 or int(argument) <1:
					raise ValueError

				if board.count%2 == 1:
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
				print("Invalid input ")


		# except Exception:
		# 	print("Enter a valid input")



def main():
	print("Welcome to the Tic-Tac-Toe game \n")

	print_instructions()

	game_run()


if __name__ == '__main__':
  main()


