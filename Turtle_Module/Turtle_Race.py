import turtle
from turtle import Turtle, Screen
import random as r


class demo:
    def __init__(self):
        start = False
        screen = Screen()
        screen.title("Turtle_Racing 3")
        # screen.bgcolor("grey")
        screen.setup(width=700, height=600)
        try:
            x = screen.textinput(title="Chose a color:)", prompt="Which turtle will the race ?").lower()
        except Exception as e:
            print("Invalid data type.")

        colors = ['red', 'orange', 'green', 'purple', 'blue', 'black']
        pos = [200, 150, 100, 50, 0, -50]
        turtle_gang = []
        for i in range(6):
            homie = Turtle("turtle")
            homie.penup()
            homie.color(colors[i])
            homie.goto(x=-300, y=pos[i])
            turtle_gang.append(homie)

        if x:
            start = True

        while start:
            for homies in turtle_gang:
                if homies.xcor() > 310:
                    win_homies = homies.pencolor()

                    if win_homies == x:
                        print('Congrats ! your turtle wins )==== 00 0 0 . . .')

                    else:
                        print(f"Oops you lose ;(, the winner is {homies.pencolor()}")
                    start = False
                homies.forward(r.randint(0, 10))


obbj = demo()
turtle.exitonclick()
