#from board import Board
from player import Player
class Game:
   def __init__(self,players,board):
      self.turn=0
      self.players=player
      self.board=board
   def play_game(self):
      print("Welcome to connect four!")
      

if __name__=="__main__":
   player1=Player()
   player2=Player()
   game=Game([player1,player2],board)
   pass