from turtle import Turtle,TurtleScreen
import turtle

ok = Turtle()
ok.speed(0)

def graph(size):
    for _ in range(360//size):
        ok.circle(100)
        ok.setheading(ok.heading()+size)

graph(5)
turtle.exitonclick()
