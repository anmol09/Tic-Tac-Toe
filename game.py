

class game_board:
	board_values = {'top-L':'','top-M':'','top-R':'','low-L':'','low-M':'','low-R':'','mid-L':'','mid-M':'','mid-R':''}	
	player = {'X':'', 'O': ''}

	def __init__(self,player_1,player_2):
		self.player['X'] = player_1
		self.player['O'] = player_2


	def display(self):
		print(board_values['top-L'] + '|' + board_values['top-M'] + '|' + board_values['top-R'])
    	print('-+-+-')
    	print(board_values['mid-L'] + '|' + board_values['mid-M'] + '|' + board_values['mid-R'])
    	print('-+-+-')
    	print(board_values['low-L'] + '|' + board_values['low-M'] + '|' + board_values['low-R'])

    def add_X(self,value):
    	
    	self.value = value
    	keys = board_values.keys()

    	for key in keys:
    		if key == value:
    			board_values[key] = 'X'

    def add_O(self,value):

    	self.value = value 
    	keys = board_values.key()

    	for key in keys:
    		if key == value:
    			board_values[key] = 'O'


def main():
	print("Welcome to the tic tac toe game! ")
	print("Get ready to play with your friend ")
	player_1 = input("Name player which wants 'X'")
	player_2 = input("Name player which wants 'O'")

	board_game = game_board(player_1,player_2)




def game_logic():


def print_instructions():
