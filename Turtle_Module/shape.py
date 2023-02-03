import turtle
from turtle import Turtle, TurtleScreen
import random
win = Turtle()


def draw_shape(no_of_sides):
    # pentagon if no_of_sides = 5
    for _ in range(no_of_sides):
        angle = 360 // no_of_sides
        win.forward(100)
        win.right(angle)


col = ['red', 'blue', 'green', 'orange', 'grey', 'pink']
for i in range(3, 11):
    no_of_sides = i
    win.color(random.choice(col))
    draw_shape(i)

turtle.exitonclick()
