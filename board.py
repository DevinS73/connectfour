

class Board():
    def __init__(self,w,h):
        self.width = w
        self.height = h
        self.board = [[' ']*w for i in range(h)]
    
    def add_piece(self,column,piece):
        '''places piece in the specified column'''
        
        if column < 1 or column > self.width:
            raise ValueError("Invalid Column")
        
        for i in range(self.height-1, -1, -1):            
            if self.board[i][column-1] == ' ':
                self.board[i][column-1] = piece
                break
        else:
            raise ValueError("Column Full")
    
    def empty_board(self):
        '''resets the board to an empty slate'''
        
        self.board = [[' ']*self.width for i in range(self.height)]
    
    def check_win(self):
        '''determines if there is a winner, returns True or False'''
        
        c = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 'x':
                    c += 1
                else:
                    c = 0
                if c >= 4:
                    return True
            c = 0            
        c = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 'o':
                    c += 1
                else:
                    c = 0
                if c >= 4:
                    return True
            c = 0            
        c = 0
        for i in range(self.width):
            for j in range(self.height):
                if self.board[j][i] == 'x':
                    c += 1
                else:
                    c = 0
                if c >= 4:
                    return True
            c = 0        
        c = 0
        for i in range(self.width):
            for j in range(self.height):
                if self.board[j][i] == 'o':
                    c += 1
                else:
                    c = 0
                if c >= 4:
                    return True
            c = 0            
        c = 0
        for i in range(self.height-3):
            for j in range(self.width-3):
                c = 0
                for k in range(4):
                    if self.board[i+k][j+k] == 'x':
                        c += 1
                    else:
                        c = 0
                    if c >= 4:
                        return True                            
        c = 0
        for i in range(self.height-3):
            for j in range(self.width-3):
                c = 0
                for k in range(4):
                    if self.board[i+k][j+k] == 'o':
                        c += 1
                    else:
                        c = 0
                    if c >= 4:
                        return True                            
        c = 0
        for i in range(self.height-1,self.height-3,-1):
            for j in range(self.width-3):
                c = 0
                for k in range(4):
                    if self.board[i-k][j+k] == 'x':
                        c += 1
                    else:
                        c = 0
                    if c >= 4:
                        return True                
        c = 0
        for i in range(self.height-1,self.height-3,-1):
            for j in range(self.width-3):
                c = 0
                for k in range(4):
                    if self.board[i-k][j+k] == 'o':
                        c += 1
                    else:
                        c = 0
                    if c >= 4:
                        return True
        
        return False
    
    def is_full(self):
        '''checks if board is full, returns True or False'''
        
        for row in self.board:
            for ele in row:
                if ele == ' ':
                    return False
        return True
    
    def disp_board(self):
        '''displays the board with the column numbers underneath'''
        
        for i in range(self.width*2):
            print('-',end='')
        print()
        for row in self.board:
            for ele in row:
                print(ele,end=' ')
            print()        
        for i in range(self.width*2):
            print('-',end='')
        print()
        for i in range(self.width):
            print(i+1,end=' ')


if __name__ == "__main__":
    new_board = Board(7,6)
    for j in range(6):
        for i in range(7):
            new_board.add_piece(i+1,'x')
    new_board.disp_board()
    print(new_board.is_full())
