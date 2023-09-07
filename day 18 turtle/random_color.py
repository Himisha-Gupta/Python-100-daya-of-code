import turtle
import random
from turtle import Turtle , Screen

tim = Turtle()

turtle.colormode(255)

def randomm_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)

    my_tuple = (r, b, g)
    return my_tuple


tim.pencolor(randomm_color())
tim.forward(100)
tim.left(120)
tim.forward(100)
tim.left(120)
screen = Screen()
screen.exitonclick()