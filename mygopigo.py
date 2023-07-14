from gopigo import *

from time import sleep

def forward(time = 1.0, speed = 100):
    set_speed(speed)
    fwd()
    sleep(time)
    stop()

def back(time = 1.0, speed = 100):
    set_speed(speed)
    bwd()
    sleep(time)
    stop()

def left(time = 1.0, speed = 100):
    set_speed(speed)
    gopigp.left()
    sleep(time)
    stop()

def right(time = 1.0, speed = 100):
    set_speed(speed)
    gopigo.right()
    sleep(time)
    stop()


