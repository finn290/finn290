from time import sleep
import random
#18/9/20
#This is a game where player/s pick up any amount of sticks and the person who
#draws the last stick loses
#this game has 3 main game modes
#>pvp: where both characters are player controlled
#>player vs cpu: where they play against the computer picking the pieces they take randomly
#>player vs terminator: the player plays against an ai that should play with strategy
#Its been a while since I've seen this so its wierd to see how much I've improved
def display():
    print(board[0])
    print(board[1])
    print(board[2])
def remove(row,spaces):
    for x in range(spaces):
        board[row].remove('I')
board = [['I','I','I','I','I','I','I'],['I','I','I','I','I'],['I','I','I']]
def round():
        row = (int(input('player what row are you going to take from? 1, 2 or 3?'))-1)
        while 0 > row or row > 4:
                row = (int(input('player what row are you going to take from? 1, 2 or 3? that has sticks on'))-1)

        spaces = int(input('player how many sticks will you take?'))
        while spaces > len(board[row]) or spaces < 1:
            spaces= int(input('Enter a number less than or equal to the number of sticks left'))
        remove(row,spaces)
        display()
def cpu(board):
    print('''the computer's turn''')
    row = random.randint(0,2)
    rand = len(board[row])
    while rand < 1:
        row = random.randint(0,2)
        rand = len(board[row])
    spaces = random.randint(1,random.randint(0,rand))
    remove(row,spaces)
    print('the computer has randomly taken' , spaces , 'sticks from row' , (row + 1)) 
    display()
def terminator():
    print('''It is the master computer's turn''')
    spaces = 0
    row = 1
    if (len(board[0]) + (len(board[1])) + len((board[2]))) == 15:
        row = 0
        spaces = 6
#one row left
    elif len(board[0]) == 0 and len(board[1]) == 0:
        row = 2
        spaces = (len(board[2]) - 1)
    elif len(board[2]) == 0 and len(board[1]) == 0:
        row = 0
        spaces = (len(board[row]) - 1)
    elif len(board[2]) == 0 and len(board[0]) == 0:
        row = 1
        spaces = (len(board[row])- 1)
#2 rip
    elif (len(board[0]) > 0 and len(board[1]) > 0) and (len(board[0]) == 1 or len(board[1]) == 1):
        if len(board[0]) > len(board[1]):
            row = 0
            spaces = (len(board[row]) ) 
        elif len(board[0]) < len(board[1]):
            row = 1
            spaces = (len(board[row]) )
    elif (len(board[2]) > 0 and len(board[1]) > 0) and (len(board[2]) == 1 or len(board[1]) == 1):
        if len(board[2]) > len(board[1]):
            row = 2
            spaces = (len(board[row]) ) 
        elif len(board[2]) < len(board[1]):
            row = 1
            spaces = (len(board[row])) 
    elif (len(board[0]) > 0 and len(board[2]) > 0) and (len(board[0]) == 1 or len(board[1]) == 1):
        if len(board[0]) > len(board[2]):
            row = 0
            spaces = (len(board[row]) ) 
        elif len(board[0]) < len(board[2]):
            row = 2
            spaces = (len(board[row]) ) 

            
        
        
#2 rows left
    elif (len(board[0]) > 0 and len(board[1]) > 0):
        row = 0
        spaces = len(board[2]) - 1
    elif (len(board[1]) > 0 and len(board[2]) > 0):
        row = 2
        spaces = (len(board[2])) - 1
    elif (len(board[0]) > 0 and len(board[2]) > 0):
        row = 0
        spaces = len(board[2]) - 1
   
            
            
    else:
        row = random.randint(0,2)
        while len(board[row]) < 1:
            row = random.randint(0,2)
        spaces = len(board[2]) - 1

    if spaces < 1:
        spaces = 1
    sleep(0.5)
    display()
    sleep(0.5)
    print('the computer has taken' , spaces , 'sticks from row' , (row + 1)) 
            
    

    remove(row,spaces)
    display()
def hardmode():
    rounds = 0
    while len(board[0]) + len(board[1]) + len(board[2]) > 0:
        terminator()
        rounds = rounds + 1
        if len(board[0]) > 0 or len(board[1]) > 0 or len(board[2]) > 0:
            round()
            rounds = rounds + 1

    if (rounds % 2) == 0:
           print('the computer won expertly')
    else:
           print('you have bested the computer')
        
def pvp():
    roundsa = 0
    while len(board[0]) > 0 or len(board[1]) > 0 or len(board[2]) > 0:
        roundsa = roundsa + 1
        if (roundsa % 2) == 0:
           player = '2'
        else:
           player = '1'
        print('player ' + player + ',your up')
        round()
    if (roundsa % 2) == 0:
        print('Player 1 has won')
    else:
        print('Player 2 has won')
def cvp():
        player = 0
        while len(board[0]) > 0 or len(board[1]) > 0 or len(board[2]) > 0:
            player = player + 1
            cpu(board)
            if len(board[0]) > 0 or len(board[1]) > 0 or len(board[2]) > 0:
                player = player + 1
                round()
        if (player % 2) == 0:
            print('the computer has won')
        else:
            print('player has won')
player = 1

game = input('multiplayer or play against the computer or hard mode(m/c/h)')
if game== 'm':
     pvp()
elif game == 'c':
    (cvp())
elif game == 'h':
    hardmode()
else:
    print('invalid response')
    game = input('multiplayer or play against the computer or hard mode(m/c/h)')
    if game== 'm':
         pvp()
    elif game == 'c':
        (cvp())
    elif game == 'h':
        hardmode()
    else:
        print('invalid response')
    
    
