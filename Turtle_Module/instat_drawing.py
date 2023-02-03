import turtle
from turtle import Turtle, Screen

homie = Turtle()

screen = Screen()


def move_f():
    homie.forward(20)


def move_b():
    homie.backward(20)


def left():
    homie.left(20)


def right():
    homie.right(20)


def clear():
    homie.clear()
    homie.penup()
    homie.home()
    homie.pendown()

def up():
    homie.penup()

def down():
    homie.pendown()
screen.listen()
screen.onkey(key="d", fun=move_f)
screen.onkey(key="a", fun=move_b)
screen.onkey(key="w", fun=left)
screen.onkey(key="s", fun=right)
screen.onkey(key="c", fun=clear)
screen.onkey(key="u", fun=up)
screen.onkey(key="o", fun=down)
turtle.exitonclick()
