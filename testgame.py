import curses
import time
import atexit


# Here starts the code to make the robot move
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

def attheend():
    curses.nocbreak()
    stdscr.keypad(0)
    curses.endwin()

atexit.register = attheend


stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.nodelay(1)  #nodelay(1) give us a -1 back when nothing is pressed
Richtung = ' '
while Richtung != ord('q'):
	#Start of while loop
	stdscr.refresh()

	Richtung = stdscr.getch() #Gets the key which is pressed
		
	stdscr.addch(20,25,Richtung)
	
	if Richtung == ord('e'):
		print "StopMotors()"

	if  Richtung == ord('a'):
		print "Left()"

	if Richtung == ord('s'):
		print "Backwards()"

	if Richtung == ord('d'):
		print "Right()"
	
	if Richtung == ord('w'):
		print "Forwards()"
	
	if Richtung == int('-1'):
		print "StopMotors()"
		
	time.sleep(0.04) #I need the timesleep because if not the robot will get a -1 all the time and not move to fast while loop I think, have to work on this.
	#End of while loop
	
#Important to set everthing back by end of the script
attheend()
#StopMotors()
#GPIO.cleanup()
