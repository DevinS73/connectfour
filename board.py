
class Board():
    def __init__(self,w,h):
        self.width = w
        self.height = h
        self.board = [[' ']*w for i in range(h)]
    
#    def place_piece(self,piece,column):
#        pass
#        for i in range(self.width):
#            for ele in row:
#                if ele == 0
#        self.board[][column]
#    
    def empty_board(self):
        self.board = [[' ']*w for i in range(h)]
    
    def check_win(self):
        pass
        #return bool
    
    def is_fool(self):
        pass
        #return bool
    
    def disp_board(self):
        for row in self.board:
            for ele in row:
                print(ele,end='|')
            print()
        
        for i in range(self.width):
            print(i+1,end=' ')


if __name__ == "__main__":
    b = Board(6,6)
    b.disp_board()