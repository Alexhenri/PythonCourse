
# HERE WE DISPLAY THE TIC TAC TOE GAME
def display_Tic_Tac_Toe(mlist):
	print('\n'*100)
	print('  {}  |  {}  |   {}  '.format(mlist[0], mlist [1], mlist[2]))
	print('------------------')
	print('  {}  |  {}  |   {}  '.format(mlist[3], mlist [4], mlist[5]))
	print('------------------')
	print('  {}  |  {}  |   {}  '.format(mlist[6], mlist [7], mlist[8]))

# HERE WE GET THE PLAYER'S NAMES 
def getPlayersName():
	playerOne = input('Type the name of Player One\n')
	print('Hello {} you will be "X"'.format(playerOne))
	playerTwo =	input('Type the name of Player Two\n')
	print('Hello {} you will be "O"'.format(playerTwo))

	return ([playerOne, 'X'] , [playerTwo, 'O'])

# HERE WE CHECK IF SOMEONE WIN THE GAME
def checkWinGame(mlist, count):
	for n in range(0,3):
		if mlist[3 * n] == mlist[ 3 * n + 1] == mlist[ 3 * n + 2] and mlist[3 * n] != ' ':
			return True
		elif mlist[n] == mlist[ n + 3] == mlist[ n + 6] and mlist[n] != ' ':
			return True
	
	if (mlist[0] == mlist[4] == mlist[8] and mlist[4] != ' ' ) or (mlist[2] == mlist[4] == mlist[6] and mlist[4] != ' '):
		return True
	
	return False

# HERE WE GET THE PLAYER'S INPUT 
def getPlayersInput(gc, names, mlist):
	playInput =  input('{} please make your move (1-9)!\n'.format(names[gc % 2][0]))
	# TRY IF IS A NUMBER - INT(INPUT) AND mlist[INPUT - 1] TRY IF RANGE IN (0, 10)
	try:
		playInput = int(playInput)

		# CHECK IF INPUT IS ALREADY CHOOSEN, IF SO, GET INPUT AGAIN
		if mlist[playInput - 1] != ' ':
			print('Sorry but you cannot make this move!')
			return getPlayersInput(gc,names,mlist)
		return (playInput - 1)
	except:
		print('Sorry but you have to pick an integer from 1 to 9.')
		return getPlayersInput(gc,names,mlist)

# HERE WE CHECK IF USER WANTS TO PLAY ANOTHER GAME
def checkAnotherGame():
	anotherGame = input('Start another game? (Y/N) \n')
	while anotherGame not in ['Y','y','N', 'n']:
		print("Sorry, i don't understand. Please type Y for Yes, N for No!")
		anotherGame = input('Start another game? (Y/N) \n')

	if anotherGame.lower() == 'y':
		changeNames = input('With the same names? (Y/N) \n')
		while changeNames not in ['Y','y','N', 'n']:
			print("Sorry, i don't understand. Please type Y for Yes, N for No!")
			changeNames = input('With the same names? (Y/N) \n')
		if changeNames.lower() == 'y':
			return (True, False)
		else: 
			return (True, True)

	return (False, False)


# START 
print('Welcome to Tic Tac Toe Game')
getNames = True


while True:

	# GET NAME (name, symbol)
	if(getNames):
		names = getPlayersName()

	# INITIALIZE VARIABLES 
	mylist = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	gameCount = -1
	checkEnd = False

	# MAIN LOOP
	while checkEnd == False:
		gameCount += 1
		# GAME COUNT  - 0 to 8 like list
		if gameCount > 8:
			break
		display_Tic_Tac_Toe(mylist)
		move = getPlayersInput(gameCount, names, mylist)
		mylist[move] = names[gameCount % 2][1]
		checkEnd = checkWinGame(mylist, gameCount)
		
		
	display_Tic_Tac_Toe(mylist)	

	if(gameCount > 8):
		print('Draw!!')
	else:	
		print('Congratulatios {} the {} won!!'.format(names[gameCount % 2][0], names[gameCount % 2][1]))

	# ANOTHERGAME, CHANGENAME 
	ang, cgn  = checkAnotherGame()

	if ang == False:
		break

	getNames = cgn 
# END 







