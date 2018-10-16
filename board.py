
class Board():
    def __init__(self,w,h):
        self.width = w
        self.height = h
        self.board = [[' ']*w for i in range(h)]
    
    def add_piece(self,column,piece):
        for i in range(self.height-1, -1, -1):            
            if self.board[i][column-1] == ' ':
                self.board[i][column-1] = piece
                break
        else:
            raise ValueError("column full")
    
    def empty_board(self):
        self.board = [[' ']*self.width for i in range(self.height)]
    
    def check_win(self):
        c = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 'X':
                    c += 1
                else:
                    c = 0
                if c >= 4:
                    return True
            c = 0
            
        c = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 'O':
                    c += 1
                else:
                    c = 0
                if c >= 4:
                    return True
            c = 0
            
        c = 0
        for i in range(self.width):
            for j in range(self.height):
                if self.board[j][i] == 'X':
                    c += 1
                else:
                    c = 0
                if c >= 4:
                    return True
            c = 0
        
        c = 0
        for i in range(self.width):
            for j in range(self.height):
                if self.board[j][i] == 'O':
                    c += 1
                else:
                    c = 0
                if c >= 4:
                    return True
            c = 0
            
        c = 0
        for i in range(self.width):
            if self.board[i][i] == 'X':
                c += 1
            else:
                c = 0
            if c >= 4:
                return True
            
        for i in range(self.width):
            if self.board[self.height-1-i][i] == 'X':
                c += 1
            else:
                c = 0
            if c >= 4:
                return True
            
        return False
    
    def is_full(self):
        for row in self.board:
            for ele in row:
                if ele == ' ':
                    return False
        return True
    
    def disp_board(self):
        for row in self.board:
            for ele in row:
                print(ele,end=' ')
            print()
        
        for i in range(self.width):
            print(i+1,end=' ')


if __name__ == "__main__":
    b = Board(6,7)
    b.add_piece(1,'X')
    b.add_piece(2,'O')
    b.add_piece(2,'X')
    b.add_piece(3,'O')
    b.add_piece(3,'O')
    b.add_piece(3,'X')
    b.add_piece(4,'O')
    b.add_piece(4,'O')
    b.add_piece(4,'O')
    b.add_piece(4,'X')
    b.disp_board()
    print(b.check_win())