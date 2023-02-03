from turtle import Turtle
from food import Food

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_count = 0
        self.writing = f"Score: {self.score_count}"
        self.color('white')
        self.penup()
        self.goto(-50,320)

        self.write(arg=self.writing, align='left', font=('Times new roman', 20, 'normal'))
        self.hideturtle()


    def update_score(self):
        self.score_count += 5
        self.clear()
        self.writing = f"Score: {self.score_count}"
        self.write(arg=self.writing, align='left', font=('Times new roman', 20, 'normal'))
        
    def game_over(self):
        self.clear()
        self.speed(0)
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('Times new roman', 25, 'normal'))

