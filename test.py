from msvcrt import getch, kbhit



while True:
    if kbhit(): # if input 
        key_pressed = ord(getch())
        if key_pressed == 27: #ESC
            exit()
        elif key_pressed == 80: #Down arrow:
            print "hit down"
        elif key_pressed == 72: #Down arrow:
            print "hit up"
        elif key_pressed == 75: #Down arrow:
            print "hit left"
        elif key_pressed == 77: #Down arrow:
            print "hit right"
        elif key_pressed == ord('w'):
            print "hit w"
        elif key_pressed == ord('a'):
            print "hit a"
        elif key_pressed == ord('s'):
            print "hit s"
        elif key_pressed == ord('d'):
            print "hit d"
        elif key_pressed > 47 and key_pressed < 58:
            print "hit {}".format(key_pressed-48)
        else:
            print key_pressed
            pass
            

    #print "looping"

print "exit"