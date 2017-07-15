

class game_board:

	board_values = {1:'', 2 : '' , 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
	#player = {'X':'', 'O': ''}

	def __init__(self,player_1,player_2):
		self.player['X'] = player_1
		self.player['O'] = player_2


	def display(self):
		print(game_board.board_values[1] + '|' + game_board.board_values[2] + '|' + game_board.board_values[3])
		print('-+-+-')
		print(game_board.board_values[4] + '|' + game_board.board_values[5] + '|' + game_board.board_values[6])
		print('-+-+-')
		print(game_board.board_values[7] + '|' + game_board.board_values[8] + '|' + game_board.board_values[9])

	def add_X(self,value):
		self.value = value
		keys = game_board.board_values.key()

		for key in keys:
			if key == value:
				game_board.board_values[key] = 'X'
	
	def add_O(self,value):
		
		self.value = value 
		keys = game_board.board_values.key()

		for key in keys:
			if key == value:
				game_board.board_values[key] = 'O'


def main():
	print("Welcome to the tic tac toe game! ")
	print("Get ready to play with your friend ")
	player_1 = input("Name player which wants 'X'")
	player_2 = input("Name player which wants 'O'")



	board_game = game_board(player_1,player_2)



main()
#def game_logic():


#def print_instructions():

# Diagnosis Code: 300
# Service Code: A007