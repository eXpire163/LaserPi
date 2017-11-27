import curses


# Here starts the code to make the robot move
stdscr = curses.initscr()


stdscr.nodelay(1)  #nodelay(1) give us a -1 back when nothing is pressed


while True:
    stdscr.refresh()
    Richtung = stdscr.getch() #Gets the key which is pressed
	stdscr.addch(20,25,Richtung)
    print Richtung