import gopigo as gpg

from time import sleep

def forward(time = 1.0, speed = 100):
    gpg.set_speed(speed)
    gpg.fwd()
    sleep(time)
    gpg.stop()

def back(time = 1.0, speed = 100):
    gpg.set_speed(speed)
    gpg.bwd()
    sleep(time)
    gpg.stop()

def left(time = 1.0, speed = 100):
    gpg.set_speed(speed)
    gpg.left()
    sleep(time)
    gpg.stop()

def right(time = 1.0, speed = 100):
    gpg.set_speed(speed)
    gpg.right()
    sleep(time)
    gpg.stop()


