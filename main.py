# COM speed 115200
# with SCL in D1 and SDA in D2

from machine import Pin, I2C
from time import sleep
from random import getrandbits
import ssd1306
#import framebuf
#import aengusscreen

def rectangle(x, y):
	for i in range(scale*x, scale*(x+1)):
		for j in range(scale*y, scale*(y+1)):
			display.pixel(i, j, 1)

def update():
	display.fill(0)
	for i in points:
		rectangle(*i)
	rectangle(*point)
	display.show()

def stamp():
	test = [i[0] for i in points]
	if(not point[0] in test):
		points.append(list(point))

def changepointrandomly():
	if(getrandbits(1)):
		if(getrandbits(1) and point[0] < 128/scale - 1):
			point[0] += 1
		elif(point[0] > 0):
			point[0] -= 1
	else:
		if(getrandbits(1) and point[1] < 64/scale - 1):
			point[1] += 1
		elif(point[1] > 0):
			point[1] -= 1
		


i2c = I2C(sda = Pin(4), scl = Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

scale = 8
points = []
point = [0,0]
update()


while(True):
	changepointrandomly()
	update()
	if(getrandbits(3) == 0):
		stamp()
	sleep(getrandbits(2)/6)

# GUIDE
#display.contrast(255)
#display.text('Hello, World!', 0, 0, 1)
#display.pixel(0, 0, 1)
#display.pixel(127, 63, 1)
#display.show()

#display.fill(0)
#display.show()

#display.hline(0, 8, 4, 1) # not working
#display.rect(10, 10, 107, 43, 1) # not working

#import os
#os.remove("main.py")
#os.listdir()
#f = open("main.py", "w")
#f.write(a)
#f.close()
#hit control D to restart the board.