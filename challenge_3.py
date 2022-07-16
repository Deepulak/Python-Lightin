from turtle import *

ht(); speed(0)
dot(510, "black")

def draw(col, size):
	color(col); rt(15)
	for i in range(36):
		for j in range(4):
			fd(size); rt(90)
		rt(360/36)

draw("lightgreen", 180)
draw("lightblue", 125)
draw("yellow", 87)

dot(172, "black")

done()