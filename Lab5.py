import random

#Alunos:
#Caique de Paula Figueiredo Coelho
#Lucas Queiroz

def ObtenerCopiaTablero(board):
    	#Faz uma copia do quadro e retrona esta copia

	dupeBoard = []

	for i in board:
		dupeBoard.append(i)

	return dupeBoard

def drawBoard(board):

	#Esta funcao imprime o quadro do jogo
	#O quadro eh uma lista de 9 strings representando o qaudro
	copyBoard = ObtenerCopiaTablero(board)

	for i in range(1,26):
		if(board[i] == ''):
			copyBoard[i] = str(i)
		else:
			copyBoard[i] = board[i]
	
	print(' ' + copyBoard[21] + '|' + copyBoard[22] + '|' + copyBoard[23] + '|' + copyBoard[24] + '|' + copyBoard[25])

	print('---------------')

	print(' ' + copyBoard[16] + '|' + copyBoard[17] + '|' + copyBoard[18] + '|' + copyBoard[19] + '|' + copyBoard[20])

	print('---------------')

	print(' ' + copyBoard[11] + '|' + copyBoard[12] + '|' + copyBoard[13] + '|' + copyBoard[14] + '|' + copyBoard[15])

	print('---------------')

	print(' '+ copyBoard[6] + ' |' + copyBoard[7] + ' |' + copyBoard[8] + ' |' + copyBoard[9] + ' |' + copyBoard[10])

	print('---------------')

	print(' '+ copyBoard[1] + ' |' + copyBoard[2] + ' |' + copyBoard[3] + ' |' + copyBoard[4] + ' |' + copyBoard[5])

	print('---------------')

    

def inputPlayerLetter():
	#El jugador elige qué letra quiere jugar "X" u "O"
	#Devuelve una lista con la letra del jugador y la letra de la computadora
	letter = ''
	while not(letter == 'X' or letter == 'O'):
		print('¿Quieres ser X u O?')
		letter = input().upper()
		if(letter != 'X' and letter != 'O'):
			print("¡Solo ingresa la letra X(xis) si quieres ser X o la letra O (oh) si quieres ser O!")

	#El primer elemento de la lista es el del jugador y el segundo es el de la computadora.
	if letter == 'X':
		return ['X','O']
	else:
		return ['O','X']
    
def whoGoesFirts():
	#Elige al azar al jugador que jugará primero
	if random.randint(0, 1) == 0:
		return 'computador'
	else:
		return 'Jugador'

def makeMove(board, letter, move):
	#Hace el movimiento de la computadora o del jugador dependiendo de la letra en el tablero
	board[move] = letter

