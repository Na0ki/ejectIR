#!/usr/bin/env python
#coding: utf-8

import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN)




while 1:
#	print "before GPIO.input"
	if GPIO.input(4):
#	data = 'cat /sys/class/gpio/gpio4/value'
#	f = open('/sys/class/gpio/gpio4/value')
#	data1 = f.read()
#	f.close()
#	if data == 1:
#		print "after GPIO.input"
		os.system("eject")
		print "Welcome to my room!!"
		time.sleep(5)
		os.system("eject -t")
		data = 'cat /sys/class/gpio/gpio4/value'
		continue
	else:
		print "no input"

GPIO.cleanup()
#EOF
