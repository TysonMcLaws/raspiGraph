import matplotlib.pyplot as plt

dataFile = open("myData.txt", "r")
info = dataFile.read()
dataFile.close()
info = info.split(",")

pinsMe = 123456789

x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
x9 = []
y = []

for i in range(0, len(info), 10):
	x1.append(info[i])
for i in range(1, len(info), 10):
	x2.append(info[i])
for i in range(2, len(info), 10):
	x3.append(info[i])
for i in range(3, len(info), 10):
	x4.append(info[i])
for i in range(4, len(info), 10):
	x5.append(info[i])
for i in range(5, len(info), 10):
	x6.append(info[i])
for i in range(6, len(info), 10):
	x7.append(info[i])
for i in range(7, len(info), 10):
	x8.append(info[i])
for i in range(8, len(info), 10):
	x9.append(info[i])
for i in range(9, len(info), 10):
	y.append(info[i])

x1.pop()

plt.subplot(331)
plt.plot(y, x1)
plt.ylabel('HDMI Results')
plt.legend(['Pin 1'])

if str(pinsMe).find("2") != -1:
	plt.subplot(332)
	plt.plot(y, x2, color = "red")
	plt.ylabel('HDMI Results')
	plt.legend(['Pin 2'])
if str(pinsMe).find("3") != -1:
	plt.subplot(333)
	plt.plot(y, x3, color = "orange")
	plt.ylabel('HDMI Results')
	plt.legend(['Pin 3'])
if str(pinsMe).find("4") != -1:
	plt.subplot(334)
	plt.plot(y, x4, color = "yellow")
	plt.ylabel('HDMI Results')
	plt.legend(['Pin 4'])
if str(pinsMe).find("5") != -1:
	plt.subplot(335)
	plt.plot(y, x5, color = "green")
	plt.ylabel('HDMI Results')
	plt.legend(['Pin 5'])
if str(pinsMe).find("6") != -1:
	plt.subplot(336)
	plt.plot(y, x6, color = "blue")
	plt.ylabel('HDMI Results')
	plt.legend(['Pin 6'])
if str(pinsMe).find("7") != -1:
	plt.subplot(337)
	plt.plot(y, x7, color = "indigo")
	plt.ylabel('HDMI Results')
	plt.legend(['Pin 7'])
if str(pinsMe).find("8") != -1:
	plt.subplot(338)
	plt.plot(y, x8, color = "violet")
	plt.ylabel('HDMI Results')
	plt.legend(['Pin 8'])
if str(pinsMe).find("9") != -1:
	plt.subplot(339)
	plt.plot(y, x9, color = "black")
	plt.ylabel('HDMI Results')
	plt.legend(['Pin 9'])

plt.show()