def display_Tic_Tac_Toe(mlist):

	print('  {}  |  {}  |   {}  '.format(mlist[0], mlist [1], mlist[2]))
	print('------------------')
	print('  {}  |  {}  |   {}  '.format(mlist[3], mlist [4], mlist[5]))
	print('------------------')
	print('  {}  |  {}  |   {}  '.format(mlist[6], mlist [7], mlist[8]))


def getPlayersName():
	playerOne = input('Type the name of Player One\n')
	print('Hello {} you will be "X"'.format(playerOne))
	playerTwo =	input('Type the name of Player Two\n')
	print('Hello {} you will be "O"'.format(playerTwo))

	return ([playerOne, 'X'] , [playerTwo, 'O'])


def checkEndGame(mlist, count):
	for n in range(0,3):
		if mlist[3 * n] == mlist[ 3 * n + 1] == mlist[ 3 * n + 2] and mlist[3 * n] != ' ':
			return True
		elif mlist[n] == mlist[ n + 3] == mlist[ n + 6] and mlist[n] != ' ':
			return True
	if (mlist[0] == mlist[4] == mlist[8] and mlist[4] != ' ' ) or (mlist[2] == mlist[4] == mlist[6] and mlist[4] != ' '):
		return True

	return False

def getPlayersInput(gc, names, mlist):
	playInput =  input('{} please make your move!\n'.format(names[gc % 2][0]))
	if mlist[int(playInput) - 1] != ' ':
		print('Sorry but you cannot make this move!')
		return getPlayersInput(gc,names,mlist)
	return (int(playInput) - 1)

def checkAnotherGame():
	anotherGame = input('Start another game? (Y/N) \n')
	if anotherGame.lower() == 'y':
		changeNames = input('With the same names? (Y/N) \n')
		if changeNames.lower() == 'y':
			return (True, False)
		else: 
			return (True, True)

	return (False, False)



print('Welcome to Tic Tac Toe Game')
getNames = True

while True:

	if(getNames):
		names = getPlayersName()
	mylist = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	gameCount = -1
	checkEnd = False



	while checkEnd == False:
		gameCount += 1
		if gameCount > 8:
			break
		display_Tic_Tac_Toe(mylist)
		move = getPlayersInput(gameCount, names, mylist)
		mylist[move] = names[gameCount % 2][1]
		checkEnd = checkEndGame(mylist, gameCount)
		
		
	display_Tic_Tac_Toe(mylist)	

	if(gameCount > 8):
		print('Draw!!')
	else:	
		print('Congratulatios {} the {} won!!'.format(names[gameCount % 2][0], names[gameCount % 2][1]))

	ang, cgn  = checkAnotherGame()

	if ang == False:
		break

	getNames = cgn 









