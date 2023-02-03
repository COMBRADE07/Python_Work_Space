import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('circle')
        self.up()
        self.speed(0)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('green')
        self.refresh()

    def refresh(self):
        x = random.randint(-330, 330)
        y = random.randint(-330, 330)
        self.goto(x, y)