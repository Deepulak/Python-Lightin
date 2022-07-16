import turtle

obj = turtle.Turtle()

obj.speed(10)

obj.left(90)
obj.pencolor('green')
obj.pensize(5)
obj.up()
obj.goto(0, -300)
obj.down()

def Tree(l):
	if(l<10):
		return
	else:
		obj.forward(l)
		obj.left(30)
		Tree(3*l/4)
		obj.right(60)
		Tree(3*l/4)
		obj.left(30)
		obj.backward(l)

Tree(100)

turtle.done()