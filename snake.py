import random
left = (0, -1)
right = (0, 1)
up = (-1, 0)
down = (1,0)

class Game:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.snake = Snake([(0,0),(0,1)], right)
        apple_position = random.randint(0,h-1), random.randint(0,w-1)
        self.apple = Apple((apple_position))

    def board_matrix(self):
        return [[None for _ in range(self.w)] for _ in range(self.h)]

    def render(self):
        self.matrix = self.board_matrix()
        top = ['__' for _ in range(self.w)]
        bottom = ['‾‾' for _ in range(self.w)]
        self.matrix[self.apple.position[0]][self.apple.position[1]] = 'AA'
        print(top)
        for x, y in self.snake.body[:-1]:
            self.matrix[x][y] = 'OO'
        self.matrix[self.snake.body[-1][0]][self.snake.body[-1][1]] = 'XX'
        for line in self.matrix:
            print('|',' '.join(line),'|')
        print(bottom)
        
        
    def update(self):
        x= self.snake.body[-1][0] + self.snake.direction[0]
        y = self.snake.body[-1][1] + self.snake.direction[1]
        x = x % self.h
        y = y % self.w
        new_position = (x,y)
        self.snake.take_step(new_position)

    def eat_apple(self):
        if self.snake.body[-1] == self.apple.position:
            self.snake.body = self.snake.body + [self.apple.position]
            apple_position = random.randint(0,self.h-1), random.randint(0,self.w-1)
            self.apple = Apple((apple_position))
            
    def check_collision(self):
        return self.snake.body[-1] in self.snake.body[:-1]


    def play(self):
        direction = input("Enter a direction: ")
        if direction == 'w':
            self.snake.set_direction(up)
        elif direction == 'a':
            self.snake.set_direction(left)
        elif direction == 's':
            self.snake.set_direction(down)
        elif direction == 'd':
            self.snake.set_direction(right)
        elif direction =='q':
            print('you have quit - loser')
            return
        self.update()
        if self.check_collision():
            print('you have collided - loser')
            return
        self.eat_apple()
        self.render()
        self.play()
        

class Snake:
    """"Snake Stuff"""
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction        
        
    def take_step(self, position):
        self.body = self.body[1:] + [position]
        
    def set_direction(self, direction):
        self.direction = direction  


class Apple:
    """"Apple stuff"""
    def __init__(self, position):
        self.position = position



Game(10,20).play()