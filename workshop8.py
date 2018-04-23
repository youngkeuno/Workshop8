from graphics import*
from time import*
from random import*


#1)

#empty board fuction

def blank_board():
	print("     |    |   \n ---------------\n     |    |   \n --------------\n     |    | ")

blank_board()

#2)
#funcion that takes in list and prints a board. As a sidenote, the list of lists should include " " as empty spaces rather than "" to not mess up the spacing on the board. 

def list_as_board(board):
	print("  " + board[0][0] + " |  " + board[0][1] + " |  " + board[0][2] + "  \n --------------- \n  " + board[1][0] + " |  " + board[1][1] + " |  " + board[1][2] + "  \n --------------- \n  " + board[2][0] + " |  " + board[2][1] + " |  " + board[2][2])

board=[[" ","X","O"],[" "," ","X"],["O","O","O"]]

list_as_board(board) 

#3)

def X_won(board):
	n=0
	for x in board:
		if x==["X","X","X"]:
			n=1
	for y in [0,1,2]:
		if board[0][y]=="X" and board[1][y]=="X" and board[2][y]=="X":
			n=1
	if board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
		n=1
	if board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X":
		n=1
	if n==1:
		print("X won")
	if n==0:
		print("X didn't win")

X_won(board)

board1=[[" ","X","O"],[" "," ","X"],["X","X","X"]]

X_won(board1)

def O_won(board):
	n=0
	for x in board:
		if x==["O","O","O"]:
			n=1
	for y in [0,1,2]:
		if board[0][y]=="O" and board[1][y]=="O" and board[2][y]=="O":
			n=1
	if board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
		n=1
	if board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O":
		n=1
	if n==1:
		print("O won")
	if n==0:
		print("O didn't win")

O_won(board)

O_won(board1)

def who_won(board):
	n=0
	for x in board:
		if x==["X","X","X"]:
			n=1
	for y in [0,1,2]:
		if board[0][y]=="X" and board[1][y]=="X" and board[2][y]=="X":
			n=1
	if board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
		n=1
	if board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X":
		n=1
	m=0
	for x in board:
		if x==["O","O","O"]:
			m=1
	for y in [0,1,2]:
		if board[0][y]=="O" and board[1][y]=="O" and board[2][y]=="O":
			m=1
	if board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
		m=1
	if board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O":
		m=1
	if n==0 and m==1:
		print("O won")
	if n==1 and m==0:
		print("X won")
	if n==0 and m==0:
		print("tied")
	if n==1 and m==1:
		print("Something's wrong. There's no clear winner")

who_won(board)
who_won(board1)

board2=[["Y","X","Y"],["Y","X","Y"],["X","Y","X"]]

who_won(board2)
	

#4

def who_won_return(board):
	n=0
	for x in board:
		if x==["X","X","X"]:
			n=1
	for y in [0,1,2]:
		if board[0][y]=="X" and board[1][y]=="X" and board[2][y]=="X":
			n=1
	if board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
		n=1
	if board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X":
		n=1
	m=0
	for x in board:
		if x==["O","O","O"]:
			m=1
	for y in [0,1,2]:
		if board[0][y]=="O" and board[1][y]=="O" and board[2][y]=="O":
			m=1
	if board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
		m=1
	if board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O":
		m=1
	if n==0 and m==1:
		return("O won")
	if n==1 and m==0:
		return("X won")
	if n==0 and m==0:
		return("tied")
	if n==1 and m==1:
		return("Something's wrong. There's no clear winner")

def end_game_tie(board):
	n=0
	j=0
	for x in [0,1,2]:
		for y in [0,1,2]:
			if board[x][y]!=" ":
				j=0
			else:
				n=1
	if n==0:
		return("tie")
	if n==1:
		return("game not complete")


def game():
	blank_board()
	x=[[" "," "," "],[" "," "," "],[" "," "," "]]
	while who_won_return(x)=="tied" and end_game_tie(x)=="game not complete":
		if end_game_tie(x)=="game not complete":
			xmove=input("Where does X want to move? Write two numbers and a comma as follows: 'row number , column number' with no spaces in between the comma  ")
			if x[int(xmove[0])][int(xmove[2])]==" ":
				x[int(xmove[0])][int(xmove[2])]="X"
			else: 
				j="that spot is taken"
				print(j)
				while j=="that spot is taken":
					xmove=input("Where does X want to move? Write two numbers and a comma as follows: 'row number , column number' with no spaces in between the comma  ")
					if x[int(xmove[0])][int(xmove[2])]==" ":
						x[int(xmove[0])][int(xmove[2])]="X"
						end_game_tie(x)
					else:
						print(j)
						end_game_tie(x)
			list_as_board(x)
			end_game_tie(x)
		else:
			end_game_tie(x)
		if end_game_tie(x)=="game not complete":
			omove=input("Where does O want to move? Write two numbers and a comma as follows: 'row number , column number' with no spaces in between the comma  ")
			if x[int(omove[0])][int(omove[2])]==" ":
				x[int(omove[0])][int(omove[2])]="O"
			else: 
				j="that spot is taken"
				print(j)
				while j=="that spot is taken":
					omove=input("Where does O want to move? Write two numbers and a comma as follows: 'row number , column number' with no spaces in between the comma  ")
					if x[int(omove[0])][int(omove[2])]==" ":
						x[int(omove[0])][int(omove[2])]="O"
						j="spot free"
						end_game_tie(x)
					else:
						print(j)
						end_game_tie(x)
			list_as_board(x)
			end_game_tie(x)
		else:
			end_game_tie(x)
	if who_won_return(x)!="tied":
		who_won(x)
	if who_won_return(x)=="tied" and end_game_tie(x)=="tie":
		who_won(x)
game()

input("press a key to continue")

