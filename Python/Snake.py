import random


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

class Snake():
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction
        self.grow_snake = False

    def take_step(self, direction):
        # Calculate new head position based on the current head and direction
        new_head = (self.body[-1][0] + direction[0], self.body[-1][1] + direction[1])
        
        check_x = self.body[-1][0] + direction[0] 
        check_y = self.body[-1][1] + direction[1]
        
        for x, y in self.body:
            if x == check_x and y == check_y:
                print("you died!")
                exit()

         # Move the snake: if grow_snake is True, don't remove the tail (i.e., grow the snake)
        if not self.grow_snake:
            # Move the snake by removing the tail and appending the new head
            self.body = self.body[1:] + [new_head]
        else:
            # If the snake needs to grow, just add the new head without removing the tail
            self.body.append(new_head)
            self.grow_snake = False  # Reset the grow_snake flag

    def grow(self):
        self.grow_snake = True


    def set_direction(self, direction):
        self.direction = direction

    def tail(self):
        return self.body[0]

    def append_tail(self):
        print("append tail!")
        x,y = self.tail()
        if self.direction == UP:
            self.body.insert(0, (x-1, y))

    def head(self):
        return self.body[-1]

class Apple:
    def __init__(self, game):
        self.game = game

    def set_loc(self):
        rand_x = random.randint(0, self.game.height - 1)
        rand_y = random.randint(0, self.game.width - 1)
        return rand_x, rand_y
    
    def delete(self):
        self.game.apple_x, self.game.apple_y = self.set_loc()

class Game():
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.snake = Snake([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)], UP)

        self.apple = Apple(self)
        self.apple_x, self.apple_y = self.apple.set_loc()

    def board_matrix(self):
        board = []
        for h in range(self.height):
            row = []
            for w in range(self.width):
                row.append(None)
            board.append(row)

        for i in self.snake.body:
            x, y = i  
            board[x][y] = 1
        # head
        head = self.snake.head()
        x, y = head
        board[x][y] = 2

        while board[self.apple_x][self.apple_y] is not None:
            self.apple_x, self.apple_y = self.apple.set_loc()
        board[self.apple_x][self.apple_y] = 3

        if self.snake.head() == (self.apple_x,self.apple_y):
            self.apple.delete()
            self.snake.grow()

        return board

    def render(self):
        matrix = self.board_matrix()

        print("+", end='')
        for i in range(self.width*3):
            print("-", end='')
        print("+")

        #######################################
        for i in range(self.height):
            print("|", end='')
            for j in range(self.width):
                if matrix[i][j] == None:
                    print(" - ", end='')
                elif matrix[i][j] == 1:
                    print(" O ", end='')
                elif matrix[i][j] == 2:
                    print(" # ", end='')
                elif matrix[i][j] == 3:
                    print(" A ", end='')
            print("| ") 
        ########################################

        print("+", end='')
        for i in range(self.width*3):
            print("-", end='')
        print("+")

    def get_movement(self):
        dir = input(">> ")
        if dir == 'w':
            self.snake.take_step(UP)
            self.snake.set_direction(UP)
        elif dir == 'a':
            self.snake.take_step(LEFT)
            self.snake.set_direction(LEFT)
        elif dir == 'd':
            self.snake.take_step(RIGHT)
            self.snake.set_direction(RIGHT)
        elif dir =='s':
            self.snake.take_step(DOWN)
            self.snake.set_direction(DOWN)

    def loop(self):
        while True:
            self.render()
            self.get_movement()


game = Game(10, 20)
game.loop()

        