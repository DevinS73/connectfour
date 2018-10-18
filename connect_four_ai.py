import copy
from random import randint
import board

class ConnectFourAI:
    def __init__(self,difficulty,piece,opp_piece):
        self.difficulty = difficulty
        self.opp_piece = opp_piece
        self.name = "CPU"
        self.piece = piece
        
        
    def find_move(self,board):
        if self.difficulty == 1: # easy
            return randint(1,board.width)
        
        elif self.difficulty == 2: # medium
            return self.find(board)
        
    
    def find(self,board):
            points = [0]*board.width
            points[board.width//2] = 4 # center column starts with 4
            for i in range(board.width):
                try:
                    temp_board = copy.deepcopy(board)
                    temp_board.add_piece(i+1,self.piece)
                    
                    #points2 = [0] * board.width
                    #points2[board.width//2] = 4
                    #for j in range(board.width):
                    #    try:
                    #        temp_board2 = copy.deepcopy(temp_board)
                    #        temp_board2.add_piece(j+1,self.opp_piece)
                    #        points2[j] += self.get_points(temp_board2)
                    #
                    #    except:
                    #        points2[j] = 1000000
                    #print(points2)
                    #points[i] = min(points2)
                    points[i] += self.get_points(temp_board)
                except Exception as e:
                    print(e)
                    points[i] = -10000000
            #print(points)
            
            # if the average == max...beginning of game is the only time this can happen
            if sum(points)//len(points) == max(points):
                return board.width//2 + 1
            
            
            return points.index(max(points))+1
        
        
    
    
    
    def get_points(self, board):
        points = 0
        
        # find lines of 2 
        points += self.find_lines(board,2,self.piece) * 2 # 2 points each
        
        # find lines of 3
        points += self.find_lines(board,3,self.piece) * 5 # 5 points each
        
        # find winners
        points += self.find_lines(board,4,self.piece) * 1000
        
        # find opponent lines of 2
        points -= self.find_lines(board,2,self.opp_piece) * 2
        
        # find opponent lines of 3
        points -= self.find_lines(board,3,self.opp_piece) * 100
        
        points -= self.find_double_ends(board,self.opp_piece) * 100
              
        
        return points
        
    def find_double_ends(self,board,piece):
        b = board.board
        for c in range(len(b[0])-3):
            row = [b[len(b)-1][c],b[len(b)-1][c+1],b[len(b)-1][c+2],b[len(b)-1][c+3]]
            if row[0] == ' ' and row[3] == ' ' and row[1]==row[2]==piece:
                return 1
        
        for r in range(len(b)-1):
            for c in range(len(b[0])-3):
                row = [b[r][c],b[r][c+1],b[r][c+2],b[r][c+3]]
                next_row = [b[r+1][c],b[r+1][c+1],b[r+1][c+2],b[r+1][c+3]]
                if next_row.count(' ') == 0:
                    if row[0] == ' ' and row[3] == ' ' and row[1]==row[2]==piece:
                        return 1
        return 0
    
    def find_lines(self,board,num,piece):
        count = 0
        
        b = board.board
        
        #horizontal
        for r in range(len(b)):
            for c in range(len(b[r])-3):
                row = [b[r][c],b[r][c+1],b[r][c+2],b[r][c+3]]
                if row.count(piece) == num and row.count(' ') == 4-num:
                    count += 1
 
        #vertical      
        for r in range(len(b)-3):
            for c in range(len(b[r])):
                col = [b[r][c],b[r+1][c],b[r+2][c],b[r+3][c]]
                if col.count(piece) == num and col.count(' ') == 4-num:
                    count += 1
        #major diagonal      
        for r in range(len(b)-3):
            for c in range(len(b[r])-3):
                diag = [b[r][c],b[r+1][c+1],b[r+2][c+2],b[r+3][c+3]]
                if diag.count(piece) == num and diag.count(' ') == 4-num:
                    if r+4 < len(b):
                        next_diag = [b[r+1][c],b[r+2][c+1],b[r+3][c+2],b[r+4][c+3]]
                    else:
                        next_diag = [b[r+1][c],b[r+2][c+1],b[r+3][c+2]]
                    if ' ' not in next_diag:
                        count += 1
                        #print('major diagonal',r,c)
        
        #minor diagonal
        for r in range(3,len(b)):
            for c in range(len(b[r])-3):
                diag = [b[r][c],b[r-1][c+1],b[r-2][c+2],b[r-3][c+3]]
                if diag.count(piece) == num and diag.count(' ') == 4-num:
                    if r < len(b)-1:
                        next_diag = [b[r+1][c],b[r][c+1],b[r-1][c+2],b[r-2][c+3]]
                    else:
                        next_diag = [b[r][c+1],b[r-1][c+2],b[r-2][c+3]]
                    if ' ' not in next_diag:
                        count += 1
                        #print('minor diagonal',r,c)
                    
        return count
    
            
    
    
    def get_choice(self,board):
        ''' returns the column # with the best move
            option
        '''
        curr_board = copy.deepcopy(board)
        col = self.find_move(curr_board)
        return col
        #print(col)
        #board.add_piece(col,self.piece) 
    
    
if __name__ == "__main__":
    
    test = board.Board(7,6)
    
    test.board[4][0] = "C"
    test.board[5][0] = "C"
    test.board[5][1] = "C"
    test.board[5][3] = "C"
    test.disp_board()
    
    ai = ConnectFourAI(2,'C','x')
    print(ai.find_move(test))