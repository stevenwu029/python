import random
import time
def print_board(board):
	
	length = len(board[0]) #this is coloum
	width = len(board) #this is row
	for length in range(len(board[0])):
		for width in range(len(board)):
			print(board[length][width],end = "")
		print()
		


def tieCheck(board):
	count = 0
	rowOne = False
	rowTwo = False
	rowThree = False
	columnOne = False
	columnTwo = False
	columnThree = False
	crossOne = False
	crossTwo = False


	if (board[1][1] == p1_shape or board[1][2] == p1_shape or board[1][3] == p1_shape) and (board[1][1] == p2_shape or board[1][2] == p2_shape or board[1][3] == p2_shape):
		rowOne = True
	if (board[2][1] == p1_shape or board[2][2] == p1_shape or board[2][3] == p1_shape) and (board[2][1] == p2_shape or board[2][2] == p2_shape or board[2][3] == p2_shape):
		rowTwo = True
	if (board[3][1] == p1_shape or board[3][2] == p1_shape or board[3][3] == p1_shape) and (board[3][1] == p2_shape or board[3][2] == p2_shape or board[3][3] == p2_shape):
		rowThree = True
	if (board[1][1] == p1_shape or board[2][1] == p1_shape or board[3][1] == p1_shape) and (board[1][1] == p2_shape or board[2][1] == p2_shape or board[3][1] == p2_shape):
		columnOne = True
	if (board[1][2] == p1_shape or board[2][2] == p1_shape or board[3][2] == p1_shape) and (board[1][2] == p2_shape or board[2][2] == p2_shape or board[3][2] == p2_shape):
		columnTwo = True
	if (board[1][3] == p1_shape or board[2][3] == p1_shape or board[3][3] == p1_shape) and (board[1][3] == p2_shape or board[2][3] == p2_shape or board[3][3] == p2_shape):
		columnThree = True
	if (board[1][1] == p1_shape or board[2][2] == p1_shape or board[3][3] == p1_shape) and (board[1][1] == p2_shape or board[2][2] == p2_shape or board[3][3] == p2_shape):
		crossOne = True
	if (board[1][3] == p1_shape or board[2][2] == p1_shape or board[3][1] == p1_shape) and (board[1][3] == p2_shape or board[2][2] == p2_shape or board[3][1] == p2_shape):
		crossTwo = True

	if rowOne == rowTwo == rowThree == columnOne == columnTwo == columnThree == crossOne == crossTwo == True:
		return True
	return False


def check_p1(board,p1_shape):
	if board[1][1] == board[1][2] == board[1][3] == p1_shape:
		return True
	elif board[2][1] == board[2][2] == board[2][3] == p1_shape:
		return True
	elif board[3][1] == board[3][2] == board[3][3] == p1_shape:
		return True
	elif board[1][1] == board[2][1] == board[3][1] == p1_shape:
		return True
	elif board[2][1] == board[2][2] == board[2][3] == p1_shape:
		return True
	elif board[3][1] == board[3][2] == board[3][3] == p1_shape:
		return True
	elif board[1][1] == board[2][2] == board[3][3] == p1_shape:
		return True
	elif board[1][3] == board[2][2] == board[3][1] == p1_shape:
		return True
	else:
		return False

def check_p2(board,p2_shape):
	if board[1][1] == board[1][2] == board[1][3] == p2_shape:
		return True
	elif board[2][1] == board[2][2] == board[2][3] == p2_shape:
		return True
	elif board[3][1] == board[3][2] == board[3][3] == p2_shape:
		return True
	elif board[1][1] == board[2][1] == board[3][1] == p2_shape:
		return True
	elif board[2][1] == board[2][2] == board[2][3] == p2_shape:
		return True
	elif board[3][1] == board[3][2] == board[3][3] == p2_shape:
		return True
	elif board[1][1] == board[2][2] == board[3][3] == p2_shape:
		return True
	elif board[1][3] == board[2][2] == board[3][1] == p2_shape:
		return True
	else:
		return False
p1_shape = "\tX"
p2_shape = "\tO"


print("Let's start a game :)")
player1 = input("Give me your name player1 ")
player1_roll = random.randint(1,6)

player2 = input("Give me your name player2 ")
player2_roll = random.randint(1,6)


if (player1_roll == player2_roll):
	player1_roll = 10
	player2_roll = 1

someone_win = False
out_of_space = False
if player1_roll > player2_roll:
	player1_move = True
	player2_move = False
	switch = False
	print(player1 + " moves first")
else:
	player1_move = False
	player2_move = True
	switch = True
	print(player2 + " moves first")

count_for_stupidity = 0
out_of_game = False
time.sleep(1.0)
print("RULE:")
print("Always give TWO numbers that are smaller or equal to 3")
print("Coloum first, then row")
print("Here's the board")
board = [
	[" ","\t1","\t2","\t3"],
	["\n1"," \t"," \t"," \t"],
	["\n2"," \t"," \t"," \t"],
	["\n3"," \t"," \t"," \t"],
	] 
print_board(board)

while not someone_win or not out_of_space:

	
	if tieCheck(board) == True:
		print("You guys reach a tie!")
		break

	if switch == False:
			player1_move = True
			player2_move = False
	else:
		player1_move = False
		player2_move = True
		

	if player1_move:
		row,coloum = input("What's your next move {}? ".format(player1)).split()
		if board[int(row)][int(coloum)] == " \t":
			board[int(row)][int(coloum)] = p1_shape
		else:
			while board[int(row)][int(coloum)] != "   ":
				row,coloum = input("YOOOOO Man, Give me a vacant position").split()
				count_for_stupidity += 1
				if count_for_stupidity >= 2:
					out_of_game = True
					break
			if out_of_game == True:
				print("It's time to see a doctor " + player1)
				break
			count_for_stupidity = 0
			board[int(row)][int(coloum)] = p1_shape
		print_board(board)
		switch = True
		someone_win = check_p1(board,p1_shape)
		if someone_win == True:
			print("YOOOOO " + player1 + " WINS THE GAME!!!!")
			break


	elif player2_move:
		row,coloum = input("What's your next move {} ? ".format(player2)).split()
		if board[int(row)][int(coloum)] == " \t":
			board[int(row)][int(coloum)] = p2_shape
		else:
			while board[int(row)][int(coloum)] != "   ":
				row,coloum = input("YOOOOO Man, Give me a vacant position ").split()
				count_for_stupidity += 1
				if count_for_stupidity >= 2:
					out_of_game = True
					break
			if out_of_game == True:
				print("It's time to see a doctor " + player2)
				break
			count_for_stupidity = 0
			board[int(row)][int(coloum)] = p2_shape
				

		print_board(board)
		switch = False
		someone_win = check_p2(board,p2_shape)
		if someone_win == True:
			print("YOOOOO " + player2 + " WINS THE GAME!!!!")
			break




	











