class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
            print "Using Windows keymode"
        except ImportError:
            self.impl = _GetchUnix()
            print "Using Unix keymode"

    def getkey(self):
        return self.impl.getkey()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def getkey(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def getkey(self):
        import msvcrt
        if msvcrt.kbhit():
            return msvcrt.getch()
        else:
            return '-'


getch = _Getch()
