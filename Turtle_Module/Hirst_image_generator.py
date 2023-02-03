from turtle import Turtle, TurtleScreen
import turtle
import random as r

# import colorgram
# """
#     colorgram package used for extracting rgb color from images....
# """
# rgb_col = []
# col = colorgram.extract("C:\\Users\\Rhuti\\OneDrive\\Desktop\\colorx.png",30)
#
# # extracting and store into list
#
# for color in col:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_col = (r,g,b)
#     rgb_col.append(new_col)
#
# print(rgb_col)
#

win = Turtle()
color = ["White", "Black", "Red","green","magenta","cyan","yellow","orange","purple","brown"]

# create dots for hirst images
win.setheading(225)
win.forward(300)
win.setheading(0)
win.speed(0)
for i in range(5):
    for _ in range(10):
        win.dot(20, r.choice(color))
        win.forward(r.randint(30, 60))

    win.setheading(90)
    win.forward(50)
    win.left(90)
    for _ in range(10):
        win.dot(20, r.choice(color))
        win.forward(r.randint(30, 60))

    win.setheading(90)
    win.forward(50)
    win.right(90)
turtle.exitonclick()
