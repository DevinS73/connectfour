from board import Board
from player import Player
class Game:
   def __init__(self,board):
      self.turn=0
      self.players=[]
      self.players.append(Player('X'))
      self.players.append(Player('O'))
      self.board=board
   def play_game(self):
      print("Welcome to connect four!")
      turn=0
      while self.board.check_win()==False or self.board.is_full()==False:
        self.board.disp_board()
        self.players[turn].get_choice()
        try:
              self.board.place_piece(self.players[turn].piece,self.players[turn].get_choice())
              if self.board.check_win()==True:
                  print(f'Congratualations, {self.players[turn].name}, you win!')
                  self.board.empty_board()
                  self.board.disp_board()
                  return
              if self.board.is_full()==True:
                  print("The board is full, it's a draw.")
                  self.board.empty_board()
                  self.board.disp_board()
                  return
              turn=(turn+1)%2
        except Exception as e:
              print(f'Error: {e}')

if __name__=="__main__":
   game=Game(Board(7,6))
   game.play_game()