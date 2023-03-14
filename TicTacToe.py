import os

class Game:
    def __init__(self):
        player1 = input("Enter Player 1's name: ")
        player2 = input("Enter Player 2's name: ")
        self.board = Board()
        self.players = [Player(player1, 'X'), Player(player2, 'O')]
        self.current_player = self.players[0]

    def start(self):
        print('Welcome to Tic Tac Toe!')
        self.board.display()

        while True:
            move = self.current_player.get_move()
            if self.board.make_move(move, self.current_player.symbol):
                os.system('cls')
                self.board.display()

                if self.board.check_win(self.current_player.symbol):
                    print(f'{self.current_player.name} wins!')
                    break
                elif self.board.check_tie():
                    print('It\'s a tie!')
                    break

                self.current_player = self.players[(self.players.index(self.current_player) + 1) % len(self.players)]
            else:
                print('That cell is already occupied. Please try again.')

    def end(self):
        print('Thanks for playing!')

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self):
        while True:
            try:
                move = int(input(f'{self.name}, enter your move (1-9): '))
                if 1 <= move <= 9:
                        return move
            except ValueError:
                pass

class Board:
    def __init__(self):
        self.cells = [' ' for _ in range(9)]

    def display(self):
        print(f'''
         {self.cells[0]} | {self.cells[1]} | {self.cells[2]} 
        -----------
         {self.cells[3]} | {self.cells[4]} | {self.cells[5]} 
        -----------
         {self.cells[6]} | {self.cells[7]} | {self.cells[8]} 
        ''')

    def make_move(self, move, symbol):
        if self.cells[move-1] == ' ':
            self.cells[move-1] = symbol
            return True
        else:
            return False

    def check_win(self, symbol):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for condition in win_conditions:
            if all(self.cells[i] == symbol for i in condition):
                return True
        return False

    def check_tie(self):
        return ' ' not in self.cells


game = Game()
game.start()
game.end()