def isWinner(brd, let):
	#Dado un marco y una letra, esta función devuelve True si la letra dada gana el juego.
	return((brd[1] == let and brd[2] == let and brd[3] == let and brd[4] == let) or #línea superior
		(brd[2] == let and brd[3] == let and brd[4] == let and brd[5] == let) or #línea media
		(brd[6] == let and brd[7] == let and brd[8] == let and brd[9] == let) or #línea de fondo - arriba
		(brd[7] == let and brd[8] == let and brd[9] == let and brd[10] == let) or #columna izquierda
		(brd[11] == let and brd[12] == let and brd[13] == let and brd[14] == let) or #columna medio
		(brd[12] == let and brd[13] == let and brd[14] == let and brd[15] == let) or #columna derecho
		(brd[16] == let and brd[17] == let and brd[18] == let and brd[19] == let) or #diagonal principal
        (brd[17] == let and brd[18] == let and brd[19] == let and brd[20] == let) or
        (brd[21] == let and brd[22] == let and brd[23] == let and brd[24] == let) or
        (brd[22] == let and brd[23] == let and brd[24] == let and brd[25] == let) or
        (brd[16] == let and brd[11] == let and brd[6] == let and brd[1] == let) or
        (brd[21] == let and brd[16] == let and brd[11] == let and brd[6] == let) or
        (brd[17] == let and brd[12] == let and brd[7] == let and brd[2] == let) or
        (brd[22] == let and brd[17] == let and brd[7] == let and brd[2] == let) or
        (brd[23] == let and brd[18] == let and brd[13] == let and brd[8] == let) or
        (brd[18] == let and brd[13] == let and brd[8] == let and brd[3] == let) or
        (brd[19] == let and brd[14] == let and brd[9] == let and brd[4] == let) or
        (brd[20] == let and brd[15] == let and brd[10] == let and brd[5] == let) or
        (brd[24] == let and brd[19] == let and brd[14] == let and brd[9] == let) or
        (brd[25] == let and brd[20] == let and brd[15] == let and brd[10] == let) or
        (brd[21] == let and brd[17] == let and brd[13] == let and brd[9] == let) or
        (brd[17] == let and brd[13] == let and brd[9] == let and brd[5] == let) or
        (brd[1] == let and brd[7] == let and brd[13] == let and brd[19] == let) or
        (brd[7] == let and brd[13] == let and brd[19] == let and brd[25] == let) or
        (brd[16] == let and brd[12] == let and brd[8] == let and brd[4] == let) or
        (brd[22] == let and brd[18] == let and brd[14] == let and brd[10] == let) or
        (brd[6] == let and brd[12] == let and brd[18] == let and brd[24] == let) or
        (brd[2] == let and brd[8] == let and brd[14] == let and brd[20] == let) or
		(brd[2] == let and brd[8] == let and brd[14] == let and brd[20] == let)) #diagonal secundaria

def isSpaceFree(board, move):
	#Devuelve verdadero si el espacio solicitado está libre en el marco
	if(board[move] == ''):
		return True
	else:
		return False

