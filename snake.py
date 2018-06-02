
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint


curses.initscr()
win = curses.newwin(20, 80, 0, 0)
#Dimensions of the canvas
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

key = KEY_RIGHT                                                    
score = 0

snake = [[4,10], [4,9], [4,8]]
#Snake co-ordinates -> starting
food = [10,20]               
#food co-ordinates -> starting

win.addch(food[0], food[1], '@')                                   
# Prints the food

while key != 27:                                                   
#ASCII for esc = 27
    win.border(0)
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')                
#Print Score string 
    win.addstr(0, 24, 'WELCOME TO THE GAME OF SNAKE')
    win.addstr(19, 24, 'Author : Ojaswy')                                  
#Print'SNAKE' string
    win.timeout(100 - (len(snake)/5 + len(snake)/10)%120)          
#Increases the speed of Snake as its length increases
    
    prevKey = key                                                  
    event = win.getch()
    key = key if event == -1 else event 


    if key == ord(' '):                                            
#If SPACE BAR = Pause/Resume
        key = -1                                                   
        while key != ord(' '):
#ord -> returns the unicode of a single character
            key = win.getch()
        key = prevKey
        continue

    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     
#Invalid key! :(
        key = prevKey

#New coordinates of the head of the snake

    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

  
#If snake crosses boundaries
    if snake[0][0] == 0 or snake[0][0] == 19 or snake[0][1] == 0 or snake[0][1] == 79: break

#If snake eats itself
    if snake[0] in snake[1:]: break

    
    if snake[0] == food:                                            
#When snake eats the food
        food = []
        score += 1
        while food == []:
            food = [randint(1, 18), randint(1, 79)]                 
#Calculating next food's coordinates
            if food in snake: food = []
        win.addch(food[0], food[1], '@')
    else:    
        last = snake.pop()                                          
#If it does not eat the food, length decreases
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], 'O')
    
curses.endwin()
print("\nScore - " + str(score))
print("Better luck next time! :)\n")
