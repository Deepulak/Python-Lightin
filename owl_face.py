from turtle import *

def eyes():
	shape("circle")
	shapesize(5); color("lightgrey"); stamp()
	shapesize(3); color("black"); stamp()
	shapesize(2.5); color("orange"); stamp()
	shapesize(1.3); color("black"); stamp()

pu(); ht()
goto(75, -20)  # external circle
dot(350)
dot(325, "ivory")

goto(0, -15); eyes() # left eye
fd(160); eyes() # right eye

lt(45); goto(80, 22); shape("square"); shapesize(8);
color("ivory"); stamp()

shape("turtle"); shapesize(1); color("black"); setpos(82,-90)  # break

begin_fill()

fd(60); lt(90); circle(62, 90); rt(90); bk(60)

end_fill()

done()