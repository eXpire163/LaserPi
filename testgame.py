import curses


# Here starts the code to make the robot move
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.nodelay(1)  #nodelay(1) give us a -1 back when nothing is pressed


while True:
    stdscr.refresh()
        print stdscr.getch()