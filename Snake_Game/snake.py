import time
from turtle import Turtle, Screen

STARTING_POS = [(-330, 0), (-310, 0), (-290, 0)]
MD = 20


class Snake:
    def __init__(self):
        self.snake_factory = []
        self.generate()
        self.head = self.snake_factory[0]



    def extend(self):
        self.add(self.snake_factory[-1].position())

    def add(self,position):
        snake = Turtle("square")
        snake.color('red')
        snake.shapesize(stretch_wid=0.8, stretch_len=0.8)
        snake.up()
        snake.goto(position)
        self.snake_factory.append(snake)

    def generate(self):
        for s in STARTING_POS:
            self.add(s)

    def move(self):
        for s in range(len(self.snake_factory) - 1, 0, -1):
            x = self.snake_factory[s - 1].xcor()
            y = self.snake_factory[s - 1].ycor()
            self.snake_factory[s].goto(x, y)
        self.snake_factory[0].forward(MD)

    def left(self):
        if self.head.heading != 0:
            self.snake_factory[0].setheading(180)

    def right(self):
        if self.head.heading != 180:
            self.snake_factory[0].setheading(0)

    def up(self):
        if self.head.heading != 270:
            self.snake_factory[0].setheading(90)

    def down(self):
        if self.head.heading != 270:
            self.snake_factory[0].setheading(270)

    def pause(self):
        x = True
        time.sleep(5)
