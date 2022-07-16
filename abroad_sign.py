from turtle import *

ht(); pu(); sety(-140)
shape("square"); shapesize(3,40)

colors = ("red3","orange","yellow2","seagreen","orchid","royalblue1","dodgerblue4")

for i in range(7):
	color(colors[i]); stamp(); sety(ycor()+60)

pu(); sety(-105); pd()
shape("turtle"); color("white"); width(25); circle(145)
lt(90); fd(280)

bk(120); seth(-40); fd(140)
bk(140); seth(220); fd(140)

done()
