''' testing python functions without dependencies '''
import time
from _Getch import getch

while True:
    KEY_PRESSED = ord(getch.getkey())
    if KEY_PRESSED != 45:  # if input (if input = '-')
        pass
    elif KEY_PRESSED == 27:  # ESC
        exit()
    elif KEY_PRESSED == 80:  # Down arrow:
        print "hit down"
    elif KEY_PRESSED == 72:  # Down arrow:
        print "hit up"
    elif KEY_PRESSED == 75:  # Down arrow:
        print "hit left"
    elif KEY_PRESSED == 77:  # Down arrow:
        print "hit right"
    elif KEY_PRESSED == ord('w'):
        print "hit w"
    elif KEY_PRESSED == ord('a'):
        print "hit a"
    elif KEY_PRESSED == ord('s'):
        print "hit s"
    elif KEY_PRESSED == ord('d'):
        print "hit d"
    elif KEY_PRESSED > 47 and KEY_PRESSED < 58:
        print "hit {}".format(KEY_PRESSED - 48)
    else:
        # print key_pressed # uncomment for more key tests
        pass

    # print "looping"
    print "sleep"
    time.sleep(5)
    print "awake"

print "exit"
