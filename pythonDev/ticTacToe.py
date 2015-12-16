'Date : 10-dec-2015'
'By : Remi Noel'

'This python script contains the code for a tic tac toe game'
import random
import pprint

theBoard = {'TOP-L': ' ', 'TOP-M': ' ', 'TOP-R': ' ',
            'MID-L': ' ', 'MID-M': ' ', 'MID-R': ' ',
            'LOW-L': ' ', 'LOW-M': ' ', 'LOW-R' : ' '}

playersNames = {'Player #1' : ' ', 'Player #2' : ' '}

playWithComp = False

def startGame():
	letter = ''
	print('Hello! This is a simple game of Tic-Tac-Toe. \n')
	
	while not (letter == 'Y' or letter == 'N'):
		print('Do you want to play against a computer? Yes(Y) or no(N)?')
		letter = input().upper()
		#playWithComp = True
		#No AI has been currently implemented. Will be done soon.
	
	print('Now you may enter the players'' names. You can also leave it blank. \n')	
	print('Please enter the name of the player #1: ')
	playersNames['Player #1'] = input()
	if playWithComp == False:
		print('Thanks ' + playersNames['Player #1'] + '!\nNow may player #2 enter their name: ')
		playersNames['Player #2'] = input()
		print('Thanks ' + playersNames['Player #2'] + '!\nEnjoy and good luck to both players!\n\n')
	else:
		print('Thanks ' + playersNames['Player #1'] + '!\nEnjoy and good luck against the computer!')
		playersNames['Player #2'] = 'Computer'
	cls()

def restartGame():
	for key in theBoard.keys():
		theBoard[key] = ' '
		cls()


def whoGoesFirst():
# Randomly choose the player who goes first.
	if random.randint(0, 1) == 0:
		return playersNames['Player #1']
	return playersNames['Player #2']

def decideGameState():
	print('Do you want to play again? (yes or no)')
	if input().lower().startswith('y'):
		restartGame()
		return True
	return False

def printBoard(board):
	print(board['TOP-L'] + '|' + board['TOP-M'] + '|' +  board['TOP-R'])
	print('-+-+-')
	print(board['MID-L'] + '|' + board['MID-M'] + '|' +  board['MID-R'])
	print('-+-+-')
	print(board['LOW-L'] + '|' + board['LOW-M'] + '|' +  board['LOW-R'])

def cls():
	print ('\n' * 100) 

def checkBoardCase(board, move):
	if not(board[move] == ' ') :
		print('This case has already been played! Please choose another case. \n')
		return False
	return True

def checkIfPlayerWins(board, letter):
	return ((letter == board['TOP-L'] and letter == board['TOP-M'] and letter == board['TOP-R']) or # check horizontals Top
			(letter == board['MID-L'] and letter == board['MID-M'] and letter == board['MID-R']) or	#					Mid
			(letter == board['LOW-L'] and letter == board['LOW-M'] and letter == board['LOW-R']) or	#					Low
			(letter == board['TOP-L'] and letter == board['MID-L'] and letter == board['LOW-L']) or	# check verticals 	Left
			(letter == board['TOP-M'] and letter == board['MID-M'] and letter == board['LOW-M']) or	#				  	Mid
			(letter == board['TOP-R'] and letter == board['MID-R'] and letter == board['LOW-R']) or	#				  	Right
			(letter == board['TOP-L'] and letter == board['MID-M'] and letter == board['LOW-R']) or # check diagonals 	Top-L to Low-R
			(letter == board['LOW-L'] and letter == board['MID-M'] and letter == board['TOP-R']))	#				  	Low-L to Top-R

def gameLoop():	
	moveCount = 0
	gameState = True
	winnerState = False
	drawState = False
	firstToPlay = ''
	firstToPlay = whoGoesFirst()

	if firstToPlay == playersNames['Player #1']:
		turn = 'X'
	else:
		turn = 'O'

	while(gameState):
		printBoard(theBoard)
		print('\n Turn for ' + turn + '. Move on which space?')
		move = input().upper()
		print('\n')

		while not move in theBoard.keys():
			print('Those are the valid moves available: ')
			pp = pprint.PrettyPrinter()
			pp.pprint(sorted(theBoard.keys()))
			print('Please choose a valid move: \n')
			printBoard(theBoard)
			move = input().upper()
			
		if checkBoardCase(theBoard, move) == True:
			theBoard[move] = turn

		# Check if someone won	
		if moveCount >= 4:
			if moveCount == 9:
				print('Draw!\n')
				drawState = True
				gameState = decideGameState()

			elif drawState == False:
				winnerState = checkIfPlayerWins(theBoard, turn)
				if winnerState:
					if turn == 'X':
						print(playersNames['Player #1'] + ' won! Congratulations!')
						gameState = decideGameState()
						moveCount = 0
					elif turn == 'O':
						print(playersNames['Player #2'] + ' won! Congratulations!')
						gameState = decideGameState()
						moveCount = 0
		# Switch players
		if turn == 'X':
			turn = 'O'
		else : 
			turn = 'X'
		moveCount += 1

		print('\n')



# Start the game	
startGame()

# Game loop
gameLoop()

