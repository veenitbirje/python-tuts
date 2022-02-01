'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
#--------------------------------tic tac toe game------------------------------------------------------------

def display(board):
    print('\n'*100)
    print(board[0]+ '  |  ' +board[1]+ '  |  ' +board[2])
    print('--------------')
    print(board[3]+ '  |  ' +board[4]+ '  |  ' +board[5])
    print('--------------')
    print(board[6]+ '  |  ' +board[7]+ '  |  ' +board[8])
#test_board=['x','x','x','x','o','x','x','o','x',]
#print(display(test_board))
def player_marker():
    #OUTPUT =(playe)
    
    marker=''   
    while marker!='X'and marker!='O':
         marker= input('player1: choose marker x or O = ').upper()
    if marker=='X':
        return ('O','X')
    else :
        return ('X','O')
#player_marker2, player_marker1=player_marker()
#print(player_marker2)
def place_marker(board,marker,position):
    board[position]=marker 
#print(test_board)
#place_marker(test_board,'$',2)
#print(test_board)
def win_check(board,marker):
    return ((board[0]==marker and board[1]==marker and board[2]==marker)or
    (board[3]==marker and board[4]==marker and board[5]==marker)or
    (board[6]==marker and board[7]==marker and board[8]==marker)or
    (board[0]==marker and board[3]==marker and board[6]==marker)or
    (board[1]==marker and board[4]==marker and board[7]==marker)or
    (board[2]==marker and board[5]==marker and board[8]==marker)or
    (board[0]==marker and board[4]==marker and board[8]==marker)or
    (board[2]==marker and board[4]==marker and board[6]==marker))
#U=win_check(test_board,'x')
#print(U)
#print(display(test_board))
import random
def choose_first():
    flip=random.randint(0,1)
    if flip==1:
        return 'player 1'
    else:
        return 'player 2'
#x=choose_first()
#print(x)
def space_check(board,position):
    return board[position]==''
def full_board_check(board):
    for i in range(0,10):
        if space_check(board,i):
            return False
    return True
def player_choice(board):
    position= 11
    while position not in [0,1,2,3,4,5,6,7,8] or not space_check(board,position):
        position =int(input('choose digit for 0 to 8 ='))
        
    return position
def replay():
    choice=input('do you want to play again? yes or no =')
    if choice=='yes'or choice=='YES':
        return True
    else:
        return False
#x=replay()
#print(x)
print('welcome to tic tac toe game')
while True:
    the_board=['']*10
    player1,player2=player_marker()
    turn = choose_first()
    print(turn +' your turn')
    game_on=input('do u wanna paly game? y or n')
    if game_on=='y':
        game_on =True
    else:
        game_on=False
    while game_on:
        if turn=='player1':
            display(the_board)
            choice =player_choice(the_board)
            place_marker(the_board,player1,choice)
            if  win_check(the_board,player1):
                display(the_board)
                print('the winner is player1')
                game_on=False
            else:
                if full_board_check(the_board):
                    display(the_board)
                    print('the game is tie')
                    break
                else:
                    turn='player2'
    
        else:
            display(the_board)
            choice =player_choice(the_board)
            place_marker(the_board,player2,choice)
            if  win_check(the_board,player2):
                display(the_board)
                print('the winner is player2')
                game_on=False
            else:
                if full_board_check(the_board):
                    display(the_board)
                    print('the game is tie')
                    break
                else:
                    turn='player1'
            
    
    
    if not replay():
       break
    
    
    





