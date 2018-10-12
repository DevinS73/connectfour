class Player:
    def __init__(self,piece):
        self.name=self.get_name()
        self.piece=piece
    def get_name(self):
        name=input("Enter the player's name: ")
        return name
    def get_choice(self,board):
        print(f"Choose a column number between 0 and {board.width}")
        choice=input('> ')
        return choice