import curses


# Here starts the code to make the robot move
stdscr = curses.initscr()

while True:
    stdscr.refresh()
    print stdscr.getch()