def getPlayerMove(board):
	#Recibe el movimiento del jugador
	move = ''

	while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'.split() or not isSpaceFree(board, int(move)):
		print('¿Cuál es tu próximo movimiento? (1-25)')
		move = input();
		if(move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'):
			print("¡MOVIMIENTO NO VÁLIDO! ¡INTRODUZCA UN NÚMERO ENTRE 1 Y 25!")
		
		if(move in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'):
			if(not isSpaceFree(board, int(move))):
				print("¡LUGAR NO DISPONIBLE! ¡ELIJA OTRO ESPACIO ENTRE EL 1 Y EL 25 QUE ESTÉ DISPONIBLE EN EL TABLERO!")

	return int(move)

def chooseRandomMoveFromList(board, movesList):
	#Retorna um movimento valido aleatorio
	#Devuelve Ninguno si no hay movimientos válidos
    #restringir el 5
	possiveisMovimentos = []
	for i in movesList:
		if isSpaceFree(board, i):
			possiveisMovimentos.append(i)
	if len(possiveisMovimentos) != 0:
		return random.choice(possiveisMovimentos)
	else:
		return None
    

def isBoardFull(board):
	#Devuelve True si todos los espacios de marco no están disponibles
	for i in range(1, 26):
		if isSpaceFree(board, i):
			return False
	return True

def possiveisOpcoes(board):
	#Devuelve una lista de todos los espacios en el marco que están disponibles
	#controlar los 3 ultimos movimientos
	opcoes = []
    #Espacios y posiciones en el tablero del 1 - 25
	for i in range(1, 26):
		if isSpaceFree(board, i):
			opcoes.append(i)
	return opcoes

def finishGame(board, computerLetter):
	#Comprobar si el juego ha llegado al final.
	#Devuelve -1 si el jugador gana
	#Devuelve 1 si la computadora gana
	#Devuelve 0 si el juego termina en empate
	#Devuelve Ninguno si el juego no ha terminado

	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	if(isWinner(board, computerLetter)):
		return 1

	elif(isWinner(board, playerLetter)):
		return -1

	elif(isBoardFull(board)):
		return 0

	else:
		return None


def alphabeta(board, computerLetter, turn, alpha, beta):
	#Aquí hacemos la poda del alfabeto.

	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	if turn == computerLetter:
		nextTurn = playerLetter
	else:
		nextTurn = computerLetter

	finish = finishGame(board, computerLetter)

	if (finish != None):
		return finish

	possiveis = possiveisOpcoes(board)

	if turn == computerLetter:
		for move in possiveis:
			makeMove(board, turn, move)
			val = alphabeta(board, computerLetter, nextTurn, alpha, beta)
			makeMove(board, '', move)
			if val > alpha:
				alpha = val

			if alpha >= beta:
				return alpha
		return alpha

	else:
		for move in possiveis:
			makeMove(board, turn, move)
			val = alphabeta(board, computerLetter, nextTurn, alpha, beta)
			makeMove(board, '', move)
			if val < beta:
				beta = val

			if alpha >= beta:
				return beta
		return beta



def getComputerMove(board, turn, computerLetter):
	#Aquí definimos cuál será el movimiento de la computadora

	a = -3
	opcoes = []

	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'


	#if len(possiveisOpcoes(board)) == 5:
	#	print("no se pude usar");

	#Aquí empezamos el MiniMax
	#Primero comprobamos si podemos ganar con el siguiente movimiento
	for i in range(1, 26):
		copy = ObtenerCopiaTablero(board)
		if isSpaceFree(copy, i):
			makeMove(copy, computerLetter, i)
			if isWinner(copy, computerLetter):
				return i

	#Comprueba si el jugador puede ganar en el siguiente movimiento y bloquea
	for i in range(1, 26):
		copy = ObtenerCopiaTablero(board)
		if isSpaceFree(copy, i):
			makeMove(copy, playerLetter, i)
			if isWinner(copy, playerLetter):
				return i

	possiveisOpcoesOn = possiveisOpcoes(board)

	for move in possiveisOpcoesOn:

		makeMove(board, computerLetter, move)
		val = alphabeta(board, computerLetter, playerLetter, 3, 3)		
		makeMove(board, '', move)

		if val > a:
			a = val
			opcoes = [move]

		elif val == a:
			opcoes.append(move)

	return random.choice(opcoes)

print('Juguemos al tres en raya!')

jogar = True

while jogar:
	#restablecer el juego
	theBoard = [''] * 26
	playerLetter, computerLetter = inputPlayerLetter()
	turn = whoGoesFirts()
	print('O ' + turn +' jugar primero,')
	gameisPlaying = True

	while gameisPlaying:
		if turn == 'Jugador':
			#turno del jugador
			drawBoard(theBoard)
			move = getPlayerMove(theBoard)
			makeMove(theBoard, playerLetter, move)

			if isWinner(theBoard, playerLetter):
				drawBoard(theBoard)
				print('Ganaste el juego!')
				gameisPlaying = False
			
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('El juego termino en empate')
					break
				else:
					turn = 'Computador'

		else:
			#tiempo de computadora
			move = getComputerMove(theBoard, playerLetter, computerLetter)
			makeMove(theBoard, computerLetter, move)

			if isWinner(theBoard, computerLetter):
				drawBoard(theBoard)
				print("La computadora ganó :(")
				gameisPlaying = False

			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('El juego termino en empate')
					break
				else:
					turn = 'Jugador'

	letterNew = ''
	while not(letterNew == 'S' or letterNew == 'N'):
		print("¿Quieres jugar de nuevo? Escriba S (Para usted) o N (Para No)")
		letterNew = input().upper()
		if (letterNew != 'S' and letterNew != 'N'):
			print("¡Entrada inválida! ¡Escriba S (A Si) o N (A No)!")
		if(letterNew == 'N'):
			print("¡Fue bueno jugar contigo! ¡Hasta luego")
			jogar = False