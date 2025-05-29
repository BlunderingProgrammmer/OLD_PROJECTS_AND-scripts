from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    move_forward()
    tim.left(5)


def turn_right():
    move_backwards()
    tim.right(5)


def clearscreen():
    tim.reset()


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="c", fun=clearscreen)
screen.exitonclick()
