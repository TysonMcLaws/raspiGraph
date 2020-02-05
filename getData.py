from datetime import datetime as d
import os
from time import sleep

try:
	import RPi.GPIO as GPIO
except:
	print("You don't have a Raspberry Pi.")
	print("Please Run This on a Raspberry Pi.")
	quit()
	
while True:
	duration = input("How many seconds do you want to test? ")
	rare =input("How often do you want to test? (Per Second) ")
	if int(duration) > 59:
		print("VALUE MUST BE LESS THAN 59 SECONDS")
	else:
		break
 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pin1 = 29 #GPIO 5
pin2 = 31 #GPIO 6
pin3 = 33 #GPIO 13
pin4 = 35 #GPIO 19
pin5 = 37 #GPIO 26
pin6 = 32 #GPIO 12
pin7 = 36 #GPIO 16
pin8 = 38 #GPIO 20
pin9 = 40 #GPIO 21
led = 7 #GPIO 4

GPIO.setup(pin1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pin2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pin3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pin4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pin5, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pin6, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pin7, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pin8, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pin9, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(led, GPIO.OUT)

dataFile = open("myData.txt", "w")
dataFile.close()
dataTaken = 0

while True:
	print("Waiting for Timing...")
	os.system("clear")
	if d.now().second == 0:
		print("--GO--")
		break

while True:
	dataFile = open("myData.txt", "a")
	message = ""
	GPIO.output(led, GPIO.HIGH)
	if (GPIO.input(pin1) == HIGH):
		message += "1,"
	else:
		message += "0,"
	if (GPIO.input(pin2) == HIGH):
		message += "1,"
	else:
		message += "0,"
	if (GPIO.input(pin3) == HIGH):
		message += "1,"
	else:
		message += "0,"
	if (GPIO.input(pin4) == HIGH):
		message += "1,"
	else:
		message += "0,"
	if (GPIO.input(pin5) == HIGH):
		message += "1,"
	else:
		message += "0,"
	if (GPIO.input(pin6) == HIGH):
		message += "1,"
	else:
		message += "0,"
	if (GPIO.input(pin7) == HIGH):
		message += "1,"
	else:
		message += "0,"
	if (GPIO.input(pin8) == HIGH):
		message += "1,"
	else:
		message += "0,"
	if (GPIO.input(pin9) == HIGH):
		message += "1,"
	else:
		message += "0,"	
		
	message += str(d.now().second) + "000" + str(d.now().microsecond) + ","
	dataFile.write(message)	
	dataTaken += 1
	print("Runs: " + str(dataTaken))
	sleep(1/int(rare))
	dataFile.close()
	
	if d.now().second == int(duration):
		GPIO.output(led, GPIO.LOW)
		break	
		
GPIO.cleanup()
