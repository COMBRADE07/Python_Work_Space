# import turtle
# in this method we have to called class Turtle using turtle module as follows
# win = turtle.Turtle()
import turtle
#
from turtle import Turtle, TurtleScreen

my = Turtle()
my.shape("turtle")
my.color("orange")

# draw a square
for _ in range(4):
    my.forward(50)
    my.penup()
    my.forward(50)
    my.pendown()
    my.left(90)

turtle.exitonclick()
