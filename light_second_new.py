from turtle import *

pu(); goto(-190,-125); pd()
lt(90); width(10); color('red')

for i in range(5):
	fd(500); bk(250); rt(360/5)

pu(); goto(-430,-300); pd()

for i in range(5):  
	#outline
	fd(600); rt(360/5)

done()
