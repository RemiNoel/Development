'Started : 10-dec-2015'
'Done : TBD'
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
	print("Hello! This is a simple game of Tic-Tac-Toe. \n")
	print("Now you may the players' names. You can also leave it blank if you want or play with a computer. \n")

	while not (letter == 'Y' or letter == 'N'):
		print('Do you want to play against a computer? Yes(Y) or no(N)?')
		letter = input().upper()
		#playWithComp = True
		#No AI has been currently implemented. Will be done soon.
		
	print("Please enter the name of the player #1: ")
	playersNames['Player #1'] = input()
	if playWithComp == False:
		print("Thanks " + playersNames['Player #1'] + "!\nNow may player #2 enter their name: ")
		playersNames['Player #2'] = input()
		print("Thanks " + playersNames['Player #2'] + "!\nEnjoy and good luck to both players!\n\n")
	else:
		print("Thanks " + playersNames['Player #1'] + "!\nEnjoy and good luck against the computer!")
		playersNames['Player #2'] = 'Computer'
	cls()

def restartGame():
	theBoard.values() = ' '

def whoGoesFirst():
# Randomly choose the player who goes first.
	if random.randint(0, 1) == 0:
		return playersNames['Player #1']
	else:
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
	print ("\n" * 100) 

def checkBoardCase(board, move):
	if not(board[move] == ' '):
		print("This case has already been played! Please choose another case. \n")
		return False
	else:
		return True

def checkIfPlayerWins(board, letter):
	return ((letter == theBoard["TOP-L"] and letter == theBoard["TOP-M"] and letter == theBoard["TOP-R"]) or 
		(letter == theBoard["MID-L"] and letter == theBoard["MID-M"] and letter == theBoard["MID-R"]) or
		(letter == theBoard["LOW-L"] and letter == theBoard["LOW-M"] and letter == theBoard["LOW-R"]) or	# check horizontals
		(letter == theBoard["TOP-L"] and letter == theBoard["MID-L"] and letter == theBoard["LOW-L"]) or
		(letter == theBoard["TOP-M"] and letter == theBoard["MID-M"] and letter == theBoard["LOW-M"]) or	# check verticals 
		(letter == theBoard["TOP-R"] and letter == theBoard["MID-R"] and letter == theBoard["LOW-R"]) or
		(letter == theBoard["TOP-L"] and letter == theBoard["MID-M"] and letter == theBoard["LOW-R"]) or 	# check diagonals
		(letter == theBoard["LOW-L"] and letter == theBoard["MID-M"] and letter == theBoard["TOP-R"]))

def gameLoop():	
	moveCount = 0
	gameState = True
	winnerState = False
	firstToPlay = ''
	firstToPlay = whoGoesFirst()

	if firstToPlay == playersNames['Player #1']:
		turn = 'X'
	else:
		turn = 'O'

	while(gameState):

		for i in range(9):
			printBoard(theBoard)
			print('Turn for ' + turn + '. Move on which space?')
			move = input().upper()
			while not move in theBoard.keys():
				print("Those are the valid moves available: ")
				pp = pprint.PrettyPrinter()
				pp.pprint(theBoard.keys().sorted())
				print("Please choose a valid move: ")
				move = input().upper()
				
			if checkBoardCase(theBoard, move) == True:
				theBoard[move] = turn

				# Store the coordinates of the hit and switch players
				if turn == 'X':
					turn = 'O'
				else : 
					turn = 'X'
				moveCount += 1
				print(str(moveCount) + '\n')

			# Check if someone won	
			if moveCount >= 4:
				if moveCount == 9:
					print('Draw!\n')
					gameState = decideGameState()

				winnerState = checkIfPlayerWins(theBoard, turn)
				if winnerState:
					if turn == 'X':
						print(playersNames['Player #1'] + " won! Congratulations!")
						gameState = decideGameState()
					elif turn == 'O':
						print(playersNames['Player #2'] + " won! Congratulations!")
						gameState = decideGameState()

		print("\n")
		printBoard(theBoard)



# Start the game	
startGame()

# Game loop
gameLoop()

