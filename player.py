class Player:
    def __init__(self,piece):
        self.piece=piece
        self.name=self.get_name()
    def get_name(self):
        '''Asks the player for their name and returns their input'''
        name=input(f"Enter the name for {self.piece}'s: ")
        return name
    def get_choice(self,board):
        '''Asks the player to choose a column between 1 and the width of
        board to place their piece in. If their choice is not a number
        or out of range, an error is returned.'''
        print()
        print(f"{self.name.title()}, choose a column number between 1 and {board.width}")
        while True:
            try:
                choice=int(input('> '))
                if board.width>=choice>=1:
                    return choice
                else:
                    raise ValueError
            except Exception as e:
                print('Invalid input: Please try again')