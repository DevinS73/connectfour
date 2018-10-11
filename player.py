class Player:
    def __init__(self):
        self.name=self.get_name()
        self.piece=piece
    def get_name(self):
        name=input("Enter the player's name: ")
        return name
    def get_choice(self,board):
        print("What column would you like to place your piece in?")
        choice=input('> ')
        return choice