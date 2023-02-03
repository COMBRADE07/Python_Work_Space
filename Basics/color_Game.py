import random
from tkinter import *

# list of possible colors
colors = ["red", "green", "blue", "yellow", "purple", "orange"]

# choose a random color
chosen_color = random.choice(colors)


def check_guess():
    # get the user's guess
    guess = color_entry.get()
    # check if the guess is correct
    if guess.lower() == chosen_color:
        result_label.config(text="Correct!")
    else:
        result_label.config(text="Wrong! Try again.")


def show_answer():
    result_label.config(text="The answer is: " + chosen_color)


def reset():
    global chosen_color
    chosen_color = random.choice(colors)
    color_entry.delete(0, END)
    result_label.config(text="")


# create the main window
root = Tk()
root.title("Guess the Color")

# create a label for instructions
instructions = Label(root, text="Guess the color I'm thinking of:")
instructions.pack()

# create an entry widget for the user's guess
color_entry = Entry(root)
color_entry.pack()

# create a button to check the user's guess
check_button = Button(root, text="Check", command=check_guess)
check_button.pack()

# create a button to show the answer
show_answer_button = Button(root, text="Show Answer", command=show_answer)
show_answer_button.pack()

# create a button to reset the game
reset_button = Button(root, text="Reset", command=reset)
reset_button.pack()

# create a label to display the result
result_label = Label(root, text="")
result_label.pack()

# start the event loop
root.mainloop()
