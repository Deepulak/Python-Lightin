import turtle

# number of sides
n = 60

# creating instance of turtle
pen = turtle.Turtle()
# loop to draw a side
for i in range(n):
	# drawing side of the length i*10
	pen.forward(i * 10)
	# changing direction of pen by 144 degree
	#in clockwise
	pen.right(144)
# closing the instance
turtle.done()