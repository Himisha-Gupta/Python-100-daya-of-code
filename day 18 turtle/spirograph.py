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
tim.speed(0)

#-----------------------------Method 1----------------------------------------------

def draw_spirograph(size_of_gap):
     for _ in range(int(360/size_of_gap)):
        tim.pencolor(randomm_color())
        tim.circle(50)
        tim.setheading(tim.heading()+ size_of_gap)


draw_spirograph(20)


#-----------------------------Method 2----------------------------------------------

# for _ in range(18):
#     tim.pencolor(randomm_color())
#     tim.circle(50)
#     tim.left(20)


screen = Screen()
screen.exitonclick()