class Player:
    def __init__(self,piece):
        self.piece=piece
        self.name=self.get_name()
    def get_name(self):
        name=input(f"Enter the name for {self.piece}'s: ")
        return name
    def get_choice(self,board):
        print(f"{self.name}, choose a column number between 1 and {board.width}")
        while True:
            try:
                choice=int(input('> '))
                if board.width>=choice>=1:
                    return choice
                else:
                    raise ValueError
            except Exception as e:
                print('Invalid input: Please try again')