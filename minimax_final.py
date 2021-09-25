import random

class TicTacToeWMinimax:

    def __init__(self):
        """Initialize with empty board"""
        self.board =    ["-", "-", "-",
                         "-", "-", "-",
                         "-", "-", "-"]
    def print_board(self):
        print("\n")
        print(" " +self.board[0] + " | " + self.board[1] + " | " + self.board[2] )
        print(" " +self.board[3] + " | " + self.board[4] + " | " + self.board[5] )
        print(" " +self.board[6] + " | " + self.board[7] + " | " + self.board[8] )
        print("\n")


    def full_board(self):
        empty = self.empty_spots()
        if not empty:
            return True
        return False
    
    def evaluate(self):
        winner = None
        # horizontal
        hor = [0,3,6]
        for  i in hor:
            if self.board[i] == self.board[i+1] == self.board[i+2] == "X":
              winner = "X"
              print( "%s Wins!" % winner)
              exit(0)
            if self.board[i] == self.board[i+1] == self.board[i+2] == "O":
              winner = "O"
              print( "%s Wins!" % winner)
              exit(0)
              
      #Vertical
        vert = [0,1,2]
        for i in vert:
            if self.board[i] == self.board[i+3] == self.board[i+6]=="X":
              winner = "X"
              print( "%s Wins!" % winner)
              exit(0)
            if self.board[i] == self.board[i+3] == self.board[i+6]=="O":
              winner = "O"
              print( "%s Wins!" % winner)
              exit(0)
              
      #Diagonal
        if self.board[0] == self.board[4] == self.board[8]=="X":
            winner = "X"
            print( "%s Wins!" % winner)
            exit(0)
        if self.board[0] == self.board[4] == self.board[8]=="O":
            winner = "O"
            print( "%s Wins!" % winner)
            exit(0)
            
        if self.board[2] == self.board[4] == self.board[6] == "X":
            winner = "X"
            print( "%s Wins!" % winner)
            exit(0)
        if self.board[2] == self.board[4] == self.board[6] == "O":
            winner = "O"
            print( "%s Wins!" % winner)
            exit(0)
        
        if winner == None and self.full_board():
            print( "Tie")
            exit(0)

    def makemove(self, move,player):
        self.board[move] = player

    def checkwin(self):
        winner = None
      # horizontal
        hor = [0,3,6]
        for  i in hor:
            if self.board[i] == self.board[i+1] == self.board[i+2] == "X":
              winner = "X"
              return winner
            if self.board[i] == self.board[i+1] == self.board[i+2] == "O":
              winner = "O"
              return winner
              
      #Vertical
        vert = [0,1,2]
        for i in vert:
            if self.board[i] == self.board[i+3] == self.board[i+6]=="X":
              winner = "X"
              return winner
            if self.board[i] == self.board[i+3] == self.board[i+6]=="O":
              winner = "O"
              return winner
              
      #Diagonal
        if self.board[0] == self.board[4] == self.board[8]=="X":
            winner = "X"
            return winner
        if self.board[0] == self.board[4] == self.board[8]=="O":
            winner = "O"
            return winner
            
        if self.board[2] == self.board[4] == self.board[6] == "X":
            winner = "X"
            return winner
        if self.board[2] == self.board[4] == self.board[6] == "O":
            winner = "O"
            return winner
        
        if winner == None and self.full_board():
            winner = "Tie"
            return winner
        
    def gameover(self):
        if self.checkwin() != None:
            return True
        for i in self.board:
            if i == "-":
                return False
        return True
    def empty_spots(self):
        empty = []
        for i in range(0,9):
            if self.board[i]=="-":
                empty.append(i)
        return empty

    def minimax(self,board,depth,player):
        winning = board.checkwin()
        available = board.empty_spots()
        if depth == 0 or board.gameover():
            if winning == "X":
                return -1
            elif winning == "O":
                return 1
            else:
                return 0

        if player == "O":
            bestval = -1
            for i in available:
                board.makemove(i, player)
                value = self.minimax(board, depth-1, changeplayer(player))
                board.makemove(i, "-")
                bestval = max(bestval,value)
            return bestval

        if player == "X":
            bestval = 1
            for i in available:
                board.makemove(i, player)
                value = self.minimax(board, depth+1, changeplayer(player))
                board.makemove(i, "-")
                bestval = min(bestval,value)
            return bestval

def changeplayer(player):
    if player == "X":
        return "O"
    else:
        return "X"

def computernextmove(board,depth,player):
    available = board.empty_spots()
    middle = 0
    choices = []
    for i in available:
        board.makemove(i,"O")
        value = board.minimax(board,depth +1, changeplayer(player))
        board.makemove(i,"-")
        if value> middle:
            choices = [i]
            break
        elif value == middle:
            choices.append(i)
 
    if len(choices) > 0:
        x = random.choice(choices)
        return x
    else:
        r = random.choice(available)
        return r


if __name__ == '__main__':

    g = TicTacToeWMinimax()
    g.print_board()
    print('Player is X and computer is O')
    print("Player will play first.")
    while g.gameover() != True :
        print("Choose an empty spot from 1 to 9")
        x = input()
        themove = int(x) -1
        while themove not in g.empty_spots():
            print("Invalid.Choose an empty spot from 1 to 9")
            x = input()
            themove = int(x) -1
        mymove = int(x)
        pmove = mymove - 1
        g.makemove(pmove, "X")
        g.print_board()
        g.evaluate()

        computermove = computernextmove(g,0,"O")
        g.makemove(computermove,"O")
        g.print_board()
        g.evaluate()

#references
        #https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/
        
    



            
                
                
            


    


        
        


    
