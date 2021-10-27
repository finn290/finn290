#[y cordinate,x coridinate]
import random
direc = ['l','r','u','d']
def movecheck(loc,moves,user):
    move_legal = False
    while move_legal == False:
        direction = 'a'
        while not (direction == 'l' or direction == 'r' or direction == 'u' or direction == 'd'):
                    if user == 'p':
                        direction = input('What direction are you going? enter L,R,U or D ')
                    elif user == 'c':
                        direction = random.choice(direc)
                    else:
                        print('error with validating user')
                        direction = random.choice(direc)
                    if direction == 'l':
                        if loc[1] - moves >= 0:
                            move_legal = True
                            loc[1] = loc[1] - moves

                    if direction == 'u':
                        if loc[0] - moves >= 0:
                            move_legal = True
                            loc[0] = loc[0] - moves

                    if direction == 'd':
                        if loc[0] + moves <= boardsize - 1:
                            move_legal = True
                            loc[0] = loc[0] + moves

                    if direction == 'r':
                        if (loc[1] + moves) <= boardsize - 1:
                            move_legal = True
                            loc[1] = loc[1] + moves

def cpu(loc):
    moves = random.randint(1,3)
    movecheck(loc,moves,'c')
    if board[bloc[0]][bloc[1]] == 'a':
        return('b')
        print('the computer won')
    else:
        board[bloc[0]][bloc[1]] = 'b'
        display()
        return('f')
    
def amove(aloc):
    
    moves = random.randint(1,3)
    print('player a, you are moving',moves,'spaces')
    movecheck(aloc,moves,'p')
        
    if board[aloc[0]][aloc[1]] == 'b':
        return('a')
    else:
        board[aloc[0]][aloc[1]] = 'a'
        display()
        return('f')

    board[aloc[0]][aloc[1]] = 'a'
def bmove(bloc):
    
    moves = random.randint(1,3)
    print('player b, you are moving',moves,'spaces')
    movecheck(bloc,moves,'p')
    if board[bloc[0]][bloc[1]] == 'a':
        return('b')
        print('player b won')
    else:
        board[bloc[0]][bloc[1]] = 'b'
        display()
        return('f')
    
def display():
    for a in range(len(board)):
        print(board[a])
    print(' ')
def check(loc,player):
    if loc in traps:
        return(player)
        if player == 'b':
            print('player a fell in a trap')
        elif player == 'a':
            print('player b was trapped')
        return(player)
    else:
        return('f')
        
        
boardsize = 8
board = []

for y in range(boardsize):
    board.append([])
    for x in range(boardsize):
        board[y].append('o')
board[0][0] = 'a'
board[boardsize - 1][boardsize - 1] = 'b'

aloc = [0,0]
bloc = [boardsize - 1,boardsize - 1]
board[bloc[0]][bloc[1]] = 'o'
game_over = 'f'
trap = True
blocks = False
want2play = True
mode = '?'
while want2play == True:
    while not (mode == 's' or mode == 'm'):
        mode = input('what mode do you want to play? single player(s),multiplayer(m) or edit game seetings(e)')
        if mode == 'e':
            print('at the moment trap squares are', trap , 'and block squares are' , blocks)
            change = input('enter t to change trap settings or press s to change square setting (still in development) or enter both to change both')
            if 't' in change:
                trap = not trap
            if 'b' in change:
                blocks = not blocks
        if trap == True:
            traps = [[random.randint(1,boardsize-1),random.randint(1,boardsize-1)],[random.randint(1,boardsize),random.randint(1,boardsize-1)],[random.randint(1,boardsize-1),random.randint(1,boardsize-1)],[random.randint(1,boardsize-1),random.randint(1,boardsize-1)]]
            print('trap locations generated')
        if mode == 'm':    
            while game_over == 'f':
                board[bloc[0]][bloc[1]] = 'o'
                game_over = bmove(bloc)
                game_over = check(bloc,'a')
                if not(game_over == 'b' or game_over == 'a'):
                    board[aloc[0]][aloc[1]] = 'o'
                    game_over= amove(aloc)
                    game_over = check(aloc,'b')
            print('player', game_over, 'won')
                    
        if mode == 's':
            while game_over == 'f':
                board[bloc[0]][bloc[1]] = 'o'
                game_over = cpu(bloc)
                game_over = check(bloc,'a')
                if not(game_over == 'b' or game_over == 'a'):
                    board[aloc[0]][aloc[1]] = 'o'
                    game_over= amove(aloc)
                    game_over = check(aloc,'b')
            print('player', game_over, 'won')



    
    
