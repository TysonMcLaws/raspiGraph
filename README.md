# raspiGraph
This code uses 9 of the pins on a Raspberry Pi 3 to act as a digital oscilloscope.  Then graphs the result.

getData.py gets data for the time perdiod you set and the frecuency.

getDataFake.py generates random numbers for the time perdiod you set and the frecuency.

graphTest.py graphs the result.

RPi_GPIO is an image of the pinout used.

Result Sample:

0,0,1,0,1,0,0,1,0,017,0,0,0,0,0,0,1,1,0,010,1,1,0,1,1,1,1,1,0,020,

**You need the last comma

***Runs in sets of ten (Index [0-8]-Inputs && Index [9]-Time (Seconds && 2 Microsecond Didgets))
