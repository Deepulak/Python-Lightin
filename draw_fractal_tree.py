import turtle

obj = turtle.Turtle()

obj.speed(10)
list1 = ['yellow', 'red', 'green', 'blue', 'orange']

for i in range(200):
	obj.color(list1[i%5])
	obj.pensize(i/10+1)
	obj.forward(i)
	obj.left(59)

turtle.done()