#random player that will choose a winning position if available
#and block player from winning

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
                    print("%s wins!" % letter)
                    exit(0)
    #Checks verticals
    for x in range(0, 3):
            if board[0 + x] == board[3 + x] == board[6 + x]== letter:
                    print("%s wins!" % letter)
                    exit(0)
    #Checks diagonals
    if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]== letter:
            print("%s wins!" % letter)
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

#------------smart computer moves ----------

def getBoardCopy(board):  # Make a duplicate of the board.
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def checkWin(dupeboard,letter):

    return ((dupeboard[0] == letter and dupeboard[1] == letter and dupeboard[2] == letter) or  
            (dupeboard[3] == letter and dupeboard[4] == letter and dupeboard[5] == letter) or  
            (dupeboard[6] == letter and dupeboard[7] == letter and dupeboard[8] == letter) or  
            (dupeboard[0] == letter and dupeboard[3] == letter and dupeboard[6] == letter) or  
            (dupeboard[1] == letter and dupeboard[4] == letter and dupeboard[7] == letter) or  
            (dupeboard[2] == letter and dupeboard[5] == letter and dupeboard[8] == letter) or  
            (dupeboard[0] == letter and dupeboard[4] == letter and dupeboard[8] == letter) or  
            (dupeboard[2] == letter and dupeboard[4] == letter and dupeboard[6] == letter))  

def testwinningmove(b, letter , nextposition):
    # b = dupe board
    # nextposition = the square to check if makes a win 
    bCopy = getBoardCopy(b)
    bCopy[nextposition] = letter
    return checkWin(bCopy, letter)

def computernextmove(dupeboard):
    availablemoves = empty_spots(board)
    for i in range(0, 9):  #wins if a nest spot winning is available
        if i in availablemoves and testwinningmove(dupeboard, "X", i):
            return i
    for i in range(0, 9): #blocks player from winning 
        if i in availablemoves and testwinningmove(dupeboard, "O", i):
            return i
    #plays a random game
    i = random.choice(availablemoves)
    return i


def computer_move():
    availablemoves = empty_spots(board)
    #print(availablemoves)
    playing = computer
    if full_board(board):
        evaluate(playing)
    cmove = computernextmove(board)
    move(cmove,playing,board)
    evaluate(playing)
    player()



#------------------------------------------
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
    

#references: mblogscode 
    
    

        
        
    

