''' running laser point laser show '''
import time
import atexit
import threading

from Adafruit_MotorHAT import Adafruit_MotorHAT

from _Getch import getch

#from scipy import interpolate


# create a default object, no changes to I2C address or frequency
MH = Adafruit_MotorHAT(addr=0x60)

MOTOR_X = MH.getStepper(200, 1)
MOTOR_Y = MH.getStepper(200, 2)        # 200 steps/rev, motor port #1

atexit.register(turn_off_motors)

CURRENT_X = 0
CURRENT_Y = 0
MAX_X = 5
MAX_Y = 5
ACTIVE = False

CURRENT_MODE = 1

STEP_MODE = Adafruit_MotorHAT.SINGLE



def turn_off_motors():
    ''' turn off and release all stepper motors '''
    go_to_pos(0, 0)
    MH.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    MH.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    MH.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    MH.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


def stepper_worker(stepper, numsteps, direction, style):
    ''' helper for async move '''
    # print("Steppin!")
    stepper.step(numsteps, direction, style)
    # print("Done")


def go_to_pos(pos_x, pos_y):
    '''moves to new position, first x than y'''
    global CURRENT_X
    global CURRENT_Y
    # check direction to move
    dir_x = Adafruit_MotorHAT.FORWARD if pos_x > CURRENT_X else Adafruit_MotorHAT.BACKWARD
    dir_y = Adafruit_MotorHAT.FORWARD if pos_y > CURRENT_Y else Adafruit_MotorHAT.BACKWARD
    # move to target position
    MOTOR_X.step(abs(pos_x - CURRENT_X), dir_x, STEP_MODE)
    MOTOR_Y.step(abs(pos_y - CURRENT_Y), dir_y, STEP_MODE)
    # update positions
    CURRENT_X = pos_x
    CURRENT_Y = pos_y


def go_to_pos_async(pos_x, pos_y):
    '''moves to new position, multi threaded '''
    global CURRENT_X
    global CURRENT_Y
    # check direction to move
    dir_x = Adafruit_MotorHAT.FORWARD if pos_x > CURRENT_X else Adafruit_MotorHAT.BACKWARD
    dir_y = Adafruit_MotorHAT.FORWARD if pos_y > CURRENT_Y else Adafruit_MotorHAT.BACKWARD
    # move to target position
    thread_x = threading.Thread(target=stepper_worker, args=(
        MOTOR_X, abs(pos_x - CURRENT_X), dir_x, STEP_MODE))
    thread_y = threading.Thread(target=stepper_worker, args=(
        MOTOR_Y, abs(pos_y - CURRENT_Y), dir_y, STEP_MODE))
    thread_x.start()
    thread_y.start()
    # update positions
    while thread_x.isAlive() and thread_y.isAlive():
        pass
    CURRENT_X = pos_x
    CURRENT_Y = pos_y


def check_keyboard_input():
    ''' check for keyboard input '''
    key_pressed = ord(getch.getkey())
    if  key_pressed != 45:  # if input (if input = '-')
        if key_pressed == 27:  # ESC
            exit()
        elif key_pressed == 80:
            print "hit down"
            MOTOR_Y.step(1, Adafruit_MotorHAT.FORWARD, STEP_MODE)
        elif key_pressed == 72:
            print "hit up"
            MOTOR_Y.step(1, Adafruit_MotorHAT.BACKWARD, STEP_MODE)
        elif key_pressed == 75:
            print "hit left"
            MOTOR_X.step(1, Adafruit_MotorHAT.FORWARD, STEP_MODE)
        elif key_pressed == 77:
            print "hit right"
            MOTOR_X.step(1, Adafruit_MotorHAT.BACKWARD, STEP_MODE)
        elif key_pressed == 77:
            print "toggle_active"
            global ACTIVE
            ACTIVE = not ACTIVE
        elif key_pressed == ord('w'):
            print "hit w"
            global MAX_Y
            MAX_Y += 1
        elif key_pressed == ord('a'):
            print "hit a"
            global MAX_X
            MAX_X -= 1
        elif key_pressed == ord('s'):
            print "hit s"
            global MAX_Y
            MAX_Y -= 1
        elif key_pressed == ord('d'):
            print "hit d"
            global MAX_X
            MAX_X += 1
        elif key_pressed > 47 and key_pressed < 58:
            print "hit {}".format(key_pressed - 48)
            global CURRENT_MODE
            CURRENT_MODE = key_pressed - 48
        else:
            pass
            # print key_pressed


def laser_off():
    ''' todo, turn off laser '''
    pass


def laser_on():
    ''' todo, turn on laser '''
    pass


def draw_rect(left, bottom, right, top):
    ''' draw rectangle full size '''
    go_to_pos(left, bottom)
    go_to_pos(left, top)
    go_to_pos(right, top)
    go_to_pos(right, bottom)


def main_loop():
    ''' main loop for laser action '''
    if CURRENT_MODE == 1:
        draw_rect(0, 0, MAX_X, MAX_Y)
    elif CURRENT_MODE == 2:
        for i in xrange(0, MAX_X / 2):
            draw_rect(i, i, MAX_X - i, MAX_Y - i)
    elif CURRENT_MODE == 3:
        pass
    else:
        pass




laser_on()

while True:
    check_keyboard_input()
    if ACTIVE:
        main_loop()
    else:
        laser_off()
        time.sleep(1)
