from board import Board
from player import Player
class Game:
   def __init__(self,board):
      self.turn=0
      self.players=[]
      self.players.append(Player('x'))
      self.players.append(Player('o'))
      self.board=board
   def play_game(self):
      print("Welcome to connect four!")
      turn=0
      while True:
        self.board.disp_board()
        try:
              self.board.add_piece(self.players[turn].get_choice(self.board),self.players[turn].piece)
              if self.board.check_win()==True:
                  print(f'Congratualations, {self.players[turn].name.title()}, you win!')
                  self.board.disp_board()
                  self.board.empty_board()
                  return
              if self.board.is_full()==True:
                  print("The board is full, it's a draw.")
                  self.board.disp_board()
                  self.board.empty_board()
                  return
              turn=(turn+1)%2
        except Exception as e:
              print(f'Error: {e}')

if __name__=="__main__":
   game=Game(Board(7,6))
   game.play_game()