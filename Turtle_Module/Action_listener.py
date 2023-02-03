import turtle
from turtle import Turtle, Screen

win = Turtle()
screen = Screen()


def movef():
    win.forward(20)


screen.listen()
screen.onkey(key="space", fun=movef)

turtle.exitonclick()
