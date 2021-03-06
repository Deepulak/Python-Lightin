from turtle import *
import random

speed(speed='fastest')

def draw(n, x, angle):
	#%23 loop for number of stars
	for i in range(n):
		colormode(255)
	#	%23 choosing random integers
	#	%23 between 0 to 255
	#	%23 to generate random rgb values
		a = random.randint(0, 255)
		b = random.randint(0, 255)
		c = random.randint(0, 255)
	#	%23 setting the outline
	#	%23 and fill color
		pencolor(a, b, c)
		fillcolor(a, b, c)
		# begins filling the start
		begin_fill()
		# loop for drawing each start
	for j in range(5):
		forward(5 * n - 5 * i)
		right(x)
	 	forward(5 * n - 5 * i)
	 	right(72 - x)
	# Color filling complete
	end_fill()
	# rotating fot
	# the next star
	rt(angle)
	 # setting the parameter
n = 30 # number of stars
x = 144 # exterior angle of each star
angle = 18 # angle of roation for the spiral
draw(n, x, angle)