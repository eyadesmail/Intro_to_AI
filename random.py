import random
import sys
 
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

player = "Player"
computer = "Computer"
 

def print_board(board):
    
    print("\n")
    print(" " +board[0] + " | " + board[1] + " | " + board[2] )
    print(" " +board[3] + " | " + board[4] + " | " + board[5] )
    print(" " +board[6] + " | " + board[7] + " | " + board[8] )
    print("\n")
 



def full_board(board):
    empty = empty_spots(board)
    if not empty:
        return True
    return False
    

def empty_spots(board):
    empty = []
    for i in range(0,9):
        if board[i]=="-":
            empty.append(i)
    return empty

def evaluate(who):
    if who == player:
        letter = "O"
    else:
        letter = "X"
    
    #Checks horizontals
    for x in (0, 3, 6):
            if board[0 + x] == board[1 + x] == board[2 + x] == letter:
                    print("%s wins!" % who)
                    exit(0)
    #Checks verticals
    for x in range(0, 3):
            if board[0 + x] == board[3 + x] == board[6 + x]== letter:
                    print("%s wins!" % who)
                    exit(0)
    #Checks diagonals
    if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]== letter:
            print("%s wins!" % who)
            exit(0)
    #Check for tie
    if board.count("X") == 5 or board.count("O") == 5:
            print("tie")
            exit(0)

def move(move,playing,board):
    moves = empty_spots(board)
    if move not in moves:
        return "invalid move"
    else:
        updateboard(board,move,playing)
        
def updateboard(board,move,playing):
    if playing == player:
        letter = "O"
    else:
        letter = "X"
    board[move] = letter
    print_board(board)


def computer_move():
    availablemoves = empty_spots(board)
    print(availablemoves)
    playing = computer
    if full_board(board):
        evaluate(playing)

    #make random move
    cmove = random.choice(availablemoves)
    move(cmove,playing,board)
    evaluate(playing)
    player()
    
def player():
    availablemoves = empty_spots(board)
    print(availablemoves)
    playing = player
    if full_board(board):
        evaluate(playing)
    
    
    
    print("Choose an empty spot from 1 to 9")
    x = input()
    themove = int(x) -1
    
 
    while themove not in availablemoves:
        print("Invalid.Choose an empty spot from 1 to 9")
        x = input()
        themove = int(x) -1
    mymove = int(x)
    pmove = mymove - 1
    move(pmove,playing,board)
    evaluate(playing)
    computer_move()

def game(board):
    print_board(board)
    print('Player is O and computer is X')
    print("Player will play first.")
    player()
    
game(board)
    

    
    
    

        
        
    

