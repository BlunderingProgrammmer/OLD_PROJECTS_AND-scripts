from turtle import Turtle, Screen
import pandas

turtle = Turtle()
turtle.penup()
screen = Screen()
screen.title("US STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# CODE TO GET COORDINATES
# def get_mouse_coordinate(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_coordinate)
# turtle.mainloop()
states_data = pandas.read_csv("50_states.csv")
state_list = states_data["state"].to_list()

answer_state = screen.textinput(title="guess the state ?", prompt="whats another states name?? ").title()

for state in state_list:
    if answer_state == state:
        x_coordinate = states_data[states_data["states"] == answer_state].index[0]
        x_coor = states_data.iloc[x_coordinate,:3]
        print(x_coor)
        turtle.teleport()

screen.exitonclick()
