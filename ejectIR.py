#!/usr/bin/env python
#coding: utf-8

import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

while 1:
	if GPIO.input(4):
		os.system("eject")
		print "Welcome to my room!!"
		time.sleep(1)
		os.system("eject -t")
		continue
	else:
		print "no input"

GPIO.cleanup()
#EOF
