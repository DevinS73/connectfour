from board import Board
from player import Player
class Game:
   def __init__(self,players,board):
      self.turn=0
      self.players=players
      self.board=board
   def play_game(self):
      print("Welcome to connect four!")
      turn=0
      while board.check_win()==False and board.is_full()==False:
        players[turn%len(players)].get_choice()
          try:
              board.place_piece(players[turn%len(players)].piece,players[turn%len(players)].get_choice())
              board.disp_board()
              if board.check_win()==True:
                  print(f'Congratualations, {players[turn%len(players)].name}, you win!')
                  board.empty_board()
                  break
              if board.is_full()==True:
                  print("The board is full, it's a draw.")
                  board.empty_board()
                  break
              turn+=1
          except Exception as e:
              print(f'Error: {e}')

if __name__=="__main__":
   print("For player 1 (O's):")
   player1=Player('O')
   print()
   print("For player 2 (X's):")
   player2=Player('X')
   game=Game([player1,player2],Board(7,6))