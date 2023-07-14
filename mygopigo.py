import gopigo as gpg

from time import sleep
from math import floor

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

def blink(time = 5.0, blink_time = 0.5):
    
    blinks = time/(blink_time*2)
    for _ in range (int(floor(blinks))):
        gpg.led_on(gpg.LED_L)
        gpg.led_on(gpg.LED_R)
        sleep(blink_time)
        gpg.led_off(gpg.LED_L)
        gpg.led_off(gpg.LED_R)
        sleep(blink_time)
