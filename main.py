board = [['.','.','.'],['.','.','.'],['.','.','.']]
player = 1
moves = 0
def display(board):
    #Display the board
    for row in board:
        for el in row:
            print(el, end="   ")
        print("\n")

def current_player(player):
    #Display current player's turn
    print(f"Player {player}'s turn")

def outp(player):
    #Auxillary function for the update_board func to see which letter is put in that position based on whose turn is it
    if player == 1:
        return 'X'
    return 'O'

def update_board(n, board, player, moves):
    #Update the board with the selected coords
    board[int(n[0])][int(n[1])] = outp(player)
    moves+=1
    return board, moves

def commence_turn(board, player):
    #Ask for position input and validate it by checking if it is valid coords and it's not occupied
    while True:
        n = input("Enter the position: ")
        try: 
            z = int(n)
            if z <= 22 and len(n) == 2:
                if board[int(n[0])][int(n[1])] != '.':
                    print("Area occupied")
                    continue
                else: break
        except: continue 
    return n

def checkCondition(board):
    #vertical check
    for i in range(len(board)):
        if '.' not in [board[0][i], board[1][i], board[2][i]]:
            if (board[0][i] == board[1][i]) and (board[0][i] == board[2][i]):
                return True
    #horizontal check
    for i in range(len(board)):
        if '.' not in [board[i][0], board[i][1], board[i][2]]:
            if (board[i][0] == board[i][1]) and (board[i][0] == board[i][2]):
                return True
    #left to right diagonal check
    if '.' not in [board[0][0], board[1][1], board[2][2]]:
        if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]):
            return True
    #right to left diagonal check
    if '.' not in [board[2][0], board[1][1], board[0][2]]:
        if (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]):
            return True
    return False

def checkWin(player):
    #Declare winner
    print(f"Player {player} wins!")
    quit()

def switch(player):
    #Switch the players' turns
    if player == 1: player = 2
    else: player = 1
    return player

def tie_check(board, moves):
    #If the max number of moves is not reached yet, this means that there are still empty slots in the grid
    if moves != 9: return
    display(board)
    print("Game has ended in a Tie!")
    quit()


while True:
    current_player(player)
    display(board)
    board, moves = update_board(commence_turn(board, player), board, player, moves)
    if checkCondition(board):
        display(board)
        checkWin(player)
    tie_check(board, moves)
    player = switch(player)

    