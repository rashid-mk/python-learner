python=1
import turtle
#print(python)#000000#CB2828
import calendar
import time
#print(calendar.month(2020,6))
my_turtle=turtle.Turtle()
my_turtle.speed(10000)
def move_turtle():
	while True:
		my_turtle.right(23)
		my_turtle.right(4)
		my_turtle.forward(10)
		my_turtle.right(23)
		my_turtle.forward(80)
		my_turtle.right(90)
		for i in range(4):

			my_turtle.forward(50)
			my_turtle.right(90)
			my_turtle.left(45)
			my_turtle.left(32)
			my_turtle.left(5)
			my_turtle.left(-45)
			my_turtle.left(45)
		#turtle.done()
move_turtle()
