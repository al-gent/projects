#welcome window
print("Welcome to the Snake Game!")
difficulty = int(input("Enter difficulty level(1-5): "))

# setup window
import curses
from random import randint
curses.initscr()
win = curses.newwin(20, 60, 0, 0) # y,x
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1) # -1

# snake and food
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)

ESC = 27

#game logic
score = 0
key = curses.KEY_RIGHT
while key != ESC:
    win.addstr(0, 2, 'Score ' + str(score) + ' ')
    win.timeout(200 // difficulty - len(snake)*(5)) # increase speed
    
    prevkey = key
    event = win.getch()
    
    key = event if event != -1 else prevkey
    
    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prevkey
        
    # calculate next coordinates
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1
        
    snake.insert(0, (y, x)) # append O(n)
    
    #check if we hit the border
    if y == 0: break
    if y == 19: break
    if x == 0: break
    if x == 59: break
    
    # if snake runs over itself
    if snake[0] in snake[1:]: break
    
    # if snake eats the food
    if snake[0] == food:
        score += 1
        food = ()
        while food == ():
            food = (randint(1, 18), randint(1, 58))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], '#')
        
    else:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
    
    for c in snake:
        win.addch(c[0], c[1], '*')
        
    win.addch(food[0], food[1], '#')
    
curses.endwin()
print(f"Final score = {score}")
    