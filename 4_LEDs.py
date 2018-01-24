#!/usr/bin/python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)

#Assignments
r = 4
b = 17
y = 21
g = 22

#Red
GPIO.setup(r,GPIO.OUT)

#Blue
GPIO.setup(b,GPIO.OUT)

#Yellow
GPIO.setup(y,GPIO.OUT)

#Green
GPIO.setup(g, GPIO.OUT)

#Time between alternating lights
lapse = 1

while 1:
    #Red on, Blue off, Yellow off, Green off
    GPIO.output(g, GPIO.LOW)
    GPIO.output(r, GPIO.HIGH)
    time.sleep(lapse)

    #Red off, Blue on, Yellow off, Green off
    GPIO.output(r, GPIO.LOW)
    GPIO.output(b, GPIO.HIGH)
    time.sleep(lapse)

    #Red off, Blue on, Yellow on, Green off
    GPIO.output(b, GPIO.LOW)
    GPIO.output(y, GPIO.HIGH)
    time.sleep(lapse)

    #Red off, Blue on, Yellow off, Green on
    GPIO.output(y, GPIO.LOW)
    GPIO.output(g, GPIO.HIGH)
    time.sleep(lapse)
