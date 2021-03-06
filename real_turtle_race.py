import turtle
import random, time

player1 = turtle.Turtle()	# Creating player 1
player1.shape("turtle")
player1.penup()
player1.goto(10, 20) 	# setting player 1's position
player1.pendown()
player1.color("blue")	# setting player 1's color
player1.write("Player 1")

player2 = turtle.Turtle()	# Creating player 2
player2.shape("turtle")
player2.penup()
player2.goto(10, 80) 	# setting player 2's position
player2.pendown()
player2.color("red")	# setting player 2's color
player2.write("Player 2")

start1 = 0
start2 = 0
end = 180
# Creating end circle for player 1
endTurtle1 = turtle.Turtle()
endTurtle1.penup()
# Creating end circle for player 1's position
endTurtle1.goto(200, 20)
endTurtle1.pendown()
# Creating a circle
endTurtle1.shape("circle")
# Coloring the circle
endTurtle1.fillcolor("white")
# Creating end circle for player 2
endTurtle2 = turtle.Turtle()
endTurtle2.penup()
# Creating end circle for player 2's position
endTurtle2.goto(200, 80)
endTurtle2.pendown()
# Creating a circle
endTurtle2.shape("circle")
# Coloring the circle
endTurtle2.fillcolor("white")

win = turtle.Screen()
#win.bgcolor("light green")
# running while loop until the start
# position for any player is less than end position
while start1<=end or start2<=end:
	if start1>=end:
		# printing the player1 name in the title
		win.title(f"Player1 position is {start1}, Player2 position is {start2}, Player1 wins")
		time.sleep(5)
		break
	elif start2>=end:
		# printing the player2 name in the title
		win.title(f"Player1 positioin is {start1}, Player2 position is {start2}, Player2 wins")
		time.sleep(5)
		break
	# dice for player1
	dice1 = random.randrange(1, 6)
	# dice for player2
	dice2 = random.randrange(1, 6)
	# forwarding player1
	player1.forward(dice1 * 2)
	time.sleep(1)
	# forwarding player2
	player2.forward(dice2 * 2)
	time.sleep(1)
	# Increasing position values for player1
	start1 += dice1 * 2
	# Increasing position values for player2
	start2 += dice2 * 2
	win.title(f"Player1 position is {start1}, player2 position is {start2}, no one wins")

time.sleep(3)
turtle.bye() 	