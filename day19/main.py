from turtle import Turtle, Screen
import random

is_race = False
screen = Screen()
screen.setup(width=500, height=500)

user_get = screen.textinput(title="make your bet", prompt="which turtle: ")
color_list = ["red", "green", "yellow", "blue", "purple", "orange"]
y_positions = [-100, -70, -40, -10, 20, 50]
all_turtle = []

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])
    tim.color(color_list[turtle_index])
    all_turtle.append(tim)


if user_get:
    is_race = True

while is_race:
    rand_distance = random.randint(1,10)
    tim.forward(rand_distance)