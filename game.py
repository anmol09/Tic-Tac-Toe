

class game_board:
	board_values = {'top-L':'','top-M':'','top-R':'','low-L':'','low-M':'','low-R':'','mid-L':'','mid-M':'','mid-R':''}	

	def __init__(self,player_1,player_2):
		self.player_1 = player_1
		self.player_2 = player_2


	def display():
		print(board['topL'] + '|' + board['top-M'] + '|' + board['top-R'])
    	print('-+-+-')
    	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    	print('-+-+-')
    	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])



def main():
	print("Welcome to the tic tac toe game! ")
	print("Get ready to play with your friend ")
	player_1 = input("Name player which wants 'X'")
	player_2 = input("Name player which wants 'O'")

	board_game = game_board(player_1,player_2)




def game_logic():


def print_instructions():
