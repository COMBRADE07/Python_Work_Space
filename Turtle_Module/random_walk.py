from turtle import Turtle, TurtleScreen
import turtle
import random

win = Turtle()

# for i in range(0, 10):
#     print(random.randint(0, 40))
win.speed(5)
win.pensize(15)
angle = [90,180,270]
colorx = ['red', 'orange', 'pink', 'blue', 'purple']
for i in range(50):
    win.forward(30)
    win.color(random.choice(colorx))
    win.setheading(random.choice(angle))

turtle.exitonclick()
