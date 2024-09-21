import random

class Game:
    def __init__(self):
        self.score = 0
        self.red = [] # X
        self.blue = [] # O

    def board_matrix(self):
        board = []

        # Phase 1: Plain board
        for i in range(0, 3):
            row = []
            for j in range(0, 3):
                row.append(None)
            board.append(row)

        # Phase 2: Red board
        for locations in self.red:
            x, y = locations
            board[x][y] = 1

        # Phase 3: Blue board
        for locations in self.blue:
            x, y = locations
            board[x][y] = 2

        return board

    def render(self):
        board = self.board_matrix()

        print("$", end='')
        for i in range(len(board)*3 - 2): print("=",end='')
        print("$")

        for row in board:
            for item in row:
                if item is None:
                    print(" / ", end='')
                elif item == 1:
                    print(" X ", end='')
                else:
                    print(" O ", end='')
            print()

        print("$", end='')
        for i in range(len(board)*3 - 2): print("=",end='')
        print("$")

    def get_turn(self):
        choice = input("Choose your turn: ")

        row = int(choice[:1])
        col = int(choice[-1:])

        for locations in self.red:
            x, y = locations
            if x == row and y == col:
                print("Invalid move. Try again.")
                self.get_turn()
                return

        self.take_turn(row, col)
        self.enemy_turn()

    def take_turn(self, row, col):
        self.red.append((row, col))
        print(self.red)

    def enemy_turn(self):
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        for locations in self.red:
            x, y = locations
            if x == row and y == col:
                self.enemy_turn()
                return
            else:
                self.blue.append((row, col))

    def loop(self):
        while True:
            self.get_turn()
            self.render()
    
game = Game()
game.loop()