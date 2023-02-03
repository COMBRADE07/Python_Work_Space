import turtle

from score import Score
from food import Food
from snake import Snake
from turtle import Turtle, Screen
import time

# for preventing maximize window
Screen().cv._rootwindow.resizable(False, False)
try:
    screen = Screen()
    screen.setup(height=700, width=700)
    screen.title('Hungry_Dungry_Snake')
    screen.bgcolor('black')
    screen.tracer(0)

    # creating snake
    ss = Snake()

    # feeding food
    food = Food()

    score = Score()

    screen.listen()
    screen.onkey(ss.up, "Up")
    screen.onkey(ss.down, "Down")
    screen.onkey(ss.left, "Left")
    screen.onkey(ss.right, "Right")
    screen.onkey(ss.pause, "space")

    status = True
    while status:
        screen.update()
        time.sleep(0.5)
        ss.move()

        #   detecting food
        if ss.head.distance(food) < 13:
            food.refresh()
            ss.extend()
            # updating scoreboard
            score.update_score()

        #     making boundry and game over
        if ss.head.xcor() > 340 or ss.head.ycor() > 330 or ss.head.xcor() < -340 or ss.head.ycor() < -330:
            score.game_over()
            status = False
            ss.pause()
            exit()
    turtle.exitonclick()
except Exception as e:
    print("Game Over")


