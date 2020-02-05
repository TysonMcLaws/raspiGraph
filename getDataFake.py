import random 
from datetime import datetime as d
from time import sleep
import os

dataFile = open("myData.txt", "w")
dataFile.close()
dataTaken = 0
while True:
	duration = input("How many seconds do you want to test? ")
	rare =input("How often do you want to test? (Per Second) ")
	if int(duration) > 59:
		print("VALUE MUST BE LESS THAN 59 SECONDS")
	else:
		break
		
while True:
	print("Waiting for Timing...")
	print(str(60 - d.now().second) + " More Seconds")
	os.system("clear")
	if d.now().second == 0:
		break

while True :
	dataFile = open("myData.txt", "a")
	message = ""
	if 1 == 1:
		message += str(random.randrange(0, 2)) + ","
	else:
		message += "0,"
		
	if 2 == 2:
		message += str(random.randrange(0, 2)) + ","
	else:
		message += "0,"
	
	if 3 == 3:
		message += str(random.randrange(0, 2)) + ","
	else:
		message += "0,"
	
	if 4 == 4:
		message += str(random.randrange(0, 2)) + ","
	else:
		message += "0,"
	
	if 5 == 5:
		message += str(random.randrange(0, 2)) + ","
	else:
		message += "0,"
		
	if 6 == 6:
		message += str(random.randrange(0, 2)) + ","
	else:
		message += "0,"
	
	if 7 == 7:
		message += str(random.randrange(0, 2)) + ","
	else:
		message += "0,"
		
	if 8 == 8:
		message += str(random.randrange(0, 2)) + ","
	else:
		message += "0,"
	
	if 9 == 9:
		message += str(random.randrange(0, 2)) + ","
	else:
		message += "0,"
		
	message += str(d.now().second) + str(d.now().microsecond)[0] + str(d.now().microsecond)[1] +","
	dataFile.write(message)	
	dataTaken += 1
	print("Runs: " + str(dataTaken))
	sleep(1/int(rare))
	dataFile.close()
	
	if d.now().second == int(duration):
		break	