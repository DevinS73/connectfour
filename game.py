from board import Board
from player import Player
from connect_four_ai import ConnectFourAI
class Game:
   def __init__(self):
      self.turn=0
      self.players=[]
      self.board=Board(7,6)
   def play_game(self):
      '''Plays the game.'''
      print('Welcome to Connect Four!')
      while True:
          try:
              print('Would you like to play (s)ingle player or (d)ouble player')
              choice=input('> ')
              if choice.lower()=='s':
                  self.players.append(ConnectFourAI(2,'o','x'))
                  break
              if choice.lower()=='d':
                  self.players.append(Player('o'))
                  break
          except Exception as e:
              print('Invalid input: Please try again')
      self.players.append(Player('x'))
      while True:
        self.board.disp_board()
        try:
              if choice.lower=='s':
                  if self.players[self.turn].piece=='x':
                      self.board.add_piece(self.players[self.turn].get_choice(self.board),self.players[self.turn].piece)
              else:
                  self.board.add_piece(self.players[self.turn].get_choice(self.board),self.players[self.turn].piece)
              if self.board.check_win()==True:
                  print()
                  print(f'Congratualations, {self.players[self.turn].name.title()}, you win!')
                  self.board.disp_board()
                  self.board.empty_board()
                  return
              if self.board.is_full()==True:
                  print()
                  print("The board is full, it's a draw.")
                  self.board.disp_board()
                  self.board.empty_board()
                  return
              self.turn=(self.turn+1)%2
              print()
        except Exception as e:
              print()
              print(f'Error: {e}')

if __name__=="__main__":
   game=Game()
   game.play_game